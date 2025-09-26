# Module 3: Anomaly Detection and Smart Insights

Detect unusual patterns and generate automatic explanations.

## Exercise 3.1: Software Revenue Analysis
1. Navigate to the **Anomaly Detection** page
2. Filter by **Low, Spencer** in the Software category
3. Review the dynamic text summary

![Smart Insights](https://github.com/alipouw13/ai-powerbi/blob/main/images/smart-insights-1.png)

## Exercise 3.2: 90-Day Revenue Trends
1. Add a slicer for date hierarchy to the page - make it a dropdown slicer with Year, Quarter, Month
1. Select Q1 and Q2 2021
2. Review updated Revenue Summaries
3. Right click on the "Revenue won by date and region" where there is a spike in revnue > Analyze, Explain increase
4. Analyze possible explanations

![Analyze](https://github.com/alipouw13/ai-powerbi/blob/main/images/analyze.png)

5. Remove the Region field from the line chart
6. Go to insights tab and turn on "Anomalies"
7. Make sure sensitivity is set to 70% - add field to the 'Explain by" section to restrict analysis to specific fields

![Anomalies](https://github.com/alipouw13/ai-powerbi/blob/main/images/anomalies.png)

## Exercise 3.3: Natural Language Queries
1. Use the **Ask a question** feature
2. Try these queries:
   - "close %"
   - "close percent"

3. Notice the difference. Now click "add synonyms now" or go to Modeling > Q&A setup > Synonyms. Find the opportunities table and add "cloce percent" to the close % column and exit out.

![Synonyms Q&A](https://github.com/alipouw13/ai-powerbi/blob/main/images/synonyms-qna.png)

4. Now try the following queries again and notice they should give the same output:
   - "close %"
   - "close percent"
5. Proceed with the following queries and feel free to add all or some of the visuals displayed:
   - "close % by month"
   - "close % by month in a line chart"
   - "close % by month in a line chart by manager"

![Q&A](https://github.com/alipouw13/ai-powerbi/blob/main/images/close-pct.png)