# Power BI Python Visual Implementation Guide

## Overview
This guide shows how to create Python visuals in Power BI using your Contoso Sales data model. Based on Microsoft's best practices and the data structure visible in your screenshot.

## Prerequisites
1. Power BI Desktop (latest version)
2. Python installed on your machine
3. Required Python packages:
   - pandas
   - matplotlib
   - numpy
   - seaborn (optional, for advanced visualizations)

## Installation Steps

### 1. Install Python Packages
Open Command Prompt or PowerShell and run:
```bash
pip install pandas matplotlib numpy seaborn
```

### 2. Enable Python in Power BI Desktop
1. Go to **File** > **Options and settings** > **Options**
2. Select **Python scripting** in the left panel
3. Set the Python home directory to your Python installation
4. Click **OK**

## Using the Python Visual

### Step 1: Add Python Visual
1. In Power BI Desktop, click the **Python visual** icon in the Visualizations pane
2. If prompted, click **Enable** to enable script visuals

### Step 2: Add Data Fields
Based on your data model, add these fields to the **Values** section:

**For Opportunity Analysis:**
- Value (from Opportunities table)
- Probability (from Opportunities table)  
- Status (from Opportunities table)

**Alternative fields you can use:**
- Account Owner (from Accounts)
- Campaign Name (from Campaigns)
- Product Category (from Products)
- Territory (from Territories)
- Case Priority (from Cases)
- Revenue figures
- Date fields for time series

### Step 3: Paste the Python Code
Copy and paste one of the following scripts into the Python script editor:

## Script Option 1: Opportunity Scatter Plot
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configure plot for Power BI
plt.figure(figsize=(10, 6))

# Opportunity Value vs Probability Analysis
if 'Value' in dataset.columns and 'Probability' in dataset.columns:
    
    # Color by Status if available
    if 'Status' in dataset.columns:
        for status in dataset['Status'].unique():
            subset = dataset[dataset['Status'] == status]
            plt.scatter(subset['Probability'], subset['Value'], 
                       label=status, alpha=0.7, s=80)
        plt.legend(title='Status')
    else:
        plt.scatter(dataset['Probability'], dataset['Value'], 
                   alpha=0.7, s=80, color='steelblue')
    
    plt.xlabel('Probability (%)')
    plt.ylabel('Value ($)')
    plt.title('Sales Opportunities: Value vs Probability')
    plt.grid(True, alpha=0.3)
    
    # Add trend line
    if len(dataset) > 1:
        clean_data = dataset.dropna(subset=['Probability', 'Value'])
        if len(clean_data) > 1:
            z = np.polyfit(clean_data['Probability'], clean_data['Value'], 1)
            p = np.poly1d(z)
            x_trend = np.linspace(clean_data['Probability'].min(), clean_data['Probability'].max(), 100)
            plt.plot(x_trend, p(x_trend), "r--", alpha=0.8, linewidth=2)

plt.tight_layout()
plt.show()
```

## Script Option 2: Sales Pipeline Analysis
```python
import matplotlib.pyplot as plt
import pandas as pd

# Configure plot
plt.figure(figsize=(10, 6))

# Sales Pipeline by Stage
if 'Stage' in dataset.columns and any(col for col in dataset.columns if 'Value' in col or 'Revenue' in col):
    
    # Find value column
    value_col = next((col for col in dataset.columns if 'Value' in col or 'Revenue' in col), None)
    
    if value_col:
        # Group by stage
        stage_data = dataset.groupby('Stage')[value_col].sum().sort_values(ascending=True)
        
        # Create horizontal bar chart
        bars = plt.barh(range(len(stage_data)), stage_data.values, color='steelblue', alpha=0.8)
        
        plt.yticks(range(len(stage_data)), stage_data.index)
        plt.xlabel(f'Total {value_col} ($)')
        plt.title('Sales Pipeline by Stage')
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, stage_data.values)):
            plt.text(bar.get_width() + max(stage_data.values) * 0.01, 
                    bar.get_y() + bar.get_height()/2, 
                    f'${value:,.0f}', va='center')

plt.tight_layout()
plt.show()
```

## Script Option 3: Top Performers Analysis
```python
import matplotlib.pyplot as plt
import pandas as pd

# Configure plot
plt.figure(figsize=(12, 6))

# Top Performers Analysis
if 'Account Owner' in dataset.columns or 'Sales Rep' in dataset.columns:
    
    # Find owner column
    owner_col = 'Account Owner' if 'Account Owner' in dataset.columns else 'Sales Rep'
    value_col = next((col for col in dataset.columns if 'Value' in col or 'Revenue' in col), None)
    
    if value_col:
        # Group by owner and sum values
        owner_performance = dataset.groupby(owner_col)[value_col].sum().sort_values(ascending=False).head(10)
        
        # Create bar chart
        plt.bar(range(len(owner_performance)), owner_performance.values, color='steelblue', alpha=0.8)
        
        plt.xticks(range(len(owner_performance)), owner_performance.index, rotation=45)
        plt.ylabel(f'Total {value_col} ($)')
        plt.title(f'Top 10 Performers by {value_col}')
        plt.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()
```

## Script Option 4: Time Series Analysis
```python
import matplotlib.pyplot as plt
import pandas as pd

# Configure plot
plt.figure(figsize=(12, 6))

# Time series analysis
date_cols = [col for col in dataset.columns if 'Date' in col or 'Created' in col]
value_cols = [col for col in dataset.columns if 'Value' in col or 'Revenue' in col]

if date_cols and value_cols:
    date_col = date_cols[0]
    value_col = value_cols[0]
    
    # Convert to datetime
    dataset[date_col] = pd.to_datetime(dataset[date_col])
    
    # Group by date and sum values
    daily_data = dataset.groupby(dataset[date_col].dt.date)[value_col].sum().sort_index()
    
    # Plot line chart
    plt.plot(daily_data.index, daily_data.values, linewidth=2, color='steelblue')
    plt.xlabel('Date')
    plt.ylabel(f'{value_col} ($)')
    plt.title(f'{value_col} Over Time')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## Best Practices

### 1. Data Preparation
- Always check if columns exist before using them
- Handle missing values appropriately
- Use meaningful field names in your data model

### 2. Visualization Design
- Keep plots simple and focused
- Use appropriate colors and styling
- Add legends and labels for clarity
- Format axes appropriately (currency, percentages, etc.)

### 3. Performance Tips
- Limit data to 150,000 rows (Power BI limit)
- Use aggregations when possible
- Test with smaller datasets first

### 4. Error Handling
```python
# Always check for required columns
if 'ColumnName' in dataset.columns:
    # Your visualization code here
    pass
else:
    plt.text(0.5, 0.5, 'Required field missing', ha='center', va='center')
    plt.show()
```

## Common Data Model Fields for Contoso Sales

Based on your screenshot, here are field combinations you can use:

**Opportunities Analysis:**
- Value + Probability + Status
- AccountID + Value + Stage
- Created On + Value (time series)

**Campaign Analysis:**
- Campaign Name + Budget + Response Rate
- Campaign Type + Leads Generated

**Customer Analysis:**
- Account Name + Total Revenue + Industry
- Territory + Customer Count + Revenue

**Product Analysis:**
- Product Category + Units Sold + Revenue
- Product Name + Profit Margin

**Case Analysis:**
- Case Priority + Resolution Time
- Case Origin + Case Count + Status

## Troubleshooting

### Common Issues:
1. **"dataset is not defined"** - This is normal in the editor; it's provided by Power BI at runtime
2. **Import errors** - Ensure Python packages are installed correctly
3. **No data showing** - Check that fields are added to the Values section
4. **Plot not updating** - Click the "Run" button after making changes

### Testing Your Code:
1. Start with simple visualizations
2. Add one field at a time
3. Use print statements to debug: `print(dataset.columns)`
4. Check data types: `print(dataset.dtypes)`

For more advanced examples, see the `powerbi-python-visual-examples.py` file in this repository.
