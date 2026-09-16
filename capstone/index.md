---
layout: default
title: "Capstone 2.0 Glossary & Guidance"
description: "A student guide to the Courier, financial calculations and simulation decisions."
permalink: /capstone/
---

<style>
.capstone-guide {font-family:Georgia,"Times New Roman",serif;color:#222;}
.capstone-guide h2,.capstone-guide h3 {color:#881c1c;}
.capstone-guide h2 {border-bottom:1px solid #ddd;padding-bottom:.4rem;margin-top:2rem;}
.capstone-guide .cap-intro {border-left:4px solid #881c1c;background:#f8f3f0;padding:1rem 1.2rem;}
.capstone-guide .cap-term {margin:1.2rem 0;}
.capstone-guide .cap-term h3 {font-size:1.15rem;margin-bottom:.35rem;}
.capstone-guide input {width:100%;padding:.8rem;font:inherit;border:1px solid #aaa;border-radius:4px;box-sizing:border-box;}
.capstone-guide table {font-size:.95rem;}
.capstone-guide th {background:#881c1c;color:white;}
@media print {.page-header,.return-bar,.site-footer,.cap-search {display:none!important;} .cap-term{display:block!important;} .capstone-guide h2 {break-after:avoid;}}
</style>
<div class="capstone-guide" markdown="1">

# Capstone 2.0 Glossary & Guidance

*Matthew D. Langenkamp · Isenberg School of Management, UMass Amherst*  
*Prepared in collaboration with Thea · Updated September 15, 2026*

<div class="cap-intro" markdown="1">
Start with the money before choosing the strategy. What did we sell? What did it cost? What profit remained? Where did the cash go?

This is an independent teaching companion, not an official Capsim publication or a Dictionary entry. Definitions summarize the public Capstone 2.0 Team Member Guide and financial headings in an archived class Courier. Your live simulation’s instructions and Industry Conditions Report take precedence for configuration-specific figures.
</div>

## Start here: the calculations to learn first

1. **Sales:** price × units sold.
2. **Contribution:** sales − variable costs; divide by sales for the percentage.
3. **Depreciation:** allocate asset cost over its accounting life; distinguish expense from payment.
4. **Profit:** follow contribution → period costs → EBIT → interest/taxes → net profit.
5. **Financial position:** assets = liabilities + equity.
6. **Cash:** reconcile operating, investing and financing flows.
7. **Performance:** ROS, asset turnover, ROA, leverage and ROE.
8. **Planning:** forecast sales, subtract available inventory, and check production capacity.

**For class:** [Download the financial foundations exercise (PDF)](/assets/capstone/Capstone-Financial-Foundations.pdf). Work individually. It uses invented figures, not another team’s confidential results. No submission deadline is set on this page.

## A worked example: margin is not profit

Suppose a company sells **1 million sensors at $30 each**. Its report, in **$ thousands**, shows:

| Line | $000 | Calculation |
|---|---:|---|
| Sales | 30,000 | 1,000 thousand units × $30 |
| Material and labor | 16,000 | Costs of units sold |
| Inventory carrying cost | 600 | Separate from the inventory asset |
| Contribution | 13,400 | 30,000 − 16,000 − 600 |
| Depreciation | 2,000 | Non-cash allocation of asset cost |
| SG&A | 5,400 | Includes the listed component budgets |
| EBIT | 6,000 | 13,400 − 2,000 − 5,400; no other operating items |
| Interest | 1,000 | Financing expense |
| Taxes | 1,500 | Assumed for this example |
| Net profit | 3,500 | No profit sharing or other adjustments |

Contribution margin is **44.67%**; return on sales is **11.67%**. They answer different questions. Neither tells you the ending cash balance. These example inputs are hypothetical; the exercise uses them to practice interpretation, not memorization.

## Find a term

<div class="cap-search">
<label for="cap-search"><strong>Search terms and explanations</strong></label>
<input id="cap-search" type="search" placeholder="Try contribution, depreciation, cash or automation" aria-describedby="cap-count">
<p id="cap-count" role="status" aria-live="polite"></p>
</div>


<section class="cap-group" markdown="1">

## Read the reports

<article class="cap-term" id="capstone-courier" markdown="1">

### Capstone Courier

The industry report showing completed-round company results, product data, segment conditions and competitors. It is evidence about what happened, not a guarantee of what happens next. Read the round and units before interpreting a number.

</article>

<article class="cap-term" id="industry-conditions-report" markdown="1">

### Industry Conditions Report

The starting description of your specific simulation industry: customer buying criteria, initial segment positions and growth assumptions. It is available from your simulation dashboard. Use your own report, not another class’s numbers. The supplied September 15 report informs the examples below; verify that its settings match your industry.

</article>

<article class="cap-term" id="annual-report" markdown="1">

### Annual report

Your company’s detailed financial statements for a completed year. Use it to explain the headline ratios in the Courier.

</article>

<article class="cap-term" id="pro-forma-statements" markdown="1">

### Pro forma statements

Projected income statement, balance sheet and cash flow statement based on your decisions and forecasts. A spreadsheet can balance perfectly while its sales forecast is wrong. Compare forecast and actual results after each round.

</article>

<article class="cap-term" id="round-and-reporting-date" markdown="1">

### Round and reporting date

A decision round represents a simulated year. At the start of Round 2 you normally have Round 1 results. Distinguish past results, current decisions and investments that become available next round.

</article>

<article class="cap-term" id="units-and-dollar-scaling" markdown="1">

### Units and dollar scaling

A report may show dollars in thousands and quantities in thousands while price remains dollars per unit. Thus 1,000 thousand units × $30 = $30,000 thousand revenue ($30 million). A value of 0.25 means 25%, not 0.25%. Read each table’s labels; share counts and unit prices need not use the same scale.

</article>

</section>

<section class="cap-group" markdown="1">

## Sales, costs and profit

<article class="cap-term" id="revenue-sales" markdown="1">

### Revenue / sales

The value of products sold during the period. For one product at one price: **sales = price × units sold**. Add product revenues to get company sales. Production does not itself create revenue; unsold production is inventory. Sales are not necessarily cash collected in the same period.

</article>

<article class="cap-term" id="units-sold" markdown="1">

### Units sold

The number of products purchased by customers. Distinguish units sold from units produced, forecast units, and available capacity.

</article>

<article class="cap-term" id="price" markdown="1">

### Price

The selling price per unit. A higher price increases revenue per unit but can reduce customer appeal and volume. A lower price is not automatically a successful cost-leadership strategy.

</article>

<article class="cap-term" id="material-cost" markdown="1">

### Material cost

The cost of materials used in products. Product specifications and reliability affect it. For income-statement calculations use the costs associated with units sold; the cost of unsold units remains in inventory.

</article>

<article class="cap-term" id="labor-cost" markdown="1">

### Labor cost

The production labor cost. Automation can reduce labor requirements. Second-shift labor is more expensive than first-shift labor; the guide specifies a 50% second-shift labor premium, not a 50% increase in total product cost.

</article>

<article class="cap-term" id="variable-costs" markdown="1">

### Variable costs

Costs that change with activity. Capstone’s financial presentation groups labor, material and inventory carrying costs as variable costs. Use the report’s total rather than treating material plus labor as the entire figure in every situation.

</article>

<article class="cap-term" id="cost-of-goods-sold-cogs" markdown="1">

### Cost of goods sold (COGS)

The cost attached to the products actually sold. Do not expense all production as COGS if some output is still inventory. For Capstone calculations, follow its labelled labor, material and carrying-cost lines; do not silently substitute a different textbook classification.

</article>

<article class="cap-term" id="inventory-carrying-cost" markdown="1">

### Inventory carrying cost

The expense of holding unsold inventory, distinct from the inventory asset itself. The public guide specifies a 12% carrying-cost rate; use the simulation’s reported charge for reconciliation. Inventory is valued at cost, not at hoped-for selling price. A carrying expense is not the same as buying or producing the inventory.

</article>

<article class="cap-term" id="unit-contribution" markdown="1">

### Unit contribution

For a simplified product: **price − variable cost per unit**. At $30 price and $16 material-plus-labor cost, this is $14 before carrying costs. This is not net profit per unit.

</article>

<article class="cap-term" id="contribution-margin-dollars" markdown="1">

### Contribution margin — dollars

**Sales − total variable costs**. This amount is available to cover period costs and other expenses before profit. With $30m sales and $16.6m variable costs, contribution is $13.4m.

</article>

<article class="cap-term" id="contribution-margin-percentage" markdown="1">

### Contribution margin — percentage

**Contribution margin dollars ÷ sales × 100**. $13.4m ÷ $30m = 44.67%. A 45% margin is a rate, not $45 profit. Compare both the percentage and total dollars.

</article>

<article class="cap-term" id="fixed-costs-period-costs" markdown="1">

### Fixed costs / period costs

Costs not directly proportional to current unit sales over the relevant range. Capstone period costs include depreciation and SG&A, including R&D, promotion, sales and administration. “Fixed” does not mean management cannot change the budget.

</article>

<article class="cap-term" id="sg-a" markdown="1">

### SG&A

Selling, general and administrative expenses. Capstone includes R&D, promotion, sales and administration in this grouping. **SG&A-to-sales = SG&A ÷ sales**. Do not subtract the component budgets again after subtracting total SG&A.

</article>

<article class="cap-term" id="r-d-expense" markdown="1">

### R&D expense

The reported expense of developing or revising a product. It differs from purchasing production equipment. Spending is not evidence of a successful redesign; completion date and customer fit matter.

</article>

<article class="cap-term" id="depreciation" markdown="1">

### Depreciation

Allocation of the depreciable cost of plant and equipment over its accounting life. **Straight-line depreciation = (cost − residual value) ÷ useful life**. The public Capstone 2.0 guide uses a 15-year straight-line life. A $30m depreciable asset with zero residual value and a full year in service yields $2m annual depreciation. This is a non-cash expense in that year, not a new payment and not the current market value of the asset.

</article>

<article class="cap-term" id="accumulated-depreciation-net-plant" markdown="1">

### Accumulated depreciation / net plant

Accumulated depreciation is depreciation recorded to date. **Net plant = gross plant and equipment − accumulated depreciation**. If the report displays accumulated depreciation as a negative number, add the signed number rather than subtracting it twice. Net book value is not necessarily resale value.

</article>

<article class="cap-term" id="net-margin-capstone-product-view" markdown="1">

### Net margin — Capstone product view

In the guide’s product analysis, **product contribution − product period costs**. This is not automatically company net profit or a percentage. Company-level other expenses, interest, taxes and profit sharing may remain to be deducted.

</article>

<article class="cap-term" id="ebit-operating-result" markdown="1">

### EBIT / operating result

Earnings before interest and taxes. In the guide’s statement structure: **contribution − depreciation − SG&A − other listed operating expenses = EBIT**. If other items are shown as signed adjustments, respect their signs. EBIT is neither revenue nor cash flow.

</article>

<article class="cap-term" id="interest-expense" markdown="1">

### Interest expense

The cost of borrowing, not repayment of principal. Interest reduces profit. Repaying principal reduces cash and debt without being an income-statement expense.

</article>

<article class="cap-term" id="taxes-and-profit-sharing" markdown="1">

### Taxes and profit sharing

Deductions shown after operating results and interest in the simulation’s income statement. Use the actual report lines. Do not assume a tax refund or a profit-sharing rate without checking the configured simulation.

</article>

<article class="cap-term" id="net-profit-net-income" markdown="1">

### Net profit / net income

The final company income-statement result. **EBIT − interest − taxes − profit sharing**, following any other displayed adjustments. Profit can be positive while cash falls or the firm requires an emergency loan.

</article>

<article class="cap-term" id="cumulative-profit" markdown="1">

### Cumulative profit

The sum of net profits over the reported rounds. It is not the cash balance. It also need not equal retained earnings, which include opening balances and dividend effects.

</article>

<article class="cap-term" id="break-even-volume" markdown="1">

### Break-even volume

In a simple constant-price, constant-unit-cost model: **fixed costs ÷ unit contribution**. The contribution must be positive. State which expenses are included. Capacity limits, second shifts, demand changes and carrying costs can make a simple threshold misleading.

</article>

</section>

<section class="cap-group" markdown="1">

## Assets, financing and cash

<article class="cap-term" id="balance-sheet" markdown="1">

### Balance sheet

A snapshot at a date. Its identity is **assets = liabilities + shareholders’ equity**. Unlike an income statement, it is not a year’s flow of revenues and expenses.

</article>

<article class="cap-term" id="cash" markdown="1">

### Cash

Money available at the reporting date. **Ending cash = beginning cash + operating cash flow + investing cash flow + financing cash flow**. Cash is not revenue, profit, unused capacity or retained earnings.

</article>

<article class="cap-term" id="accounts-receivable-a-r" markdown="1">

### Accounts receivable (A/R)

Sales not yet collected from customers. An increase generally uses operating cash relative to reported profit. Credit terms can affect both customer appeal and the time before cash arrives.

</article>

<article class="cap-term" id="inventory" markdown="1">

### Inventory

Unsold products carried as an asset at cost. **Ending units = beginning units + units produced − units sold** in a simple model with no write-offs. Higher inventory usually ties up operating cash; a stockout can sacrifice sales.

</article>

<article class="cap-term" id="current-assets" markdown="1">

### Current assets

Typically cash, receivables and inventory in the simulation. These are not equally liquid: inventory cannot be used to pay a lender without being converted into cash.

</article>

<article class="cap-term" id="plant-and-equipment-capacity-investment" markdown="1">

### Plant and equipment / capacity investment

Long-lived production assets. Buying capacity or automation consumes cash as an investment, rather than becoming a full immediate operating expense. Depreciation allocates the relevant asset cost over time.

</article>

<article class="cap-term" id="accounts-payable-a-p" markdown="1">

### Accounts payable (A/P)

Amounts owed to suppliers. An increase generally preserves operating cash temporarily; it does not create revenue or erase the obligation.

</article>

<article class="cap-term" id="current-debt" markdown="1">

### Current debt

Short-term borrowing obligations. Inspect repayment and refinancing requirements in Finance; do not assume debt renews indefinitely. Borrowing raises cash and liabilities, not sales or profit.

</article>

<article class="cap-term" id="long-term-debt-bonds" markdown="1">

### Long-term debt / bonds

Borrowing with a longer maturity. Face value is principal; interest is the cost of borrowing; maturity is when principal is due. Bond yield and the coupon rate are not necessarily the same. Check the simulation’s financing limits and transaction costs.

</article>

<article class="cap-term" id="emergency-loan" markdown="1">

### Emergency loan

Automatic financing used when the simulated firm cannot cover its cash needs under the game’s rules. It signals a financing or forecasting problem and carries costs. Diagnose inventory, collections, investment and repayments instead of treating it as ordinary planned revenue.

</article>

<article class="cap-term" id="common-stock-shares-issued" markdown="1">

### Common stock / shares issued

Equity capital raised by issuing shares. Issuance raises cash and equity, not revenue. The balance-sheet common-stock amount is not the company’s current stock-market valuation; issuing shares can dilute earnings per share.

</article>

<article class="cap-term" id="retained-earnings" markdown="1">

### Retained earnings

Accumulated earnings retained in the business rather than distributed. In a simple bridge: **ending retained earnings = beginning retained earnings + net profit − dividends**. Retained earnings are an equity account, not a separate cash reserve.

</article>

<article class="cap-term" id="equity" markdown="1">

### Equity

The owners’ residual accounting interest: **assets − liabilities**. Negative equity means liabilities exceed book assets. Return ratios using tiny or negative equity can be misleading.

</article>

<article class="cap-term" id="dividends-share-repurchases" markdown="1">

### Dividends / share repurchases

Distributions to shareholders. They use financing cash rather than being operating expenses. Dividends reduce retained earnings; repurchases reduce equity and share count according to the simulation’s accounting.

</article>

<article class="cap-term" id="working-capital-current-ratio" markdown="1">

### Working capital / current ratio

**Net working capital = current assets − current liabilities**; **current ratio = current assets ÷ current liabilities**. Neither assures immediate cash availability. A warehouse full of unwanted sensors can make current assets look comfortable while cash is scarce.

</article>

<article class="cap-term" id="cash-flow-from-operations-cfo" markdown="1">

### Cash flow from operations (CFO)

Cash generated or consumed by operations. A simplified indirect bridge is **net profit + depreciation − increase in A/R − increase in inventory + increase in A/P**, plus any other relevant adjustments. Depreciation is added back because it reduced profit without a current cash payment; the add-back does not create cash.

</article>

<article class="cap-term" id="investing-cash-flow-capital-expenditure" markdown="1">

### Investing cash flow / capital expenditure

Cash spent on or received from long-lived assets. A plant purchase is typically an investing outflow. Distinguish an investment’s cash payment from its annual depreciation expense.

</article>

<article class="cap-term" id="financing-cash-flow" markdown="1">

### Financing cash flow

Cash from borrowing and issuing shares, less debt principal repayments, dividends and share repurchases. Financing changes how the business is funded; it is not customer demand or operating profit.

</article>

<article class="cap-term" id="free-cash-flow" markdown="1">

### Free cash flow

A common teaching measure is **operating cash flow − capital expenditures**. Label the definition: it is not necessarily a separately reported Courier measure. Negative free cash flow during expansion requires financing but does not by itself prove a bad strategy.

</article>

</section>

<section class="cap-group" markdown="1">

## Courier ratios and performance

<article class="cap-term" id="return-on-sales-ros" markdown="1">

### Return on sales (ROS)

**Net profit ÷ sales × 100**. Also called net profit margin in general financial analysis. Do not substitute EBIT or the product-view net margin for net profit.

</article>

<article class="cap-term" id="asset-turnover" markdown="1">

### Asset turnover

**Sales ÷ total assets**, expressed as times (for example, 1.2×), not a profit percentage. The archived Courier reconciles to year-end assets. General accounting texts sometimes use average assets; state the denominator and follow your report.

</article>

<article class="cap-term" id="return-on-assets-roa" markdown="1">

### Return on assets (ROA)

For the Courier convention used here, **net profit ÷ total assets × 100**. It equals ROS × asset turnover when both use consistent figures. Other finance contexts may define return differently; do not mix them.

</article>

<article class="cap-term" id="leverage-courier" markdown="1">

### Leverage — Courier

**Total assets ÷ total equity**: the equity multiplier, not debt divided by equity. With $35m assets and $15m equity it is 2.33×. Leverage amplifies losses as well as returns.

</article>

<article class="cap-term" id="return-on-equity-roe" markdown="1">

### Return on equity (ROE)

**Net profit ÷ equity × 100**. With consistent denominators, **ROE = ROS × asset turnover × leverage**. A seemingly positive ROE caused by negative profit divided by negative equity is not healthy performance.

</article>

<article class="cap-term" id="earnings-per-share-eps" markdown="1">

### Earnings per share (EPS)

**Net profit ÷ the applicable number of shares**. Keep dollar and share units consistent and follow the simulation’s share-count convention. EPS is not a dividend or a stock price.

</article>

<article class="cap-term" id="stock-price-market-capitalization" markdown="1">

### Stock price / market capitalization

Stock price is the simulated market value per share. **Market capitalization = stock price × shares outstanding**. Neither equals balance-sheet cash or book equity. A higher share price alone does not diagnose the operating strategy.

</article>

<article class="cap-term" id="market-share-actual-and-potential" markdown="1">

### Market share — actual and potential

Actual share is sales captured, using the specified segment/industry and units/revenue denominator. Potential share estimates demand allocation without some availability constraints in the report’s model. Stockouts can make actual and potential differ. Do not add unit shares to revenue shares or assume last round’s share will persist.

</article>

<article class="cap-term" id="balanced-scorecard-scoring" markdown="1">

### Balanced Scorecard / scoring

A collection of performance measures, not a financial statement. Metrics, weights and enabled modules can vary by course. Read your simulation’s scoring rules; do not equate a stock price, one margin or one year’s profit with the entire score.

</article>

</section>

<section class="cap-group" markdown="1">

## Decision terms you will meet next

<article class="cap-term" id="sales-forecast" markdown="1">

### Sales forecast

Your estimate of units customers will buy. It informs production and pro forma finances but does not cause sales. Test a downside case before committing cash.

</article>

<article class="cap-term" id="production-schedule" markdown="1">

### Production schedule

Units you choose to manufacture. A starting formula is **forecast sales + desired ending inventory − beginning inventory**, subject to capacity and timing. Sales exceeding production may simply draw down opening inventory.

</article>

<article class="cap-term" id="capacity-plant-utilization" markdown="1">

### Capacity / plant utilization

First-shift capacity is an annual output capability. The guide permits up to twice first-shift capacity using a second shift. **Utilization ≈ production ÷ first-shift capacity × 100**, following the report’s exact convention. Over 100% can indicate second-shift use, not an impossible factory. Capacity purchased this round becomes available next round.

</article>

<article class="cap-term" id="automation" markdown="1">

### Automation

Investment that reduces labor requirements per unit but costs cash and can lengthen later R&D repositioning projects. Changes take a year to become available. Do not finance today’s price cut with tomorrow’s unearned savings.

</article>

<article class="cap-term" id="positioning-perceptual-map" markdown="1">

### Positioning / perceptual map

A product’s performance and size relative to a segment’s moving preferences. More performance or smaller size is not always better for every customer. Use the current industry’s coordinates and movement rates.

</article>

<article class="cap-term" id="age-revision-date" markdown="1">

### Age / revision date

Perceived age is time since introduction, adjusted by repositioning. A repositioning project halves perceived age at completion; aging then continues. An MTBF-only change does not halve age. A late revision does not improve the entire year retroactively.

</article>

<article class="cap-term" id="mtbf-reliability" markdown="1">

### MTBF / reliability

Mean Time Before Failure, expressed in hours. Higher reliability can improve appeal within a segment’s relevant range but increases material cost. It is neither product age nor a guarantee that more is always profitable.

</article>

<article class="cap-term" id="promotion-awareness" markdown="1">

### Promotion / awareness

Promotion spending builds the proportion of customers who know about a product. Awareness can decay over time. Dollars spent and awareness percentage are different measures; more spending faces diminishing returns.

</article>

<article class="cap-term" id="sales-budget-accessibility" markdown="1">

### Sales budget / accessibility

Spending that supports sales and distribution access within a segment. It is not sales revenue. Accessibility concerns customers’ ability to buy; awareness concerns their knowledge that the product exists.

</article>

<article class="cap-term" id="customer-buying-criteria-survey-score" markdown="1">

### Customer buying criteria / survey score

Customers weigh price, age, reliability and positioning differently by segment. Survey scores also reflect other relevant conditions. A price importance of 53% is a scoring weight, not a price elasticity, a demand forecast or a promised market share.

</article>

<article class="cap-term" id="segment-demand-growth" markdown="1">

### Segment demand / growth

Total customer demand in a segment. **Next-year demand = current demand × (1 + growth rate)** under the stated growth assumption. Your sales also depend on your competitive share and availability; segment growth is not automatically your growth.

</article>

<article class="cap-term" id="cost-leadership-differentiation" markdown="1">

### Cost leadership / differentiation

Cost leadership seeks a relative cost advantage while meeting customer requirements. Differentiation seeks buyer-valued distinctiveness that can support a premium. Neither means “always cheapest” or “spend the most.” These strategic choices are explored after the financial foundations.

</article>

<article class="cap-term" id="optional-modules-hr-tqm-and-sustainability" markdown="1">

### Optional modules: HR, TQM and sustainability

Additional decisions and costs or benefits when enabled. Do not assume another course’s settings apply to yours; inspect the relevant module documentation and report lines.

</article>

<article class="cap-term" id="tqm-investments-and-diminishing-returns" markdown="1">

### TQM investments and diminishing returns

The supplied TQM guide describes initiatives that can reduce material, labor and administrative costs, shorten R&D cycle time, or increase demand. Benefits begin in the investment year and persist into following years. Complementary initiatives can support the same objective, but repeated spending eventually yields smaller or no additional benefits. Maximum cumulative impacts are ceilings, not guaranteed annual improvements. Check Projected Cumulative Impacts before committing funds. These optional decisions are outside the introductory financial exercise.

</article>

</section>


## A routine before submitting decisions

- Check the units and round on the report.
- Explain changes in sales, contribution and net profit separately.
- Reconcile ending cash; inspect inventory and debt repayments.
- Run a lower-sales forecast. A pro forma cash surplus is conditional on its assumptions.
- Confirm R&D completion dates and next-round availability of plant changes.
- Record what would make you revise your decision.

## Reading the supplied Industry Conditions Report

The report distinguishes **segment centers** from **ideal spots**. Add the segment’s ideal-spot offset to its center; do not treat them as interchangeable. For example, the supplied High End Round 0 center is performance 7.5 / size 12.5. Its offset is +1.4 / −1.4, giving an ideal spot of **8.9 / 11.1**. Positions drift monthly.

The supplied Low End criteria weight price at **53%**, age at **24%**, positioning at **16%** and reliability at **7%**. High End weights positioning at **43%**, age at **29%**, reliability at **19%** and price at **9%**. These percentages describe customer scoring priorities—not guaranteed sales shares or the percentage change in sales caused by a price change.

The report labels growth rates as **beginning rates** and instructs students to check the current Courier for the upcoming year. Its price ranges are **Round 0** ranges; the guide specifies a $0.50 annual decrease. Always identify the round before using a number.

## Saving decisions as a team

Your working changes are a rough draft until you officially save them. The supplied Capstone saving guide recommends saving **by department** when working in teams, to avoid overwriting another member’s work. Coordinate who owns each department, review teammates’ saves, and use **Load Last Decision File** to bring the appropriate saved decisions into your view. Check the **Decision Summary** to confirm the saved record. A forecast or a good calculation does not, by itself, save a decision.

## Sources and scope

- [Capsim, Capstone 2.0 Team Member Guide](https://ww3.capsim.com/modules/GIA/files/1_0/0/CapsimPlatform/EN/PDF/Capstone_User_Guide_v4.pdf): Industry Conditions Report; R&D; Marketing; Production; Finance; and financial statements. Consult especially the guide’s numbered pages 2, 7–12 and 28–29. Accessed September 15, 2026.
- Archived class Courier Excel export: financial statement labels and ratio conventions cross-checked for this guide. No student identities or team results are published here.
- The examples are original, simplified teaching material. The instructor supplied an Industry Conditions Report on September 15, 2026. Its buying-criteria tables describe Round 0 and its growth rates are starting rates, not permanent forecasts. Check your own industry’s current Courier each round; this companion does not assume both class sections have identical settings.

[Other Writing](/other-writing/) · [For Students](/for-students/)

</div>
<script>
(function(){
 const input=document.getElementById('cap-search');
 const terms=Array.from(document.querySelectorAll('.cap-term'));
 const groups=Array.from(document.querySelectorAll('.cap-group'));
 function filter(){
  const query=input.value.trim().toLowerCase();let count=0;
  terms.forEach(t=>{const show=t.textContent.toLowerCase().includes(query);t.hidden=!show;t.style.display=show?'':'none';if(show)count++;});
  groups.forEach(g=>{g.style.display=Array.from(g.querySelectorAll('.cap-term')).some(t=>!t.hidden)?'':'none';});
  document.getElementById('cap-count').textContent=count+' of '+terms.length+' terms shown';
 }
 input.addEventListener('input',filter);filter();
})();
</script>
