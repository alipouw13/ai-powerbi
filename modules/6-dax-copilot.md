# Module 6: Create DAX queries with CoPilot

Leverage copilot to create DAX queries.

## Exercise 6.1: Use DAX
1. Go to DAX in the left pane
2. Use the following CoPilot prompt to discover new DAX measures: _"Suggest a measure to calculate revenue forcasts from the Opportunities table."_
3. Click 'Run' to try it out.

![DAX upload](https://github.com/alipouw13/ai-powerbi/blob/main/images/dax-copilot.png)

4. When ready, select 'Update model' to add the measure to your model. See below for the sample query.

```
Revenue Forecast (Net Adj) =
    VAR _WonNet =
      CALCULATE(
        SUMX(
          FILTER(Opportunities, Opportunities[Status] = "Won"),
          Opportunities[Value] * (1 - Opportunities[Discount]) // apply discount to won deals
        )
      )
    VAR _OpenWeightedNet =
      CALCULATE(
        SUMX(
          FILTER(Opportunities, Opportunities[Status] = "Open"),
          Opportunities[Value] * (1 - Opportunities[Discount]) * Opportunities[Probability (raw)] // discounted and probability-weighted open deals
        )
      )
    VAR _AdjPct = [Forecast Adjustment %] // measure from 'Opportunity Forecast Adjustment' table (already modeled)
    RETURN
      _WonNet + (_OpenWeightedNet * (1 + _AdjPct))
```
