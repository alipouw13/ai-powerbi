# Power BI AI Workshop: Contoso Sales Intelligence

Welcome to the Power BI AI Workshop! This hands-on workshop will guide you through creating intelligent reports using Power BI's artificial intelligence capabilities. You'll explore the Contoso Sales sample dataset and learn to build various AI-powered visualizations.

## Workshop Objectives

By the end of this workshop, you will be able to:
- Use and understand the value of Power BI's built-in AI visuals (Key Influencers, Decomposition Tree, Anomaly Detection)
- Create intelligent reports using Copilot in Power BI Desktop
- Build interactive dashboards with AI-driven insights
- Apply natural language queries to extract business insights
- Use CoPilot in Power BI Service to extract key business insights

## Prerequisites

- Power BI Desktop (latest version)
- Basic understanding of Power BI concepts
- Access to Power BI Service (Fabric free license minimum)
- No prior AI/ML knowledge required

## Getting Started

### Step 1: Get the Artificial Intelligence Sample

1. Open the Power BI service (`app.powerbi.com`)
2. Select **Learn** in the navigation pane
3. Under **Sample reports**, find and select **Artificial Intelligence Sample**
4. Power BI saves the report and dataset to your **My workspace**

### Step 2: Download the Sample for Desktop Work

1. Open the report in Power BI service
2. Go to **File** > **Download this file**
3. Select **A copy of your report and data (.pbix)**
4. Save to your desired location and open in Power BI Desktop

## Workshop Modules

### Module 1: Exploring Key Influencers

Learn to identify what factors most influence your business outcomes.

#### Exercise 1.1: Analyzing Win/Loss Factors
1. Navigate to the **Key Influencers** page
2. Explore top contributors for **Status = Won**
   - Notice the discount impact (2.76x more likely to win when discount goes up 2%)
   - Click the **2.76x** indicator to see the scatter plot correlation
3. Filter by **Furniture** category to see new insights
4. Switch to **Status = Lost** to understand loss factors

#### Exercise 1.2: Interactive Analysis
1. Use the **Close % by Product category** chart to filter data
2. Observe how Key Influencers updates dynamically
3. Identify the top sales owner for furniture wins

### Module 2: Root Cause Analysis with Decomposition Tree
**Duration: 25 minutes**

Discover the path to your highest value opportunities.

#### Exercise 2.1: Computer Sales Analysis
1. Open the **Decomposition Tree** page
2. Select **Computers** in the Category breakdown
3. Use AI splits to find the next highest opportunity path
4. Follow the path: Tablets → High value → Territory → US-SOUTH
5. Identify the top sales owner in this segment

#### Exercise 2.2: Building Your Own Decomposition
1. Start with a different category (e.g., Software)
2. Use the **High value** AI split option
3. Continue drilling down to find insights

### Module 3: Anomaly Detection and Smart Insights

Detect unusual patterns and generate automatic explanations.

#### Exercise 3.1: Software Revenue Analysis
1. Navigate to the **Anomaly Detection** page
2. Filter by **Low, Spencer** in the Software category
3. Review the dynamic text summary
4. Right-click December 2020 data point
5. Select **Analyze** > **Explain the decrease**

#### Exercise 3.2: 90-Day Revenue Trends
1. Click **Last 90 days** filter
2. Review updated Revenue Summary
3. Click the April 25th anomaly indicator
4. Analyze possible explanations and strength scores

#### Exercise 3.3: Natural Language Queries
1. Use the **Ask a question** feature
2. Try these queries:
   - "close %"
   - "close % by month"
   - "close % by month in a line chart"
   - "close % by month in a line chart by manager"

### Modeule 4: Visual calculation, verified answers, and smart narrative

Get more and enhanced insights from your data.

#### Exercise 4.1: Set up a verified answer
1. Right click on the pie chart
2. Select "Set up a verified answer"
3. Use CoPilot suggestions or add the following to the verified answers:
    a. What are the revenue goals for each sales owner?
    b. Who are the sales owners with won opportunities?
    c. What are the revenue goals for each sales manager?
    d. Which sales owners have the highest revenue goals?
4. Close the prep data for AI tab

#### Exercise 4.3: Set up smart narrative
1. Click on "CoPilot (preview)" on the narrative tile
2. Click on the tile again to edit what you want CoPilot to summarize
3. Validate the scope of your narrative
4. Click update

#### Exercise 4.4: Create a visual calculation
1. Richt click on the table
2. Click New visual calculation > Percent of grand  total
3. Select Rev Goal1 as 'Field'
4. Select Rows as 'Axis'
5. Click the green check mark
6. Click back to report to see your new column

### Module 5: Create a python visual

Use the following script to creaste a python visual. Make sure you have the following prerequisites before attempting to create:

```

```


## Advanced Exercises with Copilot

### Module 6: Create DAX queries with CoPilot

Leverage copilot to create DAX queries.

1. Go to DAX in the left pane
2. Use the following CoPilot prompt to discover new DAX measures: _"Suggest measures to calculate revenue forcasts from the Opportunities table and existing measures."_

### Module 7: Creating New Pages with Copilot

Use Copilot in Power BI Desktop to create additional analytical pages.

#### Exercise 7.1: Customer Segmentation Analysis Page
**Goal**: Create a page analyzing customer segments and their revenue contribution.

**Instructions**:
1. Create a new report page named "Customer Segmentation"
2. Use Copilot prompt: *"Create a customer segmentation analysis showing revenue by customer type, geographic distribution, and purchasing patterns"*
3. Expected visuals:
   - Treemap showing revenue by customer segment
   - Map visual showing geographic distribution
   - Clustered bar chart of top customers by revenue
   - KPI cards for key metrics

**Copilot Prompts to Try**:
- "Show me the top 10 customers by revenue"
- "Create a map showing sales by territory"
- "Add a slicer for product category"
- "Show customer lifetime value analysis"

#### Exercise 7.2: Product Performance Dashboard
**Goal**: Build a comprehensive product analysis page.

**Instructions**:
1. Create a new page named "Product Performance"
2. Use Copilot prompt: *"Create a product performance dashboard showing sales trends, profitability, and market share by product category"*
3. Expected visuals:
   - Line chart showing sales trends over time
   - Waterfall chart showing profit breakdown
   - Donut chart showing market share
   - Table with product rankings

**Copilot Prompts to Try**:
- "Show product sales trends for the last 12 months"
- "Create a profitability analysis by product"
- "Add filters for date range and territory"
- "Show seasonal patterns in product sales"

#### Exercise 7.3: Sales Rep Performance Page
**Goal**: Analyze individual sales representative performance.

**Instructions**:
1. Create a new page named "Sales Rep Analytics"
2. Use Copilot prompt: *"Create a sales rep performance analysis showing individual achievements, quota attainment, and pipeline health"*
3. Expected visuals:
   - Gauge charts for quota attainment
   - Clustered column chart comparing rep performance
   - Funnel chart showing sales pipeline
   - Scatter plot of deals won vs. average deal size

**Copilot Prompts to Try**:
- "Show quota attainment by sales rep"
- "Create pipeline analysis by stage"
- "Add performance rankings"
- "Show win rate by sales representative"

### Module 8: Advanced AI Visuals

Create sophisticated AI-powered visualizations.

#### Exercise 8.1: Predictive Analytics Page
**Goal**: Build forecasting and predictive insights.

**Instructions**:
1. Create a new page named "Predictive Insights"
2. Add these AI visuals:

**A. Revenue Forecasting**
- Create a line chart with revenue by month
- Enable forecasting (Analytics pane > Forecast > On)
- Set forecast length to 6 months
- Configure confidence interval to 95%

**B. Trend Analysis**
- Add a trend line to sales data
- Use Analytics pane > Trend line
- Interpret the trend direction and strength

**C. Smart Narrative**
- Add a Smart narrative visual
- Configure to summarize key trends
- Customize the narrative focus

**Copilot Prompts for This Page**:
- "Forecast revenue for the next 6 months"
- "Show trend analysis for key metrics"
- "Create a summary of performance insights"

#### Exercise 8.2: Correlation and Pattern Analysis
**Goal**: Discover hidden relationships in data.

**Instructions**:
1. Create a new page named "Data Insights"
2. Build these analytical visuals:

**A. Correlation Matrix**
- Create scatter plots showing relationships between:
  - Discount % vs. Win Rate
  - Deal Size vs. Sales Cycle Length
  - Territory vs. Product Category Performance

**B. Outlier Detection**
- Use box plots to identify outliers in:
  - Deal values by category
  - Sales cycle duration
  - Rep performance metrics

**C. Clustering Analysis**
- Create scatter plots with clustering
- Group customers by behavior patterns
- Identify distinct market segments

#### Exercise 8.3: Executive Summary Page
**Goal**: Create a high-level executive dashboard.

**Instructions**:
1. Create a new page named "Executive Summary"
2. Use Copilot prompt: *"Create an executive summary dashboard with KPIs, trends, and key insights for leadership review"*

**Key Components**:
- KPI cards for critical metrics
- Trend sparklines
- Key Influencers summary
- Anomaly alerts
- Performance indicators

**Copilot Prompts**:
- "Show key performance indicators"
- "Create trend summary for executives"
- "Add alerts for unusual patterns"
- "Show year-over-year comparisons"

### Module 9: CoPilot for Business users

Gain business insights from your data.

1. Publish the report to your workspace. 
2. Ensure CoPilot is enabled on your workspace.
3. Go to Power BI service and open your newly published report
4. Ask one of the CoPilot questions defined below in the CoPilot pane on the report

**CoPilot Questions**
1. What are the main drivers of revenue in my opportunities pipeline?
2. How does opportunity win rate vary by sales owner, product, or campaign?
3. Which products or campaigns are associated with the highest value opportunities?
4. What is the average time to close an opportunity, and how does it differ by owner or product?
5. Are there any patterns in lost opportunities—such as common reasons, products, or customer segments?
6. How does customer satisfaction (CSAT) relate to agent performance or case topics?
7. What is the distribution of opportunities across different industries or account sizes?
8. How effective are our campaigns in generating high-quality opportunities?
9. Which accounts or contacts are most engaged, and how does this impact opportunity outcomes?
10. Are there any trends in SLA compliance or escalations for customer cases?

## Creative Challenges

### Challenge 1: Market Opportunity Analysis
Create a page that identifies untapped market opportunities using AI insights.

### Challenge 2: Risk Assessment Dashboard
Build a risk monitoring dashboard using anomaly detection and key influencers.

### Challenge 3: Competitive Analysis
Design a competitive positioning analysis using decomposition trees and smart narratives.

## Additional Resources

- [Power BI AI Visuals Documentation](https://learn.microsoft.com/en-us/power-bi/visuals/)
- [Key Influencers Visual Guide](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-influencers)
- [Decomposition Tree Documentation](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-decomposition-tree)
- [Anomaly Detection in Power BI](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-anomaly-detection)
- [Smart Narratives Guide](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-smart-narrative)

## Workshop Completion

Congratulations! You've completed the Power BI AI Workshop. You should now have:
- A comprehensive understanding of Power BI AI visuals
- Hands-on experience with Copilot in Power BI Desktop
- Multiple report pages showcasing different AI capabilities
- Skills to apply AI insights to real business scenarios

## Next Steps

1. Apply these techniques to your own datasets
2. Explore advanced AI features in Power BI Premium
3. Share your AI-powered reports with stakeholders
4. Continue learning with Microsoft Learn modules on Power BI AI

---

**Workshop Duration**: Approximately 3 hours  
**Skill Level**: Beginner to Intermediate  
**Last Updated**: September 2025

For questions or feedback, please refer to the official Microsoft documentation or Power BI community forums.