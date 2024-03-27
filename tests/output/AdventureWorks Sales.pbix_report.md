----

[Home](./index.md) > [AdventureWorks Sales.pbix](AdventureWorks%20Sales.pbix_report.md)

| [Report sections](#report-sections) |

----


# Report sections

## Page 1

| Param  | Value  |
|---|---|
| **ID** | `0` |
| **Name** | `ReportSection` |
| **Display Name** | `Page 1` |
| **Filters** |  |
| **Ordinal** | `0` |
| **Visual containers number** | `6` |

[Up](#report-sections)



### Container 4815acfc1f588ed839c4 

| Param  | Value  |
|---|---|
| **Name:** | `4815acfc1f588ed839c4` |
| **Type:** | `areaChart` |
| **Business objects:**  | `Date, Sales` | 
| **Attributes:**  | Aggregation: `Sum(Sales.Sales Amount)`<br/> Measure: `Sales.Sales Amount by Due Date`<br/> HierarchyLevel: `Date.Fiscal.Month` | 

[Up](#report-sections)




### Container 43718bfbc9b53930dbee 

| Param  | Value  |
|---|---|
| **Name:** | `43718bfbc9b53930dbee` |
| **Type:** | `map` |
| **Business objects:**  | `Sales, Reseller` | 
| **Attributes:**  | Aggregation: `Sum(Sales.Order Quantity)`<br/> Column: `Reseller.Country-Region` | 

[Up](#report-sections)




### Container 3a1aeaede6fc79fe5066 

| Param  | Value  |
|---|---|
| **Name:** | `3a1aeaede6fc79fe5066` |
| **Type:** | `pivotTable` |
| **Business objects:**  | `Product, Reseller, Sales` | 
| **Attributes:**  | Column: `Product.Category`<br/> Column: `Reseller.Business Type`<br/> Aggregation: `Sum(Sales.Sales Amount)` | 

[Up](#report-sections)




### Container 75c624f501f3c20eb760 

| Param  | Value  |
|---|---|
| **Name:** | `75c624f501f3c20eb760` |
| **Type:** | `slicer` |
| **Business objects:**  | `Date` | 
| **Attributes:**  | HierarchyLevel: `Date.Fiscal.Year`<br/> HierarchyLevel: `Date.Fiscal.Month` | 

[Up](#report-sections)




### Container e62f8d740cd4f569300d 

| Param  | Value  |
|---|---|
| **Name:** | `e62f8d740cd4f569300d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container ddc669d1ed997bf82754 

| Param  | Value  |
|---|---|
| **Name:** | `ddc669d1ed997bf82754` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Page 2

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection350b6b55132e00f8ba89` |
| **Display Name** | `Page 2` |
| **Filters** |  |
| **Ordinal** | `1` |
| **Visual containers number** | `1` |

[Up](#report-sections)



### Container 81c88ed0eeabf5421b8f 

| Param  | Value  |
|---|---|
| **Name:** | `81c88ed0eeabf5421b8f` |
| **Type:** | `pivotTable` |
| **Business objects:**  | `Product, Reseller, Sales` | 
| **Attributes:**  | Column: `Product.Category`<br/> Column: `Reseller.Business Type`<br/> Aggregation: `Sum(Sales.Sales Amount)` | 

[Up](#report-sections)


## Page 3

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectiona113e22f3ad54b8397d8` |
| **Display Name** | `Page 3` |
| **Filters** |  |
| **Ordinal** | `2` |
| **Visual containers number** | `1` |

[Up](#report-sections)



### Container ec25b2f7759b3fd44c1d 

| Param  | Value  |
|---|---|
| **Name:** | `ec25b2f7759b3fd44c1d` |
| **Type:** | `areaChart` |
| **Business objects:**  | `Date, Sales` | 
| **Attributes:**  | HierarchyLevel: `Date.Fiscal.Month`<br/> Aggregation: `Sum(Sales.Sales Amount)`<br/> Measure: `Sales.Sales Amount by Due Date` | 

[Up](#report-sections)







----
<p align="center">
Generated at 27.03.2024 13:01:37 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 
</p>