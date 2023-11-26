----

[Home](../home.md) > [AdventureWorks_Sales2.pbix](index.md)

[Information](#information) | [Model information](#model-information) | [Model relationships](#model-relationships) | [Business objects](#business-objects) | [Measures](#measures) | [Relationships](#relationships) | [Hierarchies](#hierarchies) | [Columns](#columns) | 

----

# Information

Documentation for file **AdventureWorks_Sales2.pbix**.

# Model information


| Param  | Value  |
|---|---|
| **Catalog name** | `418255b2-96be-4dcd-9ddd-0a2ecea747a0` | 
| **Port** | `61006`|
| **Description** | `-NaN-` | 
| **Date modified** | `2023-11-22T21:37:51` | 
| **Compatibility level** | `1567` | 


[Up](#)
# Model relationships

```mermaid
graph LR;

id186(["LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959[-NaN-]"]) --> id183(["Date[Date]"])
id189(["LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854[-NaN-]"]) --> id183(["Date[Month]"])
id192(["LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696[-NaN-]"]) --> id183(["Date[Full Date]"])
id12(["Customer[CustomerKey]"]) --> id805(["Sales[CustomerKey]"])
id572(["Product[ProductKey]"]) --> id805(["Sales[ProductKey]"])
id690(["Reseller[ResellerKey]"]) --> id805(["Sales[ResellerKey]"])
id805(["Sales[SalesOrderLineKey]"]) --> id980(["Sales Order[SalesOrderLineKey]"])
id1078(["Sales Territory[SalesTerritoryKey]"]) --> id805(["Sales[SalesTerritoryKey]"])
id183(["Date[DateKey]"]) --> id805(["Sales[OrderDateKey]"])
id3642(["Table[Category]"]) --> id572(["Product[Category]"])
```



[Up](#)
# Business objects

| ID| NAME | DESCRIPTION | MODIFIED_TIME | STRUCTURE_MODIFIED_TIME |
|---|-------------|-----------------:|---------------: |---------------:|
| 12 | Customer | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T22:06:01 |
| 183 | Date | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T22:07:07 |
| 572 | Product | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T23:04:32 |
| 690 | Reseller | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T22:09:20 |
| 805 | Sales | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T22:02:59 |
| 980 | Sales Order | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T22:09:47 |
| 1078 | Sales Territory | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T22:10:09 |
| 3642 | Table | -NaN- | 2022-09-22T22:59:56 |  2020-12-16T23:04:03 |



[Up](#)
# Measures


| ID | TABLE | NAME | DESCRIPTION | EXPRESSION | IS_HIDDEN | STATE |
|----|-------|------|-------------|------------|-----------|-------|
| 19 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 |  | -NaN- | YEAR([Date]) | True |  1 |  
| 20 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 |  | -NaN- | MONTH([Date]) | True |  1 |  
| 21 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 |  | -NaN- | FORMAT([Date], "MMMM") | True |  1 |  
| 22 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 |  | -NaN- | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 23 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 |  | -NaN- | "Qtr " & [QuarterNo] | True |  1 |  
| 24 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 |  | -NaN- | DAY([Date]) | True |  1 |  
| 201 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 |  | -NaN- | YEAR([Date]) | True |  1 |  
| 202 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 |  | -NaN- | MONTH([Date]) | True |  1 |  
| 203 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 |  | -NaN- | FORMAT([Date], "MMMM") | True |  1 |  
| 204 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 |  | -NaN- | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 205 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 |  | -NaN- | "Qtr " & [QuarterNo] | True |  1 |  
| 206 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 |  | -NaN- | DAY([Date]) | True |  1 |  
| 211 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 |  | -NaN- | YEAR([Date]) | True |  1 |  
| 212 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 |  | -NaN- | MONTH([Date]) | True |  1 |  
| 213 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 |  | -NaN- | FORMAT([Date], "MMMM") | True |  1 |  
| 214 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 |  | -NaN- | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 215 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 |  | -NaN- | "Qtr " & [QuarterNo] | True |  1 |  
| 216 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 |  | -NaN- | DAY([Date]) | True |  1 |  
| 219 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 |  | -NaN- | YEAR([Date]) | True |  1 |  
| 220 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 |  | -NaN- | MONTH([Date]) | True |  1 |  
| 221 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 |  | -NaN- | FORMAT([Date], "MMMM") | True |  1 |  
| 222 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 |  | -NaN- | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 223 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 |  | -NaN- | "Qtr " & [QuarterNo] | True |  1 |  
| 224 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 |  | -NaN- | DAY([Date]) | True |  1 |  
| 3742 | Product |  | -NaN- | RELATED('Table'[Sorting]) | False |  1 |  


[Up](#)
# Relationships 


| ID | FROM_TABLE_ID | FROM_CARDINALITY | TO_TABLE_ID | TO_CARDINALITY | NAME | IS_ACTIVE  |
|----|---------------|------------------|-------------|----------------|------|------------|
| 195 | Date[Date] | 2 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959[-NaN-] | 1 | 88371ba8-2389-41b4-a22f-bcb756732d3b | True |
| 196 | Date[Month] | 2 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854[-NaN-] | 1 | 586c9eeb-fe2f-431d-a8c4-9723ce217f20 | True |
| 197 | Date[Full Date] | 2 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696[-NaN-] | 1 | 401217e9-9553-4835-a527-fd574f68046d | True |
| 3224 | Sales[CustomerKey] | 2 | Customer[CustomerKey] | 1 | e3030baf-8c61-408d-a80e-04714277dcd3 | True |
| 3227 | Sales[ProductKey] | 2 | Product[ProductKey] | 1 | a0a78efb-3ce3-472a-993a-b92e31c0e3cd | True |
| 3230 | Sales[ResellerKey] | 2 | Reseller[ResellerKey] | 1 | 0ef2b150-bb90-4b8f-8537-fc236873591c | True |
| 3233 | Sales Order[SalesOrderLineKey] | 1 | Sales[SalesOrderLineKey] | 1 | 29b21f6a-77ef-4b3b-a0c0-e4111f87627b | True |
| 3238 | Sales[SalesTerritoryKey] | 2 | Sales Territory[SalesTerritoryKey] | 1 | cecf591c-1f02-44a6-bff1-1c753a0b4835 | True |
| 3305 | Sales[OrderDateKey] | 2 | Date[DateKey] | 1 | 8e31fd7b-1e63-43a9-8a47-33876ae8aed6 | True |
| 3322 | Sales[DueDateKey] | 2 | Date[DateKey] | 1 | dfb7bf63-667c-4abb-b494-7424c4e34b60 | False |
| 3339 | Sales[ShipDateKey] | 2 | Date[DateKey] | 1 | 6a63bfea-7b52-4e05-85f4-63a0f9b8991f | False |
| 3725 | Product[Category] | 2 | Table[Category] | 1 | 93a2e7c9-4a15-47be-93c0-06eceb139103 | True |


[Up](#)
# Hierarchies 



| ID | TABLE_ID | NAME | DESCRIPTION  | IS_HIDDEN | 
|----|----------|------|--------------|-----------|-
| 3356 |Customer | Geography | -NaN- | False | 
| 27 |DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | Date Hierarchy | -NaN- | False | 
| 3399 |Date | Fiscal | -NaN- | False | 
| 230 |LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | Date Hierarchy | -NaN- | False | 
| 231 |LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | Date Hierarchy | -NaN- | False | 
| 232 |LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | Date Hierarchy | -NaN- | False | 
| 3476 |Product | Products | -NaN- | False | 
| 3518 |Reseller | Geography | -NaN- | False | 
| 3561 |Sales Order | Sales Orders | -NaN- | False | 
| 3601 |Sales Territory | Sales Territories | -NaN- | False | 


[Up](#)
# Columns 


| ID | TABLE_ID | EXPLICIT_NAME | SOURCE_COLUMN | COLUMN_ORIGIN_ID | DATA_CATEGORY | DESCRIPTION | IS_HIDDEN | STATE | IS_UNIQUE | TYPE | EXPRESSION |
|----|----------|---------------|---------------|------------------|---------------|-------------|-----------|-------|-----------|------|------------|
| 13 | Customer | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 113 | Customer | CustomerKey | CustomerKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 114 | Customer | Customer ID | Customer ID | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 115 | Customer | Customer | Customer | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 116 | Customer | City | City | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 117 | Customer | State-Province | State-Province | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 118 | Customer | Country-Region | Country-Region | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 119 | Customer | Postal Code | Postal Code | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 16 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 18 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | -NaN- | [Date] | -NaN- | PaddedDateTableDates | -NaN- | True | 1 | False | 4 | -NaN- |
| 19 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | Year | -NaN- | -NaN- | Years | -NaN- | True | 1 | False | 2 | YEAR([Date]) |
| 20 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | MonthNo | -NaN- | -NaN- | MonthOfYear | -NaN- | True | 1 | False | 2 | MONTH([Date]) |
| 21 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | Month | -NaN- | -NaN- | Months | -NaN- | True | 1 | False | 2 | FORMAT([Date], "MMMM") |
| 22 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | QuarterNo | -NaN- | -NaN- | QuarterOfYear | -NaN- | True | 1 | False | 2 | INT(([MonthNo] + 2) / 3) |
| 23 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | Quarter | -NaN- | -NaN- | Quarters | -NaN- | True | 1 | False | 2 | "Qtr " & [QuarterNo] |
| 24 | DateTableTemplate_788642c5-9a9d-4431-b350-9f47f7e53393 | Day | -NaN- | -NaN- | DayOfMonth | -NaN- | True | 1 | False | 2 | DAY([Date]) |
| 184 | Date | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 198 | Date | DateKey | DateKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 199 | Date | Date | Date | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 207 | Date | Fiscal Year | Fiscal Year | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 208 | Date | Fiscal Quarter | Fiscal Quarter | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 209 | Date | Month | Month | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 217 | Date | Full Date | Full Date | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 225 | Date | MonthKey | MonthKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 187 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 200 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | -NaN- | [Date] | -NaN- | PaddedDateTableDates | -NaN- | True | 1 | False | 4 | -NaN- |
| 201 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | Year | -NaN- | -NaN- | Years | -NaN- | True | 1 | False | 2 | YEAR([Date]) |
| 202 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | MonthNo | -NaN- | -NaN- | MonthOfYear | -NaN- | True | 1 | False | 2 | MONTH([Date]) |
| 203 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | Month | -NaN- | -NaN- | Months | -NaN- | True | 1 | False | 2 | FORMAT([Date], "MMMM") |
| 204 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | QuarterNo | -NaN- | -NaN- | QuarterOfYear | -NaN- | True | 1 | False | 2 | INT(([MonthNo] + 2) / 3) |
| 205 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | Quarter | -NaN- | -NaN- | Quarters | -NaN- | True | 1 | False | 2 | "Qtr " & [QuarterNo] |
| 206 | LocalDateTable_1635aca9-f5cf-4673-8bd0-6cbe59eca959 | Day | -NaN- | -NaN- | DayOfMonth | -NaN- | True | 1 | False | 2 | DAY([Date]) |
| 190 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 210 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | -NaN- | [Date] | -NaN- | PaddedDateTableDates | -NaN- | True | 1 | False | 4 | -NaN- |
| 211 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | Year | -NaN- | -NaN- | Years | -NaN- | True | 1 | False | 2 | YEAR([Date]) |
| 212 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | MonthNo | -NaN- | -NaN- | MonthOfYear | -NaN- | True | 1 | False | 2 | MONTH([Date]) |
| 213 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | Month | -NaN- | -NaN- | Months | -NaN- | True | 1 | False | 2 | FORMAT([Date], "MMMM") |
| 214 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | QuarterNo | -NaN- | -NaN- | QuarterOfYear | -NaN- | True | 1 | False | 2 | INT(([MonthNo] + 2) / 3) |
| 215 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | Quarter | -NaN- | -NaN- | Quarters | -NaN- | True | 1 | False | 2 | "Qtr " & [QuarterNo] |
| 216 | LocalDateTable_d1146ef7-6f90-4647-b97e-2ffae90ba854 | Day | -NaN- | -NaN- | DayOfMonth | -NaN- | True | 1 | False | 2 | DAY([Date]) |
| 193 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 218 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | -NaN- | [Date] | -NaN- | PaddedDateTableDates | -NaN- | True | 1 | False | 4 | -NaN- |
| 219 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | Year | -NaN- | -NaN- | Years | -NaN- | True | 1 | False | 2 | YEAR([Date]) |
| 220 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | MonthNo | -NaN- | -NaN- | MonthOfYear | -NaN- | True | 1 | False | 2 | MONTH([Date]) |
| 221 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | Month | -NaN- | -NaN- | Months | -NaN- | True | 1 | False | 2 | FORMAT([Date], "MMMM") |
| 222 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | QuarterNo | -NaN- | -NaN- | QuarterOfYear | -NaN- | True | 1 | False | 2 | INT(([MonthNo] + 2) / 3) |
| 223 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | Quarter | -NaN- | -NaN- | Quarters | -NaN- | True | 1 | False | 2 | "Qtr " & [QuarterNo] |
| 224 | LocalDateTable_dc06deb5-c3da-486c-acde-3111d75ed696 | Day | -NaN- | -NaN- | DayOfMonth | -NaN- | True | 1 | False | 2 | DAY([Date]) |
| 573 | Product | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 575 | Product | ProductKey | ProductKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 576 | Product | SKU | SKU | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 577 | Product | Product | Product | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 578 | Product | Standard Cost | Standard Cost | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 579 | Product | Color | Color | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 580 | Product | List Price | List Price | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 581 | Product | Model | Model | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 582 | Product | Subcategory | Subcategory | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 583 | Product | Category | Category | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 3742 | Product | Sorting | -NaN- | -NaN- | -NaN- | -NaN- | False | 1 | False | 2 | RELATED('Table'[Sorting]) |
| 691 | Reseller | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 693 | Reseller | ResellerKey | ResellerKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 694 | Reseller | Reseller ID | Reseller ID | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 695 | Reseller | Business Type | Business Type | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 696 | Reseller | Reseller | Reseller | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 697 | Reseller | City | City | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 698 | Reseller | State-Province | State-Province | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 699 | Reseller | Country-Region | Country-Region | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 700 | Reseller | Postal Code | Postal Code | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 806 | Sales | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 808 | Sales | SalesOrderLineKey | SalesOrderLineKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 809 | Sales | ResellerKey | ResellerKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 810 | Sales | CustomerKey | CustomerKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 811 | Sales | ProductKey | ProductKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 812 | Sales | OrderDateKey | OrderDateKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 813 | Sales | DueDateKey | DueDateKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 814 | Sales | ShipDateKey | ShipDateKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 815 | Sales | SalesTerritoryKey | SalesTerritoryKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 816 | Sales | Order Quantity | Order Quantity | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 817 | Sales | Unit Price | Unit Price | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 818 | Sales | Extended Amount | Extended Amount | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 819 | Sales | Unit Price Discount Pct | Unit Price Discount Pct | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 820 | Sales | Product Standard Cost | Product Standard Cost | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 821 | Sales | Total Product Cost | Total Product Cost | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 822 | Sales | Sales Amount | Sales Amount | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 981 | Sales Order | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 983 | Sales Order | Channel | Channel | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 984 | Sales Order | SalesOrderLineKey | SalesOrderLineKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 985 | Sales Order | Sales Order | Sales Order | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 986 | Sales Order | Sales Order Line | Sales Order Line | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 1079 | Sales Territory | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 1081 | Sales Territory | SalesTerritoryKey | SalesTerritoryKey | -NaN- | -NaN- | -NaN- | True | 1 | False | 1 | -NaN- |
| 1082 | Sales Territory | Region | Region | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 1083 | Sales Territory | Country | Country | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 1084 | Sales Territory | Group | Group | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 3643 | Table | RowNumber-2662979B-1795-4F74-8F37-6A1BA8059B61 | -NaN- | -NaN- | -NaN- | -NaN- | True | 1 | True | 3 | -NaN- |
| 3645 | Table | Category | Category | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |
| 3646 | Table | Sorting | Sorting | -NaN- | -NaN- | -NaN- | False | 1 | False | 1 | -NaN- |



----

----
<p align="center">
Generated at 26.11.2023 21:58:58 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 1c33f12
</p>