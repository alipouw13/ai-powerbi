# DAX measures

Please use the following CoPilot prompt to discover new DAX measures: _"Suggest measures to calculate revenue forcasts from the Opportunities table and existing measures."_

Create the following DAX measures in your table or similar:

## Weighted value of open opportunities using their probability (expected value)

```
Weighted Open Revenue =
    CALCULATE(
      SUMX(
        Opportunities,
        Opportunities[Value] * Opportunities[Probability (raw)]
      ),
      FILTER(Opportunities, Opportunities[Status] = "Open")
    )
```

## Optional global forecast adjustment (averages any selection from the adjustment table)

```
Forecast Adjustment % =
    DIVIDE(
      AVERAGE('Opportunity Forecast Adjustment'[Forecast Adjustment]),
      100
    )
```

## Revenue Forecast = Won revenue + weighted open revenue (optionally adjusted)

```
Revenue Forecast =
    [Revenue Won] + ([Weighted Open Revenue] * (1 + [Forecast Adjustment %]))
```

## Gap to Owner Goal (positive = above goal, negative = below)

```
Delta to Rev Goal =
    [Revenue Forecast] - [Rev Goal]
```