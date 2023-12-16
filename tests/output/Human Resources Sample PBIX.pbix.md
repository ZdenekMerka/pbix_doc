----

[Home](./index.md) > [Human Resources Sample PBIX.pbix](Human Resources Sample PBIX.pbix.md)

[Information](#information) | [Model information](#model-information) | [Model relationships](#model-relationships) | [Report sections](#report-sections) | [Business objects](#business-objects) | [Measures](#measures) | [Relationships](#relationships) | [Hierarchies](#hierarchies) | [Columns](#columns) | 

----

# Information

Documentation for file **Human Resources Sample PBIX.pbix**.

# Model information


| Param  | Value  |
|---|---|
| **Analyzed pbix file name** | `Human Resources Sample PBIX.pbix` | 
| **Catalog name** | `85041eff-6bac-4193-bac4-4762ed6268a8` | 
| **Port** | `61172`|
| **Description** | `-NaN-` | 
| **Date modified** | `2022-09-22T23:04:12` | 
| **Compatibility level** | `1550` | 


[Up](#)
# Model relationships

```mermaid
graph LR;

id22(["Date[Date]"]) --> id25(["Employee[date]"])
id13(["FP[FP]"]) --> id25(["Employee[FP]"])
id28(["Ethnicity[Ethnic Group]"]) --> id25(["Employee[EthnicGroup]"])
id31(["Gender[ID]"]) --> id25(["Employee[Gender]"])
id16(["PayType[PayTypeID]"]) --> id25(["Employee[PayTypeID]"])
id10(["BU[BU]"]) --> id25(["Employee[BU]"])
id34(["AgeGroup[AgeGroupID]"]) --> id25(["Employee[AgeGroupID]"])
id19(["SeparationReason[SeparationTypeID]"]) --> id25(["Employee[TermReason]"])
id2041(["LocalDateTable_6f19f..(51)[-NaN-]"]) --> id22(["Date[Date]"])
id2044(["LocalDateTable_d2ea5..(51)[-NaN-]"]) --> id22(["Date[MonthStartDate]"])
id2047(["LocalDateTable_c9dde..(51)[-NaN-]"]) --> id22(["Date[MonthEndDate]"])
id2050(["LocalDateTable_cc28e..(51)[-NaN-]"]) --> id25(["Employee[TermDate]"])
id2053(["LocalDateTable_c04ce..(51)[-NaN-]"]) --> id25(["Employee[HireDate]"])
```



[Up](#)

# Report sections

## Info

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection1` |
| **Display Name** | `Info` |
| **Filters** | `[]` |
| **Ordinal** | `0` |
| **Visual containers number** | `2` |

[Up](#)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## New Hires

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection2` |
| **Display Name** | `New Hires` |
| **Filters** | `[{"name":"Filter","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Year"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Year"}},"Right":{"Literal":{"Value":"2014L"}}}}}]},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter1","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Month"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Month"}},"Right":{"Literal":{"Value":"'Dec'"}}}}}}}]},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter2","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"FP"}},"Property":"FPDesc"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter3","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Ethnicity"}},"Property":"Ethnicity"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter4","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"AgeGroup"}},"Property":"AgeGroup"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter5","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"BU"}},"Property":"Region"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter6","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"BU"}},"Property":"VP"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter7","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Gender"}},"Property":"Gender"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false}]` |
| **Ordinal** | `1` |
| **Visual containers number** | `9` |

[Up](#)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Date, FP, Employee` | 
| **Attributes:**  | Column: Date.Month<br/> Column: FP.FPDesc<br/> Measure: Employee.New Hires | 

[Up](#)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `lineClusteredColumnComboChart` |
| **Business objects:**  | `Date, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: Employee.New Hires<br/> Measure: Employee.New Hires SPLY<br/> Measure: Employee.Actives YoY % Change | 

[Up](#)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `AgeGroup, Employee` | 
| **Attributes:**  | Column: AgeGroup.AgeGroup<br/> Measure: Employee.New Hires | 

[Up](#)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer6 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer6` |
| **Type:** | `lineStackedColumnComboChart` |
| **Business objects:**  | `BU, Ethnicity, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: Ethnicity.Ethnicity<br/> Measure: Employee.New Hires<br/> Measure: Employee.Actives | 

[Up](#)




### Container VisualContainer7 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer8 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## Actives and Separations

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection3` |
| **Display Name** | `Actives and Separations` |
| **Filters** | `[{"name":"Filter","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Year"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Year"}},"Right":{"Literal":{"Value":"2014L"}}}}}]},"type":"Categorical","howCreated":1},{"name":"Filter1","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Month"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Month"}},"Right":{"Literal":{"Value":"'Dec'"}}}}}}}]},"type":"Categorical","howCreated":1},{"name":"Filter2","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"SeparationReason"}},"Property":"SeparationReason"}},"type":"Categorical","howCreated":1},{"name":"Filter3","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"BU"}},"Property":"Region"}},"type":"Categorical","howCreated":1},{"name":"Filter4","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"BU"}},"Property":"VP"}},"type":"Categorical","howCreated":1},{"name":"Filter5","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"AgeGroup"}},"Property":"AgeGroup"}},"type":"Categorical","howCreated":1},{"name":"Filter6","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Ethnicity"}},"Property":"Ethnicity"}},"type":"Categorical","howCreated":1},{"name":"Filter7","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Gender"}},"Property":"Gender"}},"type":"Categorical","howCreated":1},{"name":"Filter8","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"FP"}},"Property":"FPDesc"}},"type":"Categorical","howCreated":1}]` |
| **Ordinal** | `2` |
| **Visual containers number** | `11` |

[Up](#)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `lineClusteredColumnComboChart` |
| **Business objects:**  | `Date, BU, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: select2<br/> Measure: Employee.Actives<br/> Measure: Employee.Actives SPLY<br/> Measure: Employee.Seps YoY % Change | 

[Up](#)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `pieChart` |
| **Business objects:**  | `AgeGroup, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `BU, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Measure: Employee.Actives YoY Var | 

[Up](#)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer6 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer6` |
| **Type:** | `lineClusteredColumnComboChart` |
| **Business objects:**  | `Date, BU, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: select2<br/> Measure: Employee.Seps<br/> Measure: Employee.Seps SPLY<br/> Measure: Employee.Actives YoY % Change | 

[Up](#)




### Container VisualContainer7 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer7` |
| **Type:** | `barChart` |
| **Business objects:**  | `SeparationReason, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#)




### Container VisualContainer8 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer9 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer9` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Employee, Date` | 
| **Attributes:**  | Measure: Employee.Seps<br/> Measure: Employee.Seps SPLY<br/> Column: Date.Month | 

[Up](#)




### Container VisualContainer10 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer10` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Employee, Date` | 
| **Attributes:**  | Measure: Employee.Seps<br/> Measure: Employee.Seps SPLY<br/> Column: Date.Month | 

[Up](#)


## Bad Hires

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection` |
| **Display Name** | `Bad Hires` |
| **Filters** | `[{"name":"Filter","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Year"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Year"}},"Right":{"Literal":{"Value":"2014L"}}}}}]},"type":"Advanced","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter1","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Month"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Month"}},"Right":{"Literal":{"Value":"'Dec'"}}}}}}}]},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter2","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"AgeGroup"}},"Property":"AgeGroup"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter3","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"BU"}},"Property":"Region"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter4","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Ethnicity"}},"Property":"Ethnicity"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter5","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"FP"}},"Property":"FPDesc"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter6","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Gender"}},"Property":"Gender"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter7","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"SeparationReason"}},"Property":"SeparationReason"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false},{"name":"Filter8","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"BU"}},"Property":"VP"}},"type":"Categorical","howCreated":1,"isLinkedAsAggregation":false}]` |
| **Ordinal** | `3` |
| **Visual containers number** | `8` |

[Up](#)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `donutChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: Gender.Gender<br/> Aggregation: Sum(Employee.BadHires) | 

[Up](#)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Date, AgeGroup, Employee` | 
| **Attributes:**  | Column: select<br/> Column: AgeGroup.AgeGroup<br/> Measure: Employee.Bad Hires YoY % Change | 

[Up](#)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `columnChart` |
| **Business objects:**  | `BU, Ethnicity, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: select2<br/> Aggregation: select3 | 

[Up](#)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `Employee, AgeGroup` | 
| **Attributes:**  | Measure: Employee.BadHire%ofActives<br/> Column: AgeGroup.AgeGroup | 

[Up](#)




### Container VisualContainer6 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer6` |
| **Type:** | `slicer` |
| **Business objects:**  | `BU` | 
| **Attributes:**  | Column: BU.Region | 

[Up](#)




### Container VisualContainer7 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## New Hires Scorecard

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection4` |
| **Display Name** | `New Hires Scorecard` |
| **Filters** | `[{"name":"Filter","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Date"}},"Property":"Year"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Date","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":0,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Year"}},"Right":{"Literal":{"Value":"2014D"}}}}}]},"type":"Advanced","howCreated":1}]` |
| **Ordinal** | `4` |
| **Visual containers number** | `6` |

[Up](#)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `slicer` |
| **Business objects:**  | `BU` | 
| **Attributes:**  | Column: BU.VP | 

[Up](#)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Date, Employee` | 
| **Attributes:**  | Column: Date.Month<br/> Measure: Employee.New Hires | 

[Up](#)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Employee, PayType` | 
| **Attributes:**  | Measure: select1<br/> Column: PayType.PayType | 

[Up](#)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `clusteredColumnChart` |
| **Business objects:**  | `Employee, FP, AgeGroup` | 
| **Attributes:**  | Measure: Employee.New Hires<br/> Column: FP.FPDesc<br/> Column: AgeGroup.AgeGroup | 

[Up](#)






# Business objects

| ID | NAME | DESCRIPTION | 
|----|------|-------------|
| 10 | BU | n/a |
| 13 | FP | n/a |
| 16 | PayType | n/a |
| 19 | SeparationReason | n/a |
| 22 | Date | n/a |
| 28 | Ethnicity | n/a |
| 31 | Gender | n/a |
| 34 | AgeGroup | n/a |



[Up](#)
# Measures


<table>
    <tr>
        <th> ID </th><th> TABLE </th><th> NAME </th><th> DESCRIPTION </th><th> EXPRESSION </th><th> IS_HIDDEN </th><th> STATE </th>
    </tr>
<tr>
        <td> 49 </td><td> BU </td><td>  </td><td> n/a </td><td> <code> mid([RegionSeq], 3,15) </code></td><td> False </td><td>  1 </td> 
    </tr>
<tr>
        <td> 67 </td><td> Date </td><td>  </td><td> n/a </td><td> <code> ([Year]-MIN([Year]))*12 +[MonthNumber] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 75 </td><td> Employee </td><td>  </td><td> n/a </td><td> <code> IF(YEAR([date]) = YEAR([HireDate]) && MONTH([date])=MONTH([HireDate]), 1) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 80 </td><td> Employee </td><td>  </td><td> n/a </td><td> <code> IF([Age]<30, 1, IF([Age]<50, 2, 3)) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 81 </td><td> Employee </td><td>  </td><td> n/a </td><td> <code> IF([date]-[HireDate]<0,[HireDate]-[date],[date]-[HireDate]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 82 </td><td> Employee </td><td>  </td><td> n/a </td><td> <code> CEILING([TenureDays]/30, 1) -1 </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 83 </td><td> Employee </td><td>  </td><td> n/a </td><td> <code> IF(OR((([HireDate]-[TermDate])*-1)>=61,ISBLANK([TermDate])),0,1) </code></td><td> False </td><td>  1 </td> 
    </tr>
<tr>
        <td> 1959 </td><td> DateTableTemplate_92..(54) </td><td>  </td><td> n/a </td><td> <code> YEAR([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 1960 </td><td> DateTableTemplate_92..(54) </td><td>  </td><td> n/a </td><td> <code> MONTH([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 1961 </td><td> DateTableTemplate_92..(54) </td><td>  </td><td> n/a </td><td> <code> FORMAT([Date], "MMMM") </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 1962 </td><td> DateTableTemplate_92..(54) </td><td>  </td><td> n/a </td><td> <code> INT(([MonthNo] + 2) / 3) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 1963 </td><td> DateTableTemplate_92..(54) </td><td>  </td><td> n/a </td><td> <code> "Qtr " & [QuarterNo] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 1964 </td><td> DateTableTemplate_92..(54) </td><td>  </td><td> n/a </td><td> <code> DAY([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2062 </td><td> LocalDateTable_6f19f..(51) </td><td>  </td><td> n/a </td><td> <code> YEAR([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2063 </td><td> LocalDateTable_6f19f..(51) </td><td>  </td><td> n/a </td><td> <code> MONTH([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2064 </td><td> LocalDateTable_6f19f..(51) </td><td>  </td><td> n/a </td><td> <code> FORMAT([Date], "MMMM") </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2065 </td><td> LocalDateTable_6f19f..(51) </td><td>  </td><td> n/a </td><td> <code> INT(([MonthNo] + 2) / 3) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2066 </td><td> LocalDateTable_6f19f..(51) </td><td>  </td><td> n/a </td><td> <code> "Qtr " & [QuarterNo] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2067 </td><td> LocalDateTable_6f19f..(51) </td><td>  </td><td> n/a </td><td> <code> DAY([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2069 </td><td> LocalDateTable_d2ea5..(51) </td><td>  </td><td> n/a </td><td> <code> YEAR([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2070 </td><td> LocalDateTable_d2ea5..(51) </td><td>  </td><td> n/a </td><td> <code> MONTH([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2071 </td><td> LocalDateTable_d2ea5..(51) </td><td>  </td><td> n/a </td><td> <code> FORMAT([Date], "MMMM") </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2072 </td><td> LocalDateTable_d2ea5..(51) </td><td>  </td><td> n/a </td><td> <code> INT(([MonthNo] + 2) / 3) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2073 </td><td> LocalDateTable_d2ea5..(51) </td><td>  </td><td> n/a </td><td> <code> "Qtr " & [QuarterNo] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2074 </td><td> LocalDateTable_d2ea5..(51) </td><td>  </td><td> n/a </td><td> <code> DAY([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2076 </td><td> LocalDateTable_c9dde..(51) </td><td>  </td><td> n/a </td><td> <code> YEAR([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2077 </td><td> LocalDateTable_c9dde..(51) </td><td>  </td><td> n/a </td><td> <code> MONTH([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2078 </td><td> LocalDateTable_c9dde..(51) </td><td>  </td><td> n/a </td><td> <code> FORMAT([Date], "MMMM") </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2079 </td><td> LocalDateTable_c9dde..(51) </td><td>  </td><td> n/a </td><td> <code> INT(([MonthNo] + 2) / 3) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2080 </td><td> LocalDateTable_c9dde..(51) </td><td>  </td><td> n/a </td><td> <code> "Qtr " & [QuarterNo] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2081 </td><td> LocalDateTable_c9dde..(51) </td><td>  </td><td> n/a </td><td> <code> DAY([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2083 </td><td> LocalDateTable_cc28e..(51) </td><td>  </td><td> n/a </td><td> <code> YEAR([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2084 </td><td> LocalDateTable_cc28e..(51) </td><td>  </td><td> n/a </td><td> <code> MONTH([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2085 </td><td> LocalDateTable_cc28e..(51) </td><td>  </td><td> n/a </td><td> <code> FORMAT([Date], "MMMM") </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2086 </td><td> LocalDateTable_cc28e..(51) </td><td>  </td><td> n/a </td><td> <code> INT(([MonthNo] + 2) / 3) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2087 </td><td> LocalDateTable_cc28e..(51) </td><td>  </td><td> n/a </td><td> <code> "Qtr " & [QuarterNo] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2088 </td><td> LocalDateTable_cc28e..(51) </td><td>  </td><td> n/a </td><td> <code> DAY([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2090 </td><td> LocalDateTable_c04ce..(51) </td><td>  </td><td> n/a </td><td> <code> YEAR([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2091 </td><td> LocalDateTable_c04ce..(51) </td><td>  </td><td> n/a </td><td> <code> MONTH([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2092 </td><td> LocalDateTable_c04ce..(51) </td><td>  </td><td> n/a </td><td> <code> FORMAT([Date], "MMMM") </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2093 </td><td> LocalDateTable_c04ce..(51) </td><td>  </td><td> n/a </td><td> <code> INT(([MonthNo] + 2) / 3) </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2094 </td><td> LocalDateTable_c04ce..(51) </td><td>  </td><td> n/a </td><td> <code> "Qtr " & [QuarterNo] </code></td><td> True </td><td>  1 </td> 
    </tr>
<tr>
        <td> 2095 </td><td> LocalDateTable_c04ce..(51) </td><td>  </td><td> n/a </td><td> <code> DAY([Date]) </code></td><td> True </td><td>  1 </td> 
    </tr>
</table>




[Up](#)
# Relationships 


| ID | FROM_TABLE | TO_TABLE | FROM:TO CARDINALITY | NAME | IS_ACTIVE  |
|----|------------|----------|---------------------|------|------------|
| 37 | Employee[date] | Date[Date] | 2:1 | 7ddd41c5-a1f5-477b-9712-84fdc7313c7d | True |
| 38 | Employee[FP] | FP[FP] | 2:1 | 497871a2-f5e1-40ff-90d7-6f980ca1119a | True |
| 39 | Employee[EthnicGroup] | Ethnicity[Ethnic Group] | 2:1 | 20c07ef2-2c50-4fd4-ad56-8b0e0e36ddc4 | True |
| 40 | Employee[Gender] | Gender[ID] | 2:1 | 539493ca-f3e3-4c1f-b14e-54cba661f036 | True |
| 41 | Employee[PayTypeID] | PayType[PayTypeID] | 2:1 | 7c262a8a-d56f-4c97-95db-c0f56177e4cd | True |
| 42 | Employee[BU] | BU[BU] | 2:1 | edfe54b9-43d8-4c14-a29d-f17ddb0dd421 | True |
| 43 | Employee[AgeGroupID] | AgeGroup[AgeGroupID] | 2:1 | 35cbfa94-d30d-4da9-8fb6-e7d469edb9bb | True |
| 44 | Employee[TermReason] | SeparationReason[SeparationTypeID] | 2:1 | 1c53ee81-f20a-40a6-a5bd-97e57652fc88 | True |
| 2056 | Date[Date] | LocalDateTable_6f19f..(51)[-NaN-] | 2:1 | 0f809af4-d31b-4977-a214-8f13fa42f41d | True |
| 2057 | Date[MonthStartDate] | LocalDateTable_d2ea5..(51)[-NaN-] | 2:1 | f496f9ad-5665-4785-a30e-b1bbcf7be215 | True |
| 2058 | Date[MonthEndDate] | LocalDateTable_c9dde..(51)[-NaN-] | 2:1 | b2a9d346-0212-432d-a1a9-57680b4a73ea | True |
| 2059 | Employee[TermDate] | LocalDateTable_cc28e..(51)[-NaN-] | 2:1 | e020e64e-e74a-4b8f-bed8-e879143ea6d8 | True |
| 2060 | Employee[HireDate] | LocalDateTable_c04ce..(51)[-NaN-] | 2:1 | 3e454a13-2d74-4769-b44d-91ce492acf1a | True |


[Up](#)
# Hierarchies 



| ID | TABLE | NAME | DESCRIPTION  | IS_HIDDEN | 
|----|----------|------|--------------|-----------|
| 130 |Date | YQM | n/a | False | 
| 1966 |DateTableTemplate_92..(54) | Date Hierarchy | n/a | False | 
| 2101 |LocalDateTable_6f19f..(51) | Date Hierarchy | n/a | False | 
| 2102 |LocalDateTable_d2ea5..(51) | Date Hierarchy | n/a | False | 
| 2103 |LocalDateTable_c9dde..(51) | Date Hierarchy | n/a | False | 
| 2104 |LocalDateTable_cc28e..(51) | Date Hierarchy | n/a | False | 
| 2105 |LocalDateTable_c04ce..(51) | Date Hierarchy | n/a | False | 


[Up](#)
# Columns 


<table>
    <tr>
        <th> ID </th><th> TABLE </th><th> EXPLICIT_NAME </th><th> DESCRIPTION </th><th> IS_HIDDEN </th><th> EXPRESSION </th>
    </tr>
<tr>
        <td> 46 </td><td> BU </td><td> BU </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 47 </td><td> BU </td><td> RegionSeq </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 48 </td><td> BU </td><td> VP </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 49 </td><td> BU </td><td> Region </td><td> n/a </td><td> False </td><td><code> mid([RegionSeq], 3,15) </code></td>
    </tr>

<tr>
        <td> 50 </td><td> FP </td><td> FP </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 51 </td><td> FP </td><td> FPDesc </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 53 </td><td> PayType </td><td> PayType </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 55 </td><td> SeparationReason </td><td> SeparationReason </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 56 </td><td> Date </td><td> Date </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 57 </td><td> Date </td><td> Month </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 58 </td><td> Date </td><td> MonthNumber </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 59 </td><td> Date </td><td> Period </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 60 </td><td> Date </td><td> PeriodNumber </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 61 </td><td> Date </td><td> Qtr </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 62 </td><td> Date </td><td> QtrNumber </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 63 </td><td> Date </td><td> Year </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 64 </td><td> Date </td><td> Day </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 65 </td><td> Date </td><td> MonthStartDate </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 66 </td><td> Date </td><td> MonthEndDate </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 83 </td><td> Employee </td><td> BadHires </td><td> n/a </td><td> False </td><td><code> IF(OR((([HireDate]-[TermDate])*-1)>=61,ISBLANK([TermDate])),0,1) </code></td>
    </tr>

<tr>
        <td> 85 </td><td> Ethnicity </td><td> Ethnicity </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 87 </td><td> Gender </td><td> Gender </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

<tr>
        <td> 90 </td><td> AgeGroup </td><td> AgeGroup </td><td> n/a </td><td> False </td><td><code> n/a </code></td>
    </tr>

</table>




----
<p align="center">
Generated at 16.12.2023 21:03:43 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 63f5c8f
</p>