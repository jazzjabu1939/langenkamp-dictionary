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
@media print {.cap-group{display:block!important;} .page-header,.return-bar,.site-footer,.cap-search {display:none!important;} .cap-term{display:block!important;} .capstone-guide h2 {break-after:avoid;}}
</style>
<div class="capstone-guide" markdown="1">

# Capstone 2.0 Glossary & Guidance

*Matthew D. Langenkamp · Isenberg School of Management, UMass Amherst*  
*Prepared in collaboration with Thea · Updated September 15, 2026*

<div class="cap-intro" markdown="1">
This guide defines the financial and operating terms used in Capstone 2.0. It includes formulas, examples and instructions for reading the Courier.

This is an independent teaching guide. For simulation rules and industry-specific figures, consult Capsim’s guides, your Industry Conditions Report and the current Courier.
</div>

## Basic calculations

1. **Sales:** price × units sold.
2. **Contribution:** sales − variable costs; divide by sales for the percentage.
3. **Depreciation:** allocate asset cost over its accounting life; distinguish expense from payment.
4. **Net profit:** subtract period costs from contribution to find EBIT; then subtract interest, taxes and profit sharing.
5. **Financial position:** assets = liabilities + equity.
6. **Cash:** reconcile operating, investing and financing flows.
7. **Performance:** ROS, asset turnover, ROA, leverage and ROE.
8. **Planned production:** forecast sales + desired ending inventory − beginning inventory. Check the result against capacity.

**For class:** [Download the financial foundations exercise (PDF)](/assets/capstone/Capstone-Financial-Foundations.pdf). Work individually. The figures are hypothetical. Your instructor will specify the deadline and submission method.

## Example: from sales to net profit

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

Contribution margin is **44.67%** of sales. After the remaining expenses, net profit is **11.67%** of sales. The cash-flow statement is needed to explain the change in cash. All figures in this example are hypothetical.

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

The industry report for a completed round. It lists company results, product data, customer buying criteria and market share.

</article>

<article class="cap-term" id="industry-conditions-report" markdown="1">

### Industry Conditions Report

A report of the industry’s starting conditions, including customer buying criteria, segment positions and growth rates. Use the report for your assigned industry.

</article>

<article class="cap-term" id="annual-report" markdown="1">

### Annual report

A company’s financial statements for a completed year.

</article>

<article class="cap-term" id="pro-forma-statements" markdown="1">

### Pro forma statements

Financial statements that project the results of proposed decisions and sales forecasts. Actual results may differ from these projections.

</article>

<article class="cap-term" id="round-and-reporting-date" markdown="1">

### Round and reporting date

A round is one simulated year. At the start of Round 2, the Courier reports Round 1 results. Check whether a figure describes a completed round or a forecast.

</article>

<article class="cap-term" id="units-and-dollar-scaling" markdown="1">

### Units and dollar scaling

The scale in which a report states its figures. Dollars and unit quantities may be reported in thousands, while prices remain dollars per unit. For example, 1,000 thousand units sold at $30 produce $30,000 thousand in revenue ($30 million). Read the labels on each table.

</article>

</section>

<section class="cap-group" markdown="1">

## Sales, costs and profit

<article class="cap-term" id="revenue-sales" markdown="1">

### Revenue / sales

The value of products sold during a period. **Sales = price × units sold** for a product sold at one price. Company sales equal the sum of product sales. Unsold products remain in inventory; credit sales remain in accounts receivable until collected.

</article>

<article class="cap-term" id="units-sold" markdown="1">

### Units sold

The number of products purchased by customers during a period. This may differ from the number produced or forecast to sell.

</article>

<article class="cap-term" id="price" markdown="1">

### Price

The amount charged for one unit. Price affects both revenue per unit and customer demand.

</article>

<article class="cap-term" id="material-cost" markdown="1">

### Material cost

The cost of materials in a product. Positioning and reliability affect this cost. The income statement records material costs for units sold; material costs for unsold units remain in inventory.

</article>

<article class="cap-term" id="labor-cost" markdown="1">

### Labor cost

The cost of production labor. Automation reduces labor requirements. Capstone charges 50% more for second-shift labor than for first-shift labor. This premium applies to labor, not to the product’s total cost.

</article>

<article class="cap-term" id="variable-costs" markdown="1">

### Variable costs

Costs that vary with activity. Capstone groups material, labor and inventory carrying costs under variable costs in its income statement.

</article>

<article class="cap-term" id="cost-of-goods-sold-cogs" markdown="1">

### Cost of goods sold (COGS)

The cost of products sold during a period. Production costs for unsold goods remain in inventory. Use the material, labor and carrying-cost lines shown in the Capstone report when calculating contribution margin.

</article>

<article class="cap-term" id="inventory-carrying-cost" markdown="1">

### Inventory carrying cost

The expense of holding unsold products. Capstone’s guide specifies a 12% carrying-cost rate. Use the reported charge to reconcile the income statement. The inventory asset is recorded at cost; carrying expense is a separate charge.

</article>

<article class="cap-term" id="unit-contribution" markdown="1">

### Unit contribution

The amount each unit contributes toward period costs and profit. **Unit contribution = price − variable cost per unit**. A $30 price less $16 in material and labor costs leaves $14 before carrying costs and other expenses.

</article>

<article class="cap-term" id="contribution-margin-dollars" markdown="1">

### Contribution margin — dollars

Sales remaining after variable costs. **Contribution margin = sales − total variable costs**. Sales of $30 million less variable costs of $16.6 million leave $13.4 million to cover period costs and profit.

</article>

<article class="cap-term" id="contribution-margin-percentage" markdown="1">

### Contribution margin — percentage

Contribution margin expressed as a share of sales. **Contribution margin percentage = contribution margin dollars ÷ sales × 100**. A contribution of $13.4 million on sales of $30 million gives 44.67%.

</article>

<article class="cap-term" id="fixed-costs-period-costs" markdown="1">

### Fixed costs / period costs

Period costs are expenses charged to the period rather than to individual units sold. Capstone includes depreciation and SG&A. Fixed costs do not vary directly with unit sales within a given operating range, though managers may change their budgets.

</article>

<article class="cap-term" id="sg-a" markdown="1">

### SG&A

Selling, general and administrative expenses. Capstone includes R&D, promotion, sales and administration. **SG&A-to-sales = SG&A ÷ sales**; multiply by 100 to express the ratio as a percentage. Deduct either the total or its components, not both.

</article>

<article class="cap-term" id="r-d-expense" markdown="1">

### R&D expense

The expense of developing or revising a product. It is separate from investment in production equipment.

</article>

<article class="cap-term" id="depreciation" markdown="1">

### Depreciation

The allocation of an asset’s depreciable cost over its useful life. **Straight-line depreciation = (cost − residual value) ÷ useful life**. Capstone uses a 15-year straight-line life. A $30 million asset with no residual value incurs $2 million of depreciation for a full year. Depreciation reduces reported profit without a current cash payment.

</article>

<article class="cap-term" id="accumulated-depreciation-net-plant" markdown="1">

### Accumulated depreciation / net plant

Accumulated depreciation is the total depreciation recorded on an asset. **Net plant = gross plant and equipment − accumulated depreciation**. If the report shows accumulated depreciation as a negative number, add that signed amount. Net plant is a book value, not an estimate of resale value.

</article>

<article class="cap-term" id="net-margin-capstone-product-view" markdown="1">

### Net margin — Capstone product view

Product contribution less product period costs, as defined in Capstone’s product analysis. This dollar amount is not company net profit. Company expenses, interest, taxes and profit sharing may still need to be deducted.

</article>

<article class="cap-term" id="ebit-operating-result" markdown="1">

### EBIT / operating result

Earnings before interest and taxes. In Capstone’s income statement, **EBIT = contribution margin − depreciation − SG&A − other operating expenses**. Follow the signs of any adjustments shown in the report.

</article>

<article class="cap-term" id="interest-expense" markdown="1">

### Interest expense

The expense of borrowing money. Interest reduces profit. Repayment of loan principal reduces cash and debt but is not an expense.

</article>

<article class="cap-term" id="taxes-and-profit-sharing" markdown="1">

### Taxes and profit sharing

Deductions from earnings shown after interest on Capstone’s income statement. Use the amounts and rates specified in your simulation.

</article>

<article class="cap-term" id="net-profit-net-income" markdown="1">

### Net profit / net income

Earnings after expenses. **Net profit = EBIT − interest − taxes − profit sharing**, with any additional adjustments shown in the report. Net profit differs from cash flow because some income and expenses do not involve cash in the same period.

</article>

<article class="cap-term" id="cumulative-profit" markdown="1">

### Cumulative profit

The sum of net profits for the rounds included in a report. Retained earnings may differ because they also reflect opening balances and dividends.

</article>

<article class="cap-term" id="break-even-volume" markdown="1">

### Break-even volume

The sales volume at which revenue equals the costs included in the calculation. **Break-even units = fixed costs ÷ unit contribution**. This formula assumes a positive, constant unit contribution and constant fixed costs. Changes in price, unit costs or capacity require a new calculation.

</article>

</section>

<section class="cap-group" markdown="1">

## Assets, financing and cash

<article class="cap-term" id="balance-sheet" markdown="1">

### Balance sheet

A statement of assets, liabilities and owners’ equity at a particular date. **Assets = liabilities + shareholders’ equity**.

</article>

<article class="cap-term" id="cash" markdown="1">

### Cash

Money held by the company. **Ending cash = beginning cash + operating cash flow + investing cash flow + financing cash flow**.

</article>

<article class="cap-term" id="accounts-receivable-a-r" markdown="1">

### Accounts receivable (A/R)

Amounts customers owe for credit sales. An increase in receivables reduces operating cash flow relative to reported profit. Longer payment terms delay collection and can affect customer demand.

</article>

<article class="cap-term" id="inventory" markdown="1">

### Inventory

Unsold products recorded as an asset at cost. Without write-offs, **ending inventory units = beginning units + units produced − units sold**. Producing inventory uses cash before the goods are sold.

</article>

<article class="cap-term" id="current-assets" markdown="1">

### Current assets

Assets expected to be used or converted into cash within a year. In Capstone, these generally comprise cash, accounts receivable and inventory.

</article>

<article class="cap-term" id="plant-and-equipment-capacity-investment" markdown="1">

### Plant and equipment / capacity investment

Long-lived assets used in production. Purchases of capacity and automation are investments. Their cost is recorded as an asset and expensed over time through depreciation.

</article>

<article class="cap-term" id="accounts-payable-a-p" markdown="1">

### Accounts payable (A/P)

Amounts owed to suppliers. An increase in payables postpones cash payments and increases operating cash flow relative to reported profit.

</article>

<article class="cap-term" id="current-debt" markdown="1">

### Current debt

Short-term borrowing. New borrowing increases cash and liabilities. Check Finance for repayment dates and refinancing requirements.

</article>

<article class="cap-term" id="long-term-debt-bonds" markdown="1">

### Long-term debt / bonds

Borrowing due beyond the current year. A bond’s face value is its principal, its coupon determines interest payments, and its maturity is the repayment date. Market yield may differ from the coupon rate. Capstone sets limits and charges for borrowing and early repayment.

</article>

<article class="cap-term" id="emergency-loan" markdown="1">

### Emergency loan

An automatic loan issued when a company cannot meet its cash needs under the simulation’s rules. It adds financing costs. Common causes include excess inventory, weak collections, unfunded investment and debt repayments.

</article>

<article class="cap-term" id="common-stock-shares-issued" markdown="1">

### Common stock / shares issued

Capital contributed by shareholders. Issuing shares increases cash and equity, not revenue. The common-stock account records contributed capital, not current market value. Additional shares may reduce earnings per share.

</article>

<article class="cap-term" id="retained-earnings" markdown="1">

### Retained earnings

Earnings kept in the business rather than paid as dividends. **Ending retained earnings = beginning retained earnings + net profit − dividends**, absent other adjustments. Retained earnings are part of equity, not a separate cash account.

</article>

<article class="cap-term" id="equity" markdown="1">

### Equity

The owners’ book interest in the company. **Equity = assets − liabilities**. Equity is negative when liabilities exceed recorded assets.

</article>

<article class="cap-term" id="dividends-share-repurchases" markdown="1">

### Dividends / share repurchases

Payments to shareholders. Dividends reduce cash and retained earnings. Share repurchases reduce cash, equity and shares outstanding. Both are financing transactions rather than operating expenses.

</article>

<article class="cap-term" id="working-capital-current-ratio" markdown="1">

### Working capital / current ratio

Net working capital is the excess of current assets over current liabilities. **Net working capital = current assets − current liabilities**. The **current ratio = current assets ÷ current liabilities**. Both measure short-term financial position, but neither shows how quickly receivables and inventory can become cash.

</article>

<article class="cap-term" id="cash-flow-from-operations-cfo" markdown="1">

### Cash flow from operations (CFO)

Cash generated or used by ordinary business operations. A simplified calculation is **net profit + depreciation − increase in receivables − increase in inventory + increase in payables**. Include other adjustments shown in the report. Depreciation is added back because it reduced profit without a current cash payment.

</article>

<article class="cap-term" id="investing-cash-flow-capital-expenditure" markdown="1">

### Investing cash flow / capital expenditure

Cash spent on or received from long-lived assets. Capital expenditure, such as a plant purchase, is an investing cash outflow. Depreciation records the asset’s expense over time rather than its purchase payment.

</article>

<article class="cap-term" id="financing-cash-flow" markdown="1">

### Financing cash flow

Cash received from borrowing and share issues, less principal repayments, dividends and share repurchases.

</article>

<article class="cap-term" id="free-cash-flow" markdown="1">

### Free cash flow

Operating cash flow remaining after capital expenditure. **Free cash flow = operating cash flow − capital expenditures** under the definition used here. This is a supplementary measure, not necessarily a separate Courier line. A negative amount indicates a funding requirement.

</article>

</section>

<section class="cap-group" markdown="1">

## Courier ratios and performance

<article class="cap-term" id="return-on-sales-ros" markdown="1">

### Return on sales (ROS)

Net profit as a percentage of sales. **ROS = net profit ÷ sales × 100**. Also called net profit margin. Use company net profit, not EBIT or Capstone’s product net margin.

</article>

<article class="cap-term" id="asset-turnover" markdown="1">

### Asset turnover

Sales generated per dollar of assets. **Asset turnover = sales ÷ total assets**, expressed as times. The Courier checked for this guide uses year-end assets; some accounting texts use average assets.

</article>

<article class="cap-term" id="return-on-assets-roa" markdown="1">

### Return on assets (ROA)

Net profit as a percentage of assets. **ROA = net profit ÷ total assets × 100** under the Courier convention used here. With consistent figures, ROS multiplied by asset turnover equals ROA.

</article>

<article class="cap-term" id="leverage-courier" markdown="1">

### Leverage — Courier

The ratio of assets to equity, also called the equity multiplier. **Leverage = total assets ÷ total equity**. Assets of $35 million and equity of $15 million give leverage of 2.33 times. This is not the debt-to-equity ratio.

</article>

<article class="cap-term" id="return-on-equity-roe" markdown="1">

### Return on equity (ROE)

Net profit as a percentage of equity. **ROE = net profit ÷ equity × 100**. With consistent figures, **ROE = ROS × asset turnover × leverage**. Very small or negative equity can make this ratio misleading; a loss divided by negative equity produces a positive ratio.

</article>

<article class="cap-term" id="earnings-per-share-eps" markdown="1">

### Earnings per share (EPS)

Net profit attributable to each share. **EPS = net profit ÷ the applicable number of shares**. Use consistent dollar and share units and Capstone’s share-count convention.

</article>

<article class="cap-term" id="stock-price-market-capitalization" markdown="1">

### Stock price / market capitalization

Stock price is the simulated market value of one share. **Market capitalization = stock price × shares outstanding**. Market capitalization differs from book equity on the balance sheet.

</article>

<article class="cap-term" id="market-share-actual-and-potential" markdown="1">

### Market share — actual and potential

Actual market share is the proportion of sales a product or company captures. Potential share estimates the share it could have captured under the report’s assumptions about availability. Stockouts can cause the two to differ. Check whether the report measures share by units or revenue and by segment or industry.

</article>

<article class="cap-term" id="balanced-scorecard-scoring" markdown="1">

### Balanced Scorecard / scoring

A set of measures used to assess company performance. Capstone groups them into financial results, internal business processes, customers, and learning and growth. Check your course’s measures, weights and targets.

</article>

</section>

<section class="cap-group" markdown="1">

## Decision terms you will meet next

<article class="cap-term" id="sales-forecast" markdown="1">

### Sales forecast

An estimate of the units customers will buy. The forecast informs production plans and pro forma statements. Compare expected results with a lower-sales scenario.

</article>

<article class="cap-term" id="production-schedule" markdown="1">

### Production schedule

The number of units planned for production. **Planned production = forecast sales + desired ending inventory − beginning inventory**, subject to capacity and timing constraints.

</article>

<article class="cap-term" id="capacity-plant-utilization" markdown="1">

### Capacity / plant utilization

Capacity is the number of units a production line can make in a year on one shift. Capstone allows a second shift, up to twice first-shift capacity. **Utilization = production ÷ first-shift capacity × 100**, subject to the report’s adjustments. Utilization above 100% indicates second-shift use. Purchased capacity becomes available next round.

</article>

<article class="cap-term" id="automation" markdown="1">

### Automation

Equipment investment that reduces labor requirements per unit. Higher automation can lengthen R&D repositioning projects. Changes become available the following year.

</article>

<article class="cap-term" id="positioning-perceptual-map" markdown="1">

### Positioning / perceptual map

Positioning describes a product’s performance and size. The perceptual map plots these attributes against segment preferences, which move over time. Customers prefer products suited to their segment rather than the smallest or fastest product in every case.

</article>

<article class="cap-term" id="age-revision-date" markdown="1">

### Age / revision date

Perceived age is the time since introduction, adjusted for redesign. A repositioning project halves perceived age when completed; the product then continues to age. An MTBF-only change does not halve age. The revision date is the date the change takes effect.

</article>

<article class="cap-term" id="mtbf-reliability" markdown="1">

### MTBF / reliability

Mean Time Before Failure, a reliability rating measured in hours. Raising MTBF within a segment’s preferred range can improve its customer score but increases material cost. Reliability above the preferred range provides no further scoring benefit.

</article>

<article class="cap-term" id="promotion-awareness" markdown="1">

### Promotion / awareness

Promotion is spending intended to make customers aware of a product. Awareness is the percentage of customers who know it. Awareness declines without support, and additional spending produces diminishing gains.

</article>

<article class="cap-term" id="sales-budget-accessibility" markdown="1">

### Sales budget / accessibility

The sales budget funds sales and distribution. Accessibility measures how readily customers in a segment can buy from the company. It differs from awareness, which measures whether customers know the product.

</article>

<article class="cap-term" id="customer-buying-criteria-survey-score" markdown="1">

### Customer buying criteria / survey score

Buying criteria are price, age, reliability and positioning, weighted by segment. The customer survey score measures how well a product meets customer preferences and also reflects awareness, accessibility and credit terms. A 53% price weight is a scoring weight, not a forecast of market share or price sensitivity.

</article>

<article class="cap-term" id="segment-demand-growth" markdown="1">

### Segment demand / growth

The number of units customers in a segment demand. **Next-year demand = current demand × (1 + growth rate)**. Check the current Courier for the upcoming growth rate. Company sales also depend on market share and product availability.

</article>

<article class="cap-term" id="cost-leadership-differentiation" markdown="1">

### Cost leadership / differentiation

Cost leadership is competition based on lower costs while meeting customer requirements. Differentiation is competition based on attributes customers value enough to support a price premium. Each requires coordinated product, marketing, production and financial decisions.

</article>

<article class="cap-term" id="optional-modules-hr-tqm-and-sustainability" markdown="1">

### Optional modules: HR, TQM and sustainability

Additional decisions available when the instructor enables Human Resources or TQM/Sustainability. Consult your course settings for their start dates and rules.

</article>

<article class="cap-term" id="tqm-investments-and-diminishing-returns" markdown="1">

### TQM investments and diminishing returns

TQM investments can reduce material, labor and administrative costs, shorten R&D projects, or increase demand. Benefits begin in the year of investment and continue in later years. Complementary initiatives can support the same objective. Repeated investment eventually produces smaller gains or none. Check Projected Cumulative Impacts; the stated maximums are cumulative limits, not annual gains.

</article>

</section>


## Before submitting decisions

- Check the units and round on the report.
- Explain changes in sales, contribution and net profit separately.
- Reconcile ending cash; inspect inventory and debt repayments.
- Check whether a lower-sales forecast leaves enough cash to meet obligations.
- Confirm R&D completion dates and next-round availability of plant changes.
- Record the assumptions behind your forecast.

## Reading the supplied Industry Conditions Report

The **ideal spot** is the position customers prefer. Calculate it by adding the segment’s offset to its center. For example, the supplied High End Round 0 center is performance 7.5 / size 12.5. Its offset is +1.4 / −1.4, giving an ideal spot of **8.9 / 11.1**. Positions drift monthly.

The supplied Low End criteria weight price at **53%**, age at **24%**, positioning at **16%** and reliability at **7%**. High End weights positioning at **43%**, age at **29%**, reliability at **19%** and price at **9%**. These percentages are scoring weights. They do not measure market share or the change in demand caused by a price change.

The report labels growth rates as **beginning rates** and instructs students to check the current Courier for the upcoming year. Its price ranges are **Round 0** ranges; the guide specifies a $0.50 annual decrease. Always identify the round before using a number.

## Saving decisions as a team

Changes remain in your rough draft until you save them to the team decision file. Assign responsibility for each department and save **by department** to avoid overwriting a teammate’s work. Use **Load Last Decision File** to load saved team decisions. Check the **Decision Summary** to confirm who saved each department and when.

## Sources and scope

- [Capsim, Capstone 2.0 Team Member Guide](https://ww3.capsim.com/modules/GIA/files/1_0/0/CapsimPlatform/EN/PDF/Capstone_User_Guide_v4.pdf): Industry Conditions Report; R&D; Marketing; Production; Finance; and financial statements. Consult especially the guide’s numbered pages 2, 7–12 and 28–29. Accessed September 15, 2026.
- Archived class Courier Excel export: financial statement labels and ratio conventions cross-checked for this guide.
- Industry Conditions Report supplied September 15, 2026: Round 0 buying criteria, segment positions and initial growth rates. Consult the current Courier for subsequent rounds.

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
