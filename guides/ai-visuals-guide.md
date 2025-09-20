# Power BI AI Visuals Guide

## Overview

This guide provides comprehensive instructions for using Power BI's AI-powered visuals to analyze Contoso Sales data. These visuals use machine learning to automatically discover insights and patterns in your data.

## 1. Key Influencers Visual

### Purpose
The Key Influencers visual helps you understand what drives a metric up or down. It's perfect for analyzing factors that influence claim amounts, severity, or processing flags.

### Best Practices:
- Use categorical fields with reasonable cardinality (< 100 unique values) in the 'Analyze' section of the visual
- Include both continuous and categorical variables
- Filter out extreme outliers for clearer patterns
- Use the "What if" feature to simulate scenarios

## 2. Decomposition Tree Visual

### Purpose
The Decomposition Tree allows you to drill down through multiple dimensions to understand how your data breaks down across different categories.

## 3. Q&A Visual

### Purpose
Natural language querying of your insurance data using conversational questions.

### Optimization Tips:
- Train the Q&A with common business terms - add synonyms for column names
- Create measures with business-friendly names
- Use consistent naming conventions
- Describe relationships that are not obvious from table mappings - add field descriptions for better recognition
- Exclude tables or columns you don’t wish to use 
- Test out common expected questions in Teach Q&A to identify gaps


## 4. Narrative Visual

### Purpose
Automatically generates narrative insights about your data in natural language.

### Configuration:
- Ensure you have populated visuals on the Location page with data you want insights on

### What It Provides:
- Automatic insights about trends
- Comparisons between segments
- Outlier identification
- Performance summaries

## 5. Anomaly Detection

### Purpose
Automatically detects unusual patterns in time series data.

### Configuration:
- Enable "Anomaly Detection" in Analytics pane
- Set sensitivity level (higher = more anomalies detected)
- Configure expected range and seasonality
- Add explanations for detected anomalies

## 6. AI-Powered Clustering (Python/R Visual)

### Purpose
Automatically segment your claims data into meaningful groups.

## 7. Best Practices for AI Visuals

### Data Preparation:
1. **Clean Data**: Remove or handle outliers appropriately
2. **Meaningful Categories**: Ensure categorical fields have business meaning
3. **Appropriate Granularity**: Balance detail with performance
4. **Date Formatting**: Use proper date/time formats

### Performance Optimization:
1. **Limit Cardinality**: Keep unique values under 1000 for explain-by fields
2. **Use Measures**: Create calculated measures for better performance
3. **Filter Context**: Apply appropriate filters to focus analysis
4. **Aggregation**: Use appropriate aggregation levels

### Business Context:
1. **Domain Knowledge**: Apply insurance expertise to interpret results
2. **Validation**: Cross-check AI insights with business logic
3. **Actionability**: Focus on insights that drive business decisions
4. **Communication**: Present findings in business-friendly language

## 8. Troubleshooting Common Issues

### Key Influencers Not Working:
- Check data types (categorical vs. numerical)
- Reduce cardinality of explain-by fields
- Ensure sufficient data points per category

### Decomposition Tree Performance:
- Limit the number of explain-by fields
- Use hierarchical fields where possible
- Apply filters to reduce data volume

### Q&A Not Understanding Questions:
- Add synonyms for your business terms
- Use simpler, more direct questions
- Train the model with common phrases

### Python Visual Errors:
- Check that required libraries are available
- Validate data types and null values
- Use try-catch blocks for error handling

