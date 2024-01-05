----

[Home](./index.md) > [Supply Chain Sample.pbix](Supply%20Chain%20Sample.pbix_report.md)

| [Report sections](#report-sections) |

----


# Report sections

## Risk Analytics

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectionaeffc6c2512def112cfa` |
| **Display Name** | `Risk Analytics` |
| **Filters** | `[]` |
| **Ordinal** | `0` |
| **Visual containers number** | `7` |

[Up](#report-sections)



### Container 785e37af27ec534ab424 

| Param  | Value  |
|---|---|
| **Name:** | `785e37af27ec534ab424` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 7c6a9e1b57ab7ebd6ad8 

| Param  | Value  |
|---|---|
| **Name:** | `7c6a9e1b57ab7ebd6ad8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 77f9305cd13f3320304c 

| Param  | Value  |
|---|---|
| **Name:** | `77f9305cd13f3320304c` |
| **Type:** | `PowerApps_PBI_CV_C29F1DCC_81F5_4973_94AD_0517D44CC06A` |
| **Business objects:**  | `Backorder Percentage` | 
| **Attributes:**  | Column: Backorder Percentage.Plant<br/> Column: Backorder Percentage.Product Type | 

[Up](#report-sections)




### Container 081c4b66305790c87291 

| Param  | Value  |
|---|---|
| **Name:** | `081c4b66305790c87291` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 60f36c4ab1755d40a1d3 

| Param  | Value  |
|---|---|
| **Name:** | `60f36c4ab1755d40a1d3` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `Explanations` | 
| **Attributes:**  | Column: Explanations.Factor<br/> Aggregation: Sum(Explanations.Risk) | 

[Up](#report-sections)




### Container 7bf07d56957f69193161 

| Param  | Value  |
|---|---|
| **Name:** | `7bf07d56957f69193161` |
| **Type:** | `tableEx` |
| **Business objects:**  | `Risk` | 
| **Attributes:**  | Column: Risk.Location<br/> Column: Risk.Product ID<br/> Column: Risk.Risk Score<br/> Column: Risk.Backorder Risk<br/> Column: Risk.Distribution Center | 

[Up](#report-sections)




### Container 4a9898755b7be14b5605 

| Param  | Value  |
|---|---|
| **Name:** | `4a9898755b7be14b5605` |
| **Type:** | `esriVisual` |
| **Business objects:**  | `Risk` | 
| **Attributes:**  | Column: Risk.Location<br/> Aggregation: CountNonNull(Risk.Product ID) | 

[Up](#report-sections)


## Exploratory Analysis

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection0805d6522ced0b422d38` |
| **Display Name** | `Exploratory Analysis` |
| **Filters** | `[]` |
| **Ordinal** | `1` |
| **Visual containers number** | `8` |

[Up](#report-sections)



### Container 0d8ec8d54ccfa45ab88f 

| Param  | Value  |
|---|---|
| **Name:** | `0d8ec8d54ccfa45ab88f` |
| **Type:** | `barChart` |
| **Business objects:**  | `Backorder Percentage, Month` | 
| **Attributes:**  | Aggregation: Avg(Backorder Percentage.Backorder %)<br/> Column: Month.Month | 

[Up](#report-sections)




### Container 785e37af27ec534ab424 

| Param  | Value  |
|---|---|
| **Name:** | `785e37af27ec534ab424` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 7c6a9e1b57ab7ebd6ad8 

| Param  | Value  |
|---|---|
| **Name:** | `7c6a9e1b57ab7ebd6ad8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 77f9305cd13f3320304c 

| Param  | Value  |
|---|---|
| **Name:** | `77f9305cd13f3320304c` |
| **Type:** | `PowerApps_PBI_CV_C29F1DCC_81F5_4973_94AD_0517D44CC06A` |
| **Business objects:**  | `Backorder Percentage` | 
| **Attributes:**  | Column: Backorder Percentage.Plant<br/> Column: Backorder Percentage.Product Type | 

[Up](#report-sections)




### Container cc83889ee3c0277d6686 

| Param  | Value  |
|---|---|
| **Name:** | `cc83889ee3c0277d6686` |
| **Type:** | `decompositionTreeVisual` |
| **Business objects:**  | `Backorder Percentage` | 
| **Attributes:**  | Measure: Backorder Percentage.% on backorder<br/> Column: Backorder Percentage.Forecast Bias<br/> Column: Backorder Percentage.Plant<br/> Column: Backorder Percentage.Product Type<br/> Column: Backorder Percentage.Shipment Destination<br/> Column: Backorder Percentage.Shipment Type<br/> Column: Backorder Percentage.Region<br/> Column: Backorder Percentage.Distribution Center<br/> Column: Backorder Percentage.Demand Type<br/> Column: Backorder Percentage.Forecast Accuracy<br/> Column: Backorder Percentage.Brand<br/> Column: Backorder Percentage.Buyer Type<br/> Measure: Backorder Percentage.Backorder $ | 

[Up](#report-sections)




### Container 081c4b66305790c87291 

| Param  | Value  |
|---|---|
| **Name:** | `081c4b66305790c87291` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 259d088b60d6704886d0 

| Param  | Value  |
|---|---|
| **Name:** | `259d088b60d6704886d0` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 5649b3e28d77b8aee842 

| Param  | Value  |
|---|---|
| **Name:** | `5649b3e28d77b8aee842` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Ask Questions

| Param  | Value  |
|---|---|
| **ID** | `31589085` |
| **Name** | `ReportSection` |
| **Display Name** | `Ask Questions` |
| **Filters** | `[]` |
| **Ordinal** | `2` |
| **Visual containers number** | `4` |

[Up](#report-sections)



### Container a3402b31dd4040b1942a 

| Param  | Value  |
|---|---|
| **Name:** | `a3402b31dd4040b1942a` |
| **Type:** | `treemap` |
| **Business objects:**  | `Backorder Percentage` | 
| **Attributes:**  | Measure: Backorder Percentage.% on backorder<br/> Column: Backorder Percentage.Demand Type | 

[Up](#report-sections)




### Container 2d77eb4274b5410b420d 

| Param  | Value  |
|---|---|
| **Name:** | `2d77eb4274b5410b420d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 2a4dc2b00972cea35e43 

| Param  | Value  |
|---|---|
| **Name:** | `2a4dc2b00972cea35e43` |
| **Type:** | `areaChart` |
| **Business objects:**  | `Month, Backorder Percentage` | 
| **Attributes:**  | Column: Month.Month<br/> Measure: Backorder Percentage.Backorder $ | 

[Up](#report-sections)




### Container 44b1eb99372df10740c4 

| Param  | Value  |
|---|---|
| **Name:** | `44b1eb99372df10740c4` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Supply Chain Analytics

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectiond48f10a3d83531ea24b4` |
| **Display Name** | `Supply Chain Analytics` |
| **Filters** | `[]` |
| **Ordinal** | `3` |
| **Visual containers number** | `4` |

[Up](#report-sections)



### Container f06d7cb16e3ae52d23d3 

| Param  | Value  |
|---|---|
| **Name:** | `f06d7cb16e3ae52d23d3` |
| **Type:** | `columnChart` |
| **Business objects:**  | `Backorder Percentage` | 
| **Attributes:**  | Measure: Backorder Percentage.Backorder $<br/> Column: Backorder Percentage.Region | 

[Up](#report-sections)




### Container a3402b31dd4040b1942a 

| Param  | Value  |
|---|---|
| **Name:** | `a3402b31dd4040b1942a` |
| **Type:** | `treemap` |
| **Business objects:**  | `Supply Analytics` | 
| **Attributes:**  | Aggregation: CountNonNull(bank-full2.Product )<br/> Column: Supply Analytics.Demand Type | 

[Up](#report-sections)




### Container 47ab9237785e689bbcb5 

| Param  | Value  |
|---|---|
| **Name:** | `47ab9237785e689bbcb5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container ca1930b86620637c9caa 

| Param  | Value  |
|---|---|
| **Name:** | `ca1930b86620637c9caa` |
| **Type:** | `keyDriversVisual` |
| **Business objects:**  | `Supply Analytics` | 
| **Attributes:**  | Column: Supply Analytics.Product <br/> Column: Supply Analytics.Demand Type<br/> Column: Supply Analytics.Forecast Accuracy<br/> Column: Supply Analytics.Forecast Bias<br/> Column: Supply Analytics.Manufactured Goods | 

[Up](#report-sections)







----
<p align="center">
Generated at 05.01.2024 01:07:16 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 
</p>