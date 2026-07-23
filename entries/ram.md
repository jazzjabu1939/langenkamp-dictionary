---
layout: default
kind: glossary
title: "RAM"
permalink: /entries/ram/
date: 2026-07-23
summary: "Random-access memory: the fast working memory that lets computers, GPUs, phones, and AI data centers keep active work close to the processor. In the AI era, RAM is no longer a dull spec line. It is a strategic bottleneck."
draft: false
published: true
---

**RAM** is random-access memory: the fast, volatile working memory that lets a computer keep active work close to the processor.

For decades, RAM looked like a dull consumer specification. How many gigabytes does the laptop have? Can the gaming PC take two more DIMMs? Will the phone keep apps open in the background? In the AI era, that humble line item has become one of the hard constraints on the future. A model is not only logic. It is parameters loaded into memory, context held in memory, KV cache expanding through memory, and intermediate state moving through memory bandwidth.

The useful distinction is simple:

- **Storage** keeps things when the power goes off: SSDs, hard drives, flash cards.
- **RAM** holds the work that is alive right now.
- **Cache** is smaller, faster memory even closer to the processor.

People often say "memory" loosely, and the looseness matters. A 4 TB SSD is storage. A 128 GB Apple Silicon machine has RAM, though Apple calls it unified memory. An NVIDIA accelerator's HBM is RAM attached directly to the accelerator package. A server's DDR5 RDIMMs are RAM attached to the CPU. These are not interchangeable, but they all belong to the same physical problem: useful computation requires active state close enough, fast enough, and large enough.

## The main types

**SRAM** is static RAM. It is very fast and expensive, used primarily for CPU and accelerator caches. The user rarely buys it directly. It hides inside the processor and makes the processor less starved.

**DRAM** is dynamic RAM. This is the ordinary working memory of modern computers and servers. DDR4 and DDR5 are generations of synchronous DRAM used in desktops, workstations, and servers. DDR5 is the current mainstream standard for new systems, with JEDEC standards defining the electrical and functional requirements for compliant devices and modules.[^ddr5]

**LPDDR** is low-power DRAM. LPDDR5 and LPDDR5X are common in phones, tablets, thin laptops, and some AI accelerators where power efficiency and compact packaging matter. It is not "lesser" DRAM; it is optimized for a different envelope. JEDEC's LPDDR5/5X standard covers the device features, electrical characteristics, packages, and signal assignments for these parts.[^lpddr]

**GDDR** is graphics DRAM. It is built for very high bandwidth to GPUs, historically for games and visualization, now also for AI workstations and lower-cost accelerators. If someone says "VRAM" on a graphics card, they usually mean GDDR or HBM attached to the GPU, not ordinary system RAM.

**HBM** is high-bandwidth memory. It stacks DRAM dies vertically and places them close to the accelerator through advanced packaging. HBM is expensive, capacity-constrained, and central to frontier AI hardware because large models need enormous bandwidth between compute and memory. JEDEC published HBM3 as JESD238 for applications where bandwidth, power efficiency, and capacity per area matter, including graphics, high-performance computing, and servers.[^hbm3] HBM4 extends that same trajectory for AI and HPC systems.

**Unified memory** is not a new memory cell type. It is an architecture. On Apple Silicon, the CPU, GPU, and Neural Engine share one high-bandwidth memory pool instead of copying data between separate CPU RAM and GPU VRAM. This is why a 128 GB MacBook Pro can be interesting for local AI inference in a way that an older "128 GB RAM" workstation with a small discrete GPU might not be.

**CXL memory** is data-center memory attached through the Compute Express Link protocol, usually over PCIe. It does not replace the fastest local DRAM, but it gives servers a way to expand, pool, and tier memory when the CPU's ordinary memory channels are not enough. For AI systems, CXL belongs in the same conversation as KV cache, memory pooling, and data-center utilization.

## Why AI changed the market

The old consumer question was capacity: does this machine have enough RAM?

The AI question is capacity plus bandwidth plus placement. Can the model fit? Can the KV cache fit? Can the accelerator be fed quickly enough? Is the memory on the package, on the board, in a DIMM slot, across CXL, or across a network? The distance becomes economic.

This is why the 2026 RAM squeeze matters. TrendForce reported on 3 July 2026 that the DRAM market remained "extremely tight" in the third quarter, with conventional DRAM contract prices forecast to rise 13-18% quarter over quarter and NAND Flash 10-15%.[^trendforce-q3] It also noted that suppliers were reallocating capacity toward server applications, reducing available PC DRAM supply, while AI-related applications continued to receive priority allocation. A month earlier, TrendForce had reported that rapidly rising conventional DRAM contract prices drove first-quarter 2026 DRAM industry revenue up 81% quarter over quarter.[^trendforce-q1]

This is not just a PC-builder nuisance. It is the material signature of the AI buildout. Data centers are pulling memory upward into HBM, server DDR5, RDIMMs, enterprise SSDs, and CXL-adjacent architectures. Consumer devices still need RAM, but consumer buyers are less able to absorb rapid price increases than hyperscalers racing to build AI capacity.

The phrase *memory wall* used to describe a performance problem: processors could compute faster than memory systems could feed them. The 2026 version is broader. It is a market wall, a packaging wall, and a sovereignty wall. The model you can run is constrained by the RAM you can buy, the bandwidth you can afford, and the supply chain you can trust.

## Why it matters here

For this Dictionary, RAM belongs near *[Logic, Memory, Power](logic-memory-power.md)* because it names the middle term in physical AI scaling. It belongs near *[Sovereign Compute](sovereign-compute.md)* because local AI depends on how much working memory the operator owns. It belongs near *[KV Cache Explosion](kv-cache-explosion.md)* because long-context systems convert "more memory" from a metaphor into an invoice.

The M5 Max purchase was not just a faster-laptop purchase. It was a RAM purchase. The 128 GB of unified memory is what lets a home operator load serious open-weight models, run them locally, keep student or personal material off vendor systems, and experiment with the open tier without asking a hyperscaler for permission. The CPU and GPU matter. The RAM is what makes the sovereignty claim operational.

RAM is therefore one of the places where the cloud stops being a cloud. It becomes chips, wafers, packaging, inventory, allocation, electricity, and price. The software world keeps trying to float upward. RAM keeps pulling it back to earth.

## See also

- *[Logic, Memory, Power](logic-memory-power.md)*
- *[KV Cache Explosion](kv-cache-explosion.md)*
- *[Apple Silicon](apple-silicon.md)*
- *[M5 Max](m5-max.md)*
- *[Ollama](ollama.md)*
- *[Quantization](quantization.md)*
- *[Sovereign Compute](sovereign-compute.md)*
- *[Dusty Laptop](dusty-laptop.md)*

[^ddr5]: JEDEC, *JESD79-5B - DDR5 SDRAM*, publication date 1 September 2022. GlobalSpec's standards listing summarizes the scope as defining DDR5 SDRAM features, functionality, electrical characteristics, packages, and signal assignments: <https://standards.globalspec.com/std/14562454/jesd79-5b>.

[^lpddr]: JEDEC, *JESD209-5C - Low Power Double Data Rate (LPDDR) 5/5X*, publication date 1 June 2023. GlobalSpec's standards listing summarizes the LPDDR5/LPDDR5X scope: <https://standards.globalspec.com/std/14618092/jesd209-5c>.

[^hbm3]: JEDEC announced publication of JESD238 HBM3 on 27 January 2022, describing it as the High Bandwidth Memory DRAM standard for higher-bandwidth, lower-power, high-capacity-per-area applications including graphics processing, high-performance computing, and servers: <https://www.businesswire.com/news/home/20220127005320/en/JEDEC-Publishes-HBM3-Update-to-High-Bandwidth-Memory-HBM-Standard>.

[^trendforce-q3]: TrendForce, "AI Server Demand Continues to Support Memory Prices in 3Q26, but Gains Moderate as Consumer Demand Weakens and High Base Effects Take Hold," 3 July 2026: <https://www.trendforce.com/presscenter/news/20260703-13134.html>.

[^trendforce-q1]: TrendForce, "Rapid Contract Price Surge Drives 1Q26 DRAM Industry Up 81% QoQ," 1 June 2026: <https://www.trendforce.com/presscenter/news/20260601-13070.html>.
