# Module 5: Create a python visual



This guide shows how to create Python visuals in Power BI using your Contoso Sales data model. Based on Microsoft's best practices and the data structure visible in your screenshot.

## Prerequisites
Use the `5.1-python-visual.py` script to create a python visual. Make sure you have the following prerequisites before attempting to create:
- [Install Python](https://www.python.org/) on your local machine.
- [Enable Python scripting](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts#enable-python-scripting) in Power BI Desktop
- Install the right [packages](https://learn.microsoft.com/en-us/power-bi/connect-data/service-python-packages-support) for the script below:
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

1. On the **Python visual** page, click on the python visual and add these fields to the **Values** section:
    - Value (from Opportunities table)
    - Probability (from Opportunities table) 
    - Status (from Opportunities table)

2. Paste the Python Code from `5.1-python-visual.py`
3. Click the play button to run the script