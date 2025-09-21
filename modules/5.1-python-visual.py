# Simple Python Visual for Power BI - Sales Opportunity Analysis
# Paste this code directly into Power BI Python Visual editor
# 
# REQUIRED FIELDS: Add these fields to the Values section in Power BI:
# - Value (from Opportunities table)
# - Probability (from Opportunities table) 
# - Status (from Opportunities table) [Optional but recommended]
#   - transforms your scatter plot from a data display into a strategic BI tool that 
#     reveals sales performance patterns, pipeline health, and opportunity conversion insights

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Configure plot style for Power BI
plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 10

# Create the visualization
plt.figure(figsize=(10, 6))

# Check if we have the required columns
if 'Value' in dataset.columns and 'Probability' in dataset.columns:
    
    # Create scatter plot with color coding by Status (if available)
    if 'Status' in dataset.columns:
        # Get unique statuses and assign colors
        statuses = dataset['Status'].unique()
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        
        for i, status in enumerate(statuses):
            subset = dataset[dataset['Status'] == status]
            color = colors[i % len(colors)]
            plt.scatter(subset['Probability'], subset['Value'], 
                       label=status, alpha=0.7, s=80, color=color)
    else:
        plt.scatter(dataset['Probability'], dataset['Value'], 
                   alpha=0.7, s=80, color='steelblue')
    
    # Customize the plot
    plt.xlabel('Probability (%)', fontsize=12, fontweight='bold')
    plt.ylabel('Value ($)', fontsize=12, fontweight='bold')
    plt.title('Sales Opportunities: Value vs Probability', fontsize=14, fontweight='bold', pad=20)
    
    # Add legend if we have status information
    if 'Status' in dataset.columns:
        plt.legend(title='Opportunity Status', title_fontsize=10, fontsize=9)
    
    # Add grid for better readability
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Format y-axis to show currency
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    # Add trend line if we have enough data points
    if len(dataset) > 1:
        # Clean data for trend line
        clean_data = dataset.dropna(subset=['Probability', 'Value'])
        if len(clean_data) > 1:
            z = np.polyfit(clean_data['Probability'], clean_data['Value'], 1)
            p = np.poly1d(z)
            x_trend = np.linspace(clean_data['Probability'].min(), clean_data['Probability'].max(), 100)
            plt.plot(x_trend, p(x_trend), "r--", alpha=0.8, linewidth=2, label='Trend')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
else:
    # Fallback: Create a simple bar chart with available data
    if len(dataset.columns) > 0:
        # Find first numerical column
        numerical_cols = dataset.select_dtypes(include=[np.number]).columns
        categorical_cols = dataset.select_dtypes(include=['object']).columns
        
        if len(numerical_cols) > 0 and len(categorical_cols) > 0:
            num_col = numerical_cols[0]
            cat_col = categorical_cols[0]
            
            # Group data and create bar chart
            grouped_data = dataset.groupby(cat_col)[num_col].sum().sort_values(ascending=False).head(10)
            
            plt.bar(range(len(grouped_data)), grouped_data.values, color='steelblue', alpha=0.8)
            plt.xlabel(cat_col, fontsize=12, fontweight='bold')
            plt.ylabel(num_col, fontsize=12, fontweight='bold')
            plt.title(f'{num_col} by {cat_col}', fontsize=14, fontweight='bold')
            plt.xticks(range(len(grouped_data)), grouped_data.index, rotation=45)
            plt.grid(True, alpha=0.3, axis='y')
            plt.tight_layout()
        else:
            plt.text(0.5, 0.5, 'Please add numerical and categorical fields\nto the Values section', 
                    ha='center', va='center', fontsize=12, transform=plt.gca().transAxes)
            plt.title('Python Visual - Waiting for Data', fontsize=14)
    else:
        plt.text(0.5, 0.5, 'Please add fields to the Values section', 
                ha='center', va='center', fontsize=12, transform=plt.gca().transAxes)
        plt.title('Python Visual - No Data', fontsize=14)

# Display the plot
plt.show()
