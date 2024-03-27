----

[Home](./index.md) > [Human Resources Sample PBIX.pbix](Human%20Resources%20Sample%20PBIX.pbix_report.md)

| [Report sections](#report-sections) |

----


# Report sections

## Info

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection1` |
| **Display Name** | `Info` |
| **Filters** |  |
| **Ordinal** | `0` |
| **Visual containers number** | `2` |

[Up](#report-sections)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## New Hires

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection2` |
| **Display Name** | `New Hires` |
| **Filters** | Name: `Filter` Type: `Categorical` Column: `Date.Year` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Year\"}}, \"Right\": {\"Literal\": {\"Value\": \"2014L\"}}}}}]}"')<br/>Name: `Filter1` Type: `Categorical` Column: `Date.Month` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Not\": {\"Expression\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Month\"}}, \"Right\": {\"Literal\": {\"Value\": \"\'Dec\'\"}}}}}}}]}"')<br/>Name: `Filter2` Type: `Categorical` Column: `FP.FPDesc` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"FP\"}}, \"Property\": \"FPDesc\"}}"')<br/>Name: `Filter3` Type: `Categorical` Column: `Ethnicity.Ethnicity` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Ethnicity\"}}, \"Property\": \"Ethnicity\"}}"')<br/>Name: `Filter4` Type: `Categorical` Column: `AgeGroup.AgeGroup` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"AgeGroup\"}}, \"Property\": \"AgeGroup\"}}"')<br/>Name: `Filter5` Type: `Categorical` Column: `BU.Region` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"BU\"}}, \"Property\": \"Region\"}}"')<br/>Name: `Filter6` Type: `Categorical` Column: `BU.VP` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"BU\"}}, \"Property\": \"VP\"}}"')<br/>Name: `Filter7` Type: `Categorical` Column: `Gender.Gender` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Gender\"}}, \"Property\": \"Gender\"}}"') |
| **Ordinal** | `1` |
| **Visual containers number** | `9` |

[Up](#report-sections)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Date, FP, Employee` | 
| **Attributes:**  | Column: Date.Month<br/> Column: FP.FPDesc<br/> Measure: Employee.New Hires | 

[Up](#report-sections)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `lineClusteredColumnComboChart` |
| **Business objects:**  | `Date, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: Employee.New Hires<br/> Measure: Employee.New Hires SPLY<br/> Measure: Employee.Actives YoY % Change | 

[Up](#report-sections)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#report-sections)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `AgeGroup, Employee` | 
| **Attributes:**  | Column: AgeGroup.AgeGroup<br/> Measure: Employee.New Hires | 

[Up](#report-sections)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer6 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer6` |
| **Type:** | `lineStackedColumnComboChart` |
| **Business objects:**  | `BU, Ethnicity, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: Ethnicity.Ethnicity<br/> Measure: Employee.New Hires<br/> Measure: Employee.Actives | 

[Up](#report-sections)




### Container VisualContainer7 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer8 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Actives and Separations

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection3` |
| **Display Name** | `Actives and Separations` |
| **Filters** | Name: `Filter` Type: `Categorical` Column: `Date.Year` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Year\"}}, \"Right\": {\"Literal\": {\"Value\": \"2014L\"}}}}}]}"')<br/>Name: `Filter1` Type: `Categorical` Column: `Date.Month` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Not\": {\"Expression\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Month\"}}, \"Right\": {\"Literal\": {\"Value\": \"\'Dec\'\"}}}}}}}]}"')<br/>Name: `Filter2` Type: `Categorical` Column: `SeparationReason.SeparationReason` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"SeparationReason\"}}, \"Property\": \"SeparationReason\"}}"')<br/>Name: `Filter3` Type: `Categorical` Column: `BU.Region` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"BU\"}}, \"Property\": \"Region\"}}"')<br/>Name: `Filter4` Type: `Categorical` Column: `BU.VP` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"BU\"}}, \"Property\": \"VP\"}}"')<br/>Name: `Filter5` Type: `Categorical` Column: `AgeGroup.AgeGroup` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"AgeGroup\"}}, \"Property\": \"AgeGroup\"}}"')<br/>Name: `Filter6` Type: `Categorical` Column: `Ethnicity.Ethnicity` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Ethnicity\"}}, \"Property\": \"Ethnicity\"}}"')<br/>Name: `Filter7` Type: `Categorical` Column: `Gender.Gender` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Gender\"}}, \"Property\": \"Gender\"}}"')<br/>Name: `Filter8` Type: `Categorical` Column: `FP.FPDesc` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"FP\"}}, \"Property\": \"FPDesc\"}}"') |
| **Ordinal** | `2` |
| **Visual containers number** | `11` |

[Up](#report-sections)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `lineClusteredColumnComboChart` |
| **Business objects:**  | `Date, BU, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: select2<br/> Measure: Employee.Actives<br/> Measure: Employee.Actives SPLY<br/> Measure: Employee.Seps YoY % Change | 

[Up](#report-sections)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#report-sections)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `pieChart` |
| **Business objects:**  | `AgeGroup, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#report-sections)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `BU, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Measure: Employee.Actives YoY Var | 

[Up](#report-sections)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer6 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer6` |
| **Type:** | `lineClusteredColumnComboChart` |
| **Business objects:**  | `Date, BU, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: select2<br/> Measure: Employee.Seps<br/> Measure: Employee.Seps SPLY<br/> Measure: Employee.Actives YoY % Change | 

[Up](#report-sections)




### Container VisualContainer7 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer7` |
| **Type:** | `barChart` |
| **Business objects:**  | `SeparationReason, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#report-sections)




### Container VisualContainer8 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer9 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer9` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Employee, Date` | 
| **Attributes:**  | Measure: Employee.Seps<br/> Measure: Employee.Seps SPLY<br/> Column: Date.Month | 

[Up](#report-sections)




### Container VisualContainer10 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer10` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Employee, Date` | 
| **Attributes:**  | Measure: Employee.Seps<br/> Measure: Employee.Seps SPLY<br/> Column: Date.Month | 

[Up](#report-sections)


## Bad Hires

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection` |
| **Display Name** | `Bad Hires` |
| **Filters** | Name: `Filter` Type: `Advanced` Column: `Date.Year` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Year\"}}, \"Right\": {\"Literal\": {\"Value\": \"2014L\"}}}}}]}"')<br/>Name: `Filter1` Type: `Categorical` Column: `Date.Month` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Not\": {\"Expression\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Month\"}}, \"Right\": {\"Literal\": {\"Value\": \"\'Dec\'\"}}}}}}}]}"')<br/>Name: `Filter2` Type: `Categorical` Column: `AgeGroup.AgeGroup` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"AgeGroup\"}}, \"Property\": \"AgeGroup\"}}"')<br/>Name: `Filter3` Type: `Categorical` Column: `BU.Region` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"BU\"}}, \"Property\": \"Region\"}}"')<br/>Name: `Filter4` Type: `Categorical` Column: `Ethnicity.Ethnicity` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Ethnicity\"}}, \"Property\": \"Ethnicity\"}}"')<br/>Name: `Filter5` Type: `Categorical` Column: `FP.FPDesc` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"FP\"}}, \"Property\": \"FPDesc\"}}"')<br/>Name: `Filter6` Type: `Categorical` Column: `Gender.Gender` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Gender\"}}, \"Property\": \"Gender\"}}"')<br/>Name: `Filter7` Type: `Categorical` Column: `SeparationReason.SeparationReason` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"SeparationReason\"}}, \"Property\": \"SeparationReason\"}}"')<br/>Name: `Filter8` Type: `Categorical` Column: `BU.VP` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"BU\"}}, \"Property\": \"VP\"}}"') |
| **Ordinal** | `3` |
| **Visual containers number** | `8` |

[Up](#report-sections)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `donutChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: Gender.Gender<br/> Aggregation: Sum(Employee.BadHires) | 

[Up](#report-sections)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Date, AgeGroup, Employee` | 
| **Attributes:**  | Column: select<br/> Column: AgeGroup.AgeGroup<br/> Measure: Employee.Bad Hires YoY % Change | 

[Up](#report-sections)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `columnChart` |
| **Business objects:**  | `BU, Ethnicity, Employee` | 
| **Attributes:**  | Column: select<br/> Column: select1<br/> Column: select2<br/> Aggregation: select3 | 

[Up](#report-sections)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `waterfallChart` |
| **Business objects:**  | `Employee, AgeGroup` | 
| **Attributes:**  | Measure: Employee.BadHire%ofActives<br/> Column: AgeGroup.AgeGroup | 

[Up](#report-sections)




### Container VisualContainer6 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer6` |
| **Type:** | `slicer` |
| **Business objects:**  | `BU` | 
| **Attributes:**  | Column: BU.Region | 

[Up](#report-sections)




### Container VisualContainer7 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## New Hires Scorecard

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection4` |
| **Display Name** | `New Hires Scorecard` |
| **Filters** | Name: `Filter` Type: `Advanced` Column: `Date.Year` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Date\", \"Name\": \"d\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Comparison\": {\"ComparisonKind\": 0, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"d\"}}, \"Property\": \"Year\"}}, \"Right\": {\"Literal\": {\"Value\": \"2014D\"}}}}}]}"') |
| **Ordinal** | `4` |
| **Visual containers number** | `6` |

[Up](#report-sections)



### Container VisualContainer 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container VisualContainer1 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer1` |
| **Type:** | `slicer` |
| **Business objects:**  | `BU` | 
| **Attributes:**  | Column: BU.VP | 

[Up](#report-sections)




### Container VisualContainer2 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer2` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Date, Employee` | 
| **Attributes:**  | Column: Date.Month<br/> Measure: Employee.New Hires | 

[Up](#report-sections)




### Container VisualContainer3 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer3` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Gender, Employee` | 
| **Attributes:**  | Column: select<br/> Measure: select1 | 

[Up](#report-sections)




### Container VisualContainer4 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer4` |
| **Type:** | `pieChart` |
| **Business objects:**  | `Employee, PayType` | 
| **Attributes:**  | Measure: select1<br/> Column: PayType.PayType | 

[Up](#report-sections)




### Container VisualContainer5 

| Param  | Value  |
|---|---|
| **Name:** | `VisualContainer5` |
| **Type:** | `clusteredColumnChart` |
| **Business objects:**  | `Employee, FP, AgeGroup` | 
| **Attributes:**  | Measure: Employee.New Hires<br/> Column: FP.FPDesc<br/> Column: AgeGroup.AgeGroup | 

[Up](#report-sections)







----
<p align="center">
Generated at 27.03.2024 12:50:21 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 
</p>