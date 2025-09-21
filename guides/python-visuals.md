# Additional python scripts


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
