----

[Home](../home.md) > [AdventureWorks_Sales2.pbix](AdventureWorks_Sales2.pbix.md)

[Information](#information) | [Model information](#model-information) | [Model relationships](#model-relationships) | [Business objects](#business-objects) | [Measures](#measures) | [Relationships](#relationships) | [Hierarchies](#hierarchies) | [Columns](#columns) | 

----

# Information

Documentation for file **AdventureWorks_Sales2.pbix**.

# Model information


| Param  | Value  |
|---|---|
| **Analyzed pbix file name** | `AdventureWorks_Sales2.pbix` | 
| **Catalog name** | `418255b2-96be-4dcd-9ddd-0a2ecea747a0` | 
| **Port** | `61006`|
| **Description** | `-NaN-` | 
| **Date modified** | `2023-11-22T21:37:51` | 
| **Compatibility level** | `1567` | 


[Up](#)
# Model relationships

```mermaid
graph LR;

id186(["LocalDateTable_1635a..(51)[-NaN-]"]) --> id183(["Date[Date]"])
id189(["LocalDateTable_d1146..(51)[-NaN-]"]) --> id183(["Date[Month]"])
id192(["LocalDateTable_dc06d..(51)[-NaN-]"]) --> id183(["Date[Full Date]"])
id12(["Customer[CustomerKey]"]) --> id805(["Sales[CustomerKey]"])
id572(["Product[ProductKey]"]) --> id805(["Sales[ProductKey]"])
id690(["Reseller[ResellerKey]"]) --> id805(["Sales[ResellerKey]"])
id805(["Sales[SalesOrderLineKey]"]) --> id980(["Sales Order[SalesOrderLineKey]"])
id1078(["Sales Territory[SalesTerritoryKey]"]) --> id805(["Sales[SalesTerritoryKey]"])
id183(["Date[DateKey]"]) --> id805(["Sales[OrderDateKey]"])
id3642(["Table[Category]"]) --> id572(["Product[Category]"])
```



[Up](#)

# Report sections

## Page 1

| Param  | Value  |
|---|---|
| **ID** | 0 |
| **Name** | ReportSection |
| **Display Name** | Page 1 |
| **Filters** | [] |
| **Ordinal** | 0 |
| **Visual containers number** | 6 |

### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



## Page 2

| Param  | Value  |
|---|---|
| **ID** |  |
| **Name** | ReportSection350b6b55132e00f8ba89 |
| **Display Name** | Page 2 |
| **Filters** | [] |
| **Ordinal** | 1 |
| **Visual containers number** | 1 |

### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



## Page 3

| Param  | Value  |
|---|---|
| **ID** |  |
| **Name** | ReportSectiona113e22f3ad54b8397d8 |
| **Display Name** | Page 3 |
| **Filters** | [] |
| **Ordinal** | 2 |
| **Visual containers number** | 1 |

### Container 

| Param  | Value  |
|---|---|
| **x** | <class 'jinja2.runtime.Undefined'> |
| **y** | <class 'jinja2.runtime.Undefined'> |
| **z** | <class 'jinja2.runtime.Undefined'> |
| **width** | <class 'int'> |
| **height** | <class 'int'> |
| **config** | <class 'type'> |
| **filters** | <class 'str'> |
| **query** | <class 'type'> |
| **dataTransforms** | <class 'jinja2.runtime.Undefined'> |



























# Business objects

| ID | NAME | DESCRIPTION | 
|----|------|-------------|
| 12 | Customer | n/a |
| 183 | Date | n/a |
| 572 | Product | n/a |
| 690 | Reseller | n/a |
| 805 | Sales | n/a |
| 980 | Sales Order | n/a |
| 1078 | Sales Territory | n/a |
| 3642 | Table | n/a |



[Up](#)
# Measures


| ID | TABLE | NAME | DESCRIPTION | EXPRESSION | IS_HIDDEN | STATE |
|----|-------|------|-------------|------------|-----------|-------|
| 19 | DateTableTemplate_78..(54) |  | n/a | YEAR([Date]) | True |  1 |  
| 20 | DateTableTemplate_78..(54) |  | n/a | MONTH([Date]) | True |  1 |  
| 21 | DateTableTemplate_78..(54) |  | n/a | FORMAT([Date], "MMMM") | True |  1 |  
| 22 | DateTableTemplate_78..(54) |  | n/a | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 23 | DateTableTemplate_78..(54) |  | n/a | "Qtr " & [QuarterNo] | True |  1 |  
| 24 | DateTableTemplate_78..(54) |  | n/a | DAY([Date]) | True |  1 |  
| 201 | LocalDateTable_1635a..(51) |  | n/a | YEAR([Date]) | True |  1 |  
| 202 | LocalDateTable_1635a..(51) |  | n/a | MONTH([Date]) | True |  1 |  
| 203 | LocalDateTable_1635a..(51) |  | n/a | FORMAT([Date], "MMMM") | True |  1 |  
| 204 | LocalDateTable_1635a..(51) |  | n/a | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 205 | LocalDateTable_1635a..(51) |  | n/a | "Qtr " & [QuarterNo] | True |  1 |  
| 206 | LocalDateTable_1635a..(51) |  | n/a | DAY([Date]) | True |  1 |  
| 211 | LocalDateTable_d1146..(51) |  | n/a | YEAR([Date]) | True |  1 |  
| 212 | LocalDateTable_d1146..(51) |  | n/a | MONTH([Date]) | True |  1 |  
| 213 | LocalDateTable_d1146..(51) |  | n/a | FORMAT([Date], "MMMM") | True |  1 |  
| 214 | LocalDateTable_d1146..(51) |  | n/a | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 215 | LocalDateTable_d1146..(51) |  | n/a | "Qtr " & [QuarterNo] | True |  1 |  
| 216 | LocalDateTable_d1146..(51) |  | n/a | DAY([Date]) | True |  1 |  
| 219 | LocalDateTable_dc06d..(51) |  | n/a | YEAR([Date]) | True |  1 |  
| 220 | LocalDateTable_dc06d..(51) |  | n/a | MONTH([Date]) | True |  1 |  
| 221 | LocalDateTable_dc06d..(51) |  | n/a | FORMAT([Date], "MMMM") | True |  1 |  
| 222 | LocalDateTable_dc06d..(51) |  | n/a | INT(([MonthNo] + 2) / 3) | True |  1 |  
| 223 | LocalDateTable_dc06d..(51) |  | n/a | "Qtr " & [QuarterNo] | True |  1 |  
| 224 | LocalDateTable_dc06d..(51) |  | n/a | DAY([Date]) | True |  1 |  
| 3742 | Product |  | n/a | RELATED('Table'[Sorting]) | False |  1 |  


[Up](#)
# Relationships 


| ID | FROM_TABLE | TO_TABLE | FROM:TO CARDINALITY | NAME | IS_ACTIVE  |
|----|------------|----------|---------------------|------|------------|
| 195 | Date[Date] | LocalDateTable_1635a..(51)[-NaN-] | 2:1 | 88371ba8-2389-41b4-a22f-bcb756732d3b | True |
| 196 | Date[Month] | LocalDateTable_d1146..(51)[-NaN-] | 2:1 | 586c9eeb-fe2f-431d-a8c4-9723ce217f20 | True |
| 197 | Date[Full Date] | LocalDateTable_dc06d..(51)[-NaN-] | 2:1 | 401217e9-9553-4835-a527-fd574f68046d | True |
| 3224 | Sales[CustomerKey] | Customer[CustomerKey] | 2:1 | e3030baf-8c61-408d-a80e-04714277dcd3 | True |
| 3227 | Sales[ProductKey] | Product[ProductKey] | 2:1 | a0a78efb-3ce3-472a-993a-b92e31c0e3cd | True |
| 3230 | Sales[ResellerKey] | Reseller[ResellerKey] | 2:1 | 0ef2b150-bb90-4b8f-8537-fc236873591c | True |
| 3233 | Sales Order[SalesOrderLineKey] | Sales[SalesOrderLineKey] | 1:1 | 29b21f6a-77ef-4b3b-a0c0-e4111f87627b | True |
| 3238 | Sales[SalesTerritoryKey] | Sales Territory[SalesTerritoryKey] | 2:1 | cecf591c-1f02-44a6-bff1-1c753a0b4835 | True |
| 3305 | Sales[OrderDateKey] | Date[DateKey] | 2:1 | 8e31fd7b-1e63-43a9-8a47-33876ae8aed6 | True |
| 3322 | Sales[DueDateKey] | Date[DateKey] | 2:1 | dfb7bf63-667c-4abb-b494-7424c4e34b60 | False |
| 3339 | Sales[ShipDateKey] | Date[DateKey] | 2:1 | 6a63bfea-7b52-4e05-85f4-63a0f9b8991f | False |
| 3725 | Product[Category] | Table[Category] | 2:1 | 93a2e7c9-4a15-47be-93c0-06eceb139103 | True |


[Up](#)
# Hierarchies 



| ID | TABLE | NAME | DESCRIPTION  | IS_HIDDEN | 
|----|----------|------|--------------|-----------|
| 3356 |Customer | Geography | n/a | False | 
| 27 |DateTableTemplate_78..(54) | Date Hierarchy | n/a | False | 
| 3399 |Date | Fiscal | n/a | False | 
| 230 |LocalDateTable_1635a..(51) | Date Hierarchy | n/a | False | 
| 231 |LocalDateTable_d1146..(51) | Date Hierarchy | n/a | False | 
| 232 |LocalDateTable_dc06d..(51) | Date Hierarchy | n/a | False | 
| 3476 |Product | Products | n/a | False | 
| 3518 |Reseller | Geography | n/a | False | 
| 3561 |Sales Order | Sales Orders | n/a | False | 
| 3601 |Sales Territory | Sales Territories | n/a | False | 


[Up](#)
# Columns 


| ID | TABLE | EXPLICIT_NAME | DESCRIPTION | IS_HIDDEN | EXPRESSION |
|----|-------|---------------|-------------|-----------|------------|
| 114 | Customer | Customer ID | n/a | False | n/a |
| 115 | Customer | Customer | n/a | False | n/a |
| 116 | Customer | City | n/a | False | n/a |
| 117 | Customer | State-Province | n/a | False | n/a |
| 118 | Customer | Country-Region | n/a | False | n/a |
| 119 | Customer | Postal Code | n/a | False | n/a |
| 199 | Date | Date | n/a | False | n/a |
| 207 | Date | Fiscal Year | n/a | False | n/a |
| 208 | Date | Fiscal Quarter | n/a | False | n/a |
| 209 | Date | Month | n/a | False | n/a |
| 217 | Date | Full Date | n/a | False | n/a |
| 576 | Product | SKU | n/a | False | n/a |
| 577 | Product | Product | n/a | False | n/a |
| 578 | Product | Standard Cost | n/a | False | n/a |
| 579 | Product | Color | n/a | False | n/a |
| 580 | Product | List Price | n/a | False | n/a |
| 581 | Product | Model | n/a | False | n/a |
| 582 | Product | Subcategory | n/a | False | n/a |
| 583 | Product | Category | n/a | False | n/a |
| 3742 | Product | Sorting | n/a | False | RELATED('Table'[Sorting]) |
| 694 | Reseller | Reseller ID | n/a | False | n/a |
| 695 | Reseller | Business Type | n/a | False | n/a |
| 696 | Reseller | Reseller | n/a | False | n/a |
| 697 | Reseller | City | n/a | False | n/a |
| 698 | Reseller | State-Province | n/a | False | n/a |
| 699 | Reseller | Country-Region | n/a | False | n/a |
| 700 | Reseller | Postal Code | n/a | False | n/a |
| 816 | Sales | Order Quantity | n/a | False | n/a |
| 817 | Sales | Unit Price | n/a | False | n/a |
| 818 | Sales | Extended Amount | n/a | False | n/a |
| 819 | Sales | Unit Price Discount ..(23) | n/a | False | n/a |
| 820 | Sales | Product Standard Cos..(21) | n/a | False | n/a |
| 821 | Sales | Total Product Cost | n/a | False | n/a |
| 822 | Sales | Sales Amount | n/a | False | n/a |
| 983 | Sales Order | Channel | n/a | False | n/a |
| 985 | Sales Order | Sales Order | n/a | False | n/a |
| 986 | Sales Order | Sales Order Line | n/a | False | n/a |
| 1082 | Sales Territory | Region | n/a | False | n/a |
| 1083 | Sales Territory | Country | n/a | False | n/a |
| 1084 | Sales Territory | Group | n/a | False | n/a |
| 3645 | Table | Category | n/a | False | n/a |
| 3646 | Table | Sorting | n/a | False | n/a |



----
<p align="center">
Generated at 26.11.2023 23:51:20 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 74bb95a
</p>