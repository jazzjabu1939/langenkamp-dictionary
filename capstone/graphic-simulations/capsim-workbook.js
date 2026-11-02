// Capsim Courier workbook reader for the Capstone Graphic Simulations.
// Reads the .xlsx in the browser (no upload, no libraries). Used by The Second Shift,
// Spreading the Overhead and Big Al Comes Calling. Money in $M, units in thousands.
const CapsimWB = (() => {
  const SEGMENTS = ["Traditional", "Low End", "High End", "Performance", "Size"];
  const num = x => { x = String(x ?? "").replace(/[$,]/g, "").trim(); return x.endsWith("%") ? parseFloat(x) / 100 : parseFloat(x); };

  async function unzip(buf) {
    const dv = new DataView(buf), u8 = new Uint8Array(buf), files = {};
    let e = buf.byteLength - 22;
    while (e >= 0 && dv.getUint32(e, true) !== 0x06054b50) e--;
    if (e < 0) throw new Error("not an .xlsx file");
    let p = dv.getUint32(e + 16, true);
    for (let i = 0, n = dv.getUint16(e + 10, true); i < n; i++) {
      const nlen = dv.getUint16(p + 28, true);
      files[new TextDecoder().decode(u8.subarray(p + 46, p + 46 + nlen))] =
        { method:dv.getUint16(p + 10, true), size:dv.getUint32(p + 20, true), off:dv.getUint32(p + 42, true) };
      p += 46 + nlen + dv.getUint16(p + 30, true) + dv.getUint16(p + 32, true);
    }
    return async name => {
      const f = files[name]; if (!f) return null;
      const start = f.off + 30 + dv.getUint16(f.off + 26, true) + dv.getUint16(f.off + 28, true);
      const data = u8.subarray(start, start + f.size);
      if (f.method === 0) return new TextDecoder().decode(data);
      return new Response(new Blob([data]).stream().pipeThrough(new DecompressionStream("deflate-raw"))).text();
    };
  }

  async function readSheets(buf, names) {
    const get = await unzip(buf), P = s => new DOMParser().parseFromString(s, "application/xml");
    const ssx = await get("xl/sharedStrings.xml");
    const ss = ssx ? [...P(ssx).getElementsByTagName("si")].map(si => si.textContent) : [];
    const tgt = {};
    for (const r of P(await get("xl/_rels/workbook.xml.rels")).getElementsByTagName("Relationship")) tgt[r.getAttribute("Id")] = r.getAttribute("Target");
    const out = {};
    for (const s of P(await get("xl/workbook.xml")).getElementsByTagName("sheet")) {
      if (!names.includes(s.getAttribute("name"))) continue;
      let t = tgt[s.getAttribute("r:id")].replace(/^\//, ""); if (!t.startsWith("xl/")) t = "xl/" + t;
      out[s.getAttribute("name")] = [...P(await get(t)).getElementsByTagName("row")].map(row => {
        const cells = [];
        for (const c of row.getElementsByTagName("c")) {
          const col = [...c.getAttribute("r").replace(/\d+/g, "")].reduce((a, ch) => a * 26 + ch.charCodeAt(0) - 64, 0) - 1;
          const v = c.getElementsByTagName("v")[0], is = c.getElementsByTagName("is")[0];
          cells[col] = is ? is.textContent : v ? (c.getAttribute("t") === "s" ? ss[+v.textContent] : v.textContent) : "";
        }
        return cells;
      });
    }
    return out;
  }

  // Rows after the header row whose first cell is `first`, as objects keyed by header text.
  function table(rows, first, file, sheet) {
    const hi = (rows || []).findIndex(r => r && r[0] === first);
    if (hi < 0) throw new Error(`${file}: the ${sheet} sheet has no "${first}" table.`);
    const H = rows[hi].map(h => (h || "").trim()), out = [];
    for (const r of rows.slice(hi + 1)) { if (!r || !r[0]) break; const o = {}; H.forEach((h, i) => o[h] = r[i]); out.push(o); }
    return out;
  }
  const need = (o, keys, file) => keys.forEach(k => { if (!(k in o)) throw new Error(`${file}: missing column "${k}".`); });

  async function read(file) {
    const sh = await readSheets(await file.arrayBuffer(), ["Production", "High Level Overview", "Finance", ...SEGMENTS]);
    if (!sh["Production"]) throw new Error(`${file.name} has no Production sheet. Is it a Capsim Courier workbook?`);
    const company = {};
    "Andrews Baldwin Chester Digby Erie Ferris Garrett Harper".split(" ").forEach(n => company[n[0]] = n);
    const names = (sh["High Level Overview"] || []).find(r => r && r.slice(1).filter(Boolean).length >= 4 && r.slice(1).filter(Boolean).every(x => isNaN(num(x))));
    if (names) names.slice(1).forEach(n => { if (n && n !== "Average") company[n[0]] = n; });

    // Per-product sales and promotion budgets, from each segment's product table.
    // Also each segment's buying criteria and product table (used by The Demand Whiteboard).
    const budgets = {}, segments = {}; let year = "";
    const nums = s => (String(s ?? "").replace(/,/g, "").match(/\d+(\.\d+)?/g) || []).map(Number);
    SEGMENTS.forEach(seg => {
      const rows = sh[seg]; if (!rows) return;
      const y = rows.map(r => r && r[0] && String(r[0]).match(/^(\d{4}) Total Market Size/)).find(Boolean);
      if (y) year = y[1];
      if (!rows.some(r => r && r[0] === "Name")) return;
      const t = table(rows, "Name", file.name, seg);
      t.forEach(r => (budgets[r["Name"]] ||= {})[seg] = [num(r["Sales Budget"]) / 1000, num(r["Promo Budget"]) / 1000]);
      const S = segments[seg] = { products:t.map(r => ({ name:r["Name"], price:num(r["Price"]), units:num(r["Units Sold"]), pot:num(r["Potential Sold"]), age:num(r["Age"]),
        pf:num(r["Performance"]), sz:num(r["Size"]), mtbf:num(r["Reliability"]), salesB:num(r["Sales Budget"]) / 1000,
        acc:num(r["Customer Accessibility"]), promoB:num(r["Promo Budget"]) / 1000, aw:num(r["Customer Awareness"]), score:num(r["Customer Satisfaction"]) })) };
      rows.forEach(r => {
        if (!r || !r[0]) return; const k = String(r[0]).trim(), v = nums(r[1]), w = num(r[2]);
        if (/Total Market Size$/.test(k)) S.size = num(r[1]);
        else if (/Demand Growth Rate$/.test(k)) S.growth = num(r[1]);
        else if (k === "Age" && /Year/i.test(r[1]) && S.age == null) { S.age = v[0]; S.wAge = w; }
        else if (k === "Price" && v.length === 2 && !S.price) { S.price = v; S.wPrice = w; }
        else if (k === "Positioning" && v.length === 2 && !S.ideal) { S.ideal = v; S.wPos = w; }
        else if ((k === "Reliability" || k === "MTBF") && v.length === 2 && !S.mtbf) { S.mtbf = v; S.wMtbf = w; }
      });
    });

    const prodRows = table(sh["Production"], "Name", file.name, "Production");
    need(prodRows[0] || {}, ["Primary Segment", "Units Sold", "Inventory", "Revision Date", "Age Dec.31", "Price", "Material Cost", "Labor Cost",
      "Auto. Next Round", "Capacity Next Round", "Plant Utilization"], file.name);
    const products = {};
    prodRows.forEach(r => {
      const n = r["Name"], seg = r["Primary Segment"] || "—", b = budgets[n] || {};
      const sp = b[seg] || Object.values(b)[0] || [0, 0];
      products[n] = { name:n, key:company[n[0]] || n[0], seg, sold:num(r["Units Sold"]), inv:num(r["Inventory"]), age:num(r["Age Dec.31"]),
        rev:r["Revision Date"], price:num(r["Price"]), mat:num(r["Material Cost"]), lab:num(r["Labor Cost"]), autoN:num(r["Auto. Next Round"]),
        capN:num(r["Capacity Next Round"]), util:num(r["Plant Utilization"]), salesB:sp[0], promoB:sp[1] };
    });

    // Company income statement, balance sheet, cash flow, stock and bonds (Finance sheet).
    const companies = {}; let prime = NaN;
    const fin = sh["Finance"];
    if (fin) {
      const cos = (fin[1] || []).slice(1).filter(Boolean);
      const row = (label, nth = 0) => fin.filter(r => r && r[0] && String(r[0]).startsWith(label))[nth] || [];
      const at = (label, j, nth) => num(row(label, nth)[j]) / 1000;
      const sm = fin.findIndex(r => r && r[0] === "Stock Market Summary"), bm = fin.findIndex(r => r && r[0] === "Bond Market Summary");
      const pr = fin.find(r => r && r[0] && String(r[0]).startsWith("Next Year's Prime")); if (pr) prime = num(pr[1]) / 100;
      cos.forEach((co, i) => {
        const j = i + 1;
        const stock = fin.slice(sm + 2, bm).find(r => r && r[0] === co) || [];
        const bonds = fin.slice(bm + 2).filter(r => r && r[0] === co && /S\d{4}$/.test(r[1] || ""));
        const face = bonds.reduce((t, b) => t + num(b[2]) / 1e6, 0), matures = {};
        bonds.forEach(b => { const y = b[1].split("S")[1]; matures[y] = (matures[y] || 0) + num(b[2]) / 1e6; });
        companies[co] = { rev:at("Sales", j), vc:at("Total Variable Costs", j), sga:at("SG&A", j), other:at("Other", j),
          cash:at("Cash", j), ar:at("Accounts Receivable", j), inv:at("Inventory", j), pe:at("Plant and Equipment", j),
          ad:-at("Accumulated Depreciation", j), ap:at("Accounts Payable", j), cd:at("Current Debt", j), ltd:at("Long-Term Debt", j),
          eq:at("Total Equity", j), capex:-at("Net Plant Improvements", j), dinv:-at("Inventory", j, 1), int:at("Interest", j),
          el:at("Cash From Emergency Loan", j), shares:num(stock[3]) / 1e6, price:num(stock[1]),
          coupon:face ? bonds.reduce((t, b) => t + parseFloat(b[1]) / 100 * num(b[2]) / 1e6, 0) / face : 0.129, matures, budgets:0 };
      });
      Object.values(products).forEach(p => { if (companies[p.key]) companies[p.key].budgets += p.salesB + p.promoB; });
    }
    const ind = file.name.match(/CP\d+/i), rd = file.name.match(/round_?(\d+)(?:_(\d{4}))?/i);
    if (rd && rd[2]) year = rd[2];
    // Capstone 2.0 industries start in 2026 (Round 0), so Round N reports year 2026 + N.
    const round = rd ? +rd[1] : year ? +year - 2026 : null;
    return { name:file.name, industry:ind ? ind[0].toUpperCase() : "", round, year, products, companies, prime, segments };
  }

  // Order two workbooks as {cur, prev}; reject different industries.
  function pair(a, b) {
    if (!b) return { cur:a, prev:null };
    if (a.industry && b.industry && a.industry !== b.industry) throw new Error(`the two workbooks are from different industries (${a.industry}, ${b.industry}).`);
    let later;
    if (a.round != null && b.round != null && a.round !== b.round) later = a.round > b.round;
    else {
      // An unrevised product (same revision date in both) is older in the later workbook.
      const k = Object.keys(a.products).find(k => b.products[k] && a.products[k].rev === b.products[k].rev && a.products[k].age !== b.products[k].age);
      later = k ? a.products[k].age > b.products[k].age : true;
    }
    return later ? { cur:a, prev:b } : { cur:b, prev:a };
  }

  // Wire a Load .xlsx button, a hidden file input and page-wide drag and drop. Returns the loader (also handy for tests).
  function wire({ button, input, note, onFiles }) {
    button.addEventListener("click", () => input.click());
    input.addEventListener("change", e => { go([...e.target.files]); e.target.value = ""; });
    document.addEventListener("dragover", e => e.preventDefault());
    document.addEventListener("drop", e => { e.preventDefault(); go([...e.dataTransfer.files].filter(f => /\.xlsx$/i.test(f.name))); });
    async function go(files) {
      if (!files.length) return;
      try {
        if (files.length > 2) throw new Error("load one or two workbooks: this round's, plus last round's.");
        note.textContent = "Reading…";
        const [a, b] = await Promise.all(files.map(read));
        note.textContent = await onFiles(pair(a, b));
      } catch (err) { note.textContent = `Could not load: ${err.message}`; }
    }
    return go;
  }

  return { read, pair, wire, num, SEGMENTS };
})();
