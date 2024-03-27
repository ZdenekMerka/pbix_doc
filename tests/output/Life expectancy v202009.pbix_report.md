----

[Home](./index.md) > [Life expectancy v202009.pbix](Life%20expectancy%20v202009.pbix_report.md)

| [Report sections](#report-sections) |

----


# Report sections

## Life Expectancy

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectionee1399c251cf213d7417` |
| **Display Name** | `Life Expectancy` |
| **Filters** |  |
| **Ordinal** | `0` |
| **Visual containers number** | `14` |

[Up](#report-sections)



### Container df8451c4c46f34b97dcf 

| Param  | Value  |
|---|---|
| **Name:** | `df8451c4c46f34b97dcf` |
| **Type:** | `shapeMap` |
| **Business objects:**  | `life_expectancy_years, Country, Metrics` | 
| **Attributes:**  | Column: `Country.Country Code`<br/> Aggregation: `Min(Country.Country)`<br/> Measure: `Metrics.Life Expectancy` | 

[Up](#report-sections)




### Container 60ad1a6cbc2a1aab0cd4 

| Param  | Value  |
|---|---|
| **Name:** | `60ad1a6cbc2a1aab0cd4` |
| **Type:** | `slicer` |
| **Business objects:**  | `Years` | 
| **Attributes:**  | Column: `Years.Years` | 

[Up](#report-sections)




### Container 95dab029e45250390896 

| Param  | Value  |
|---|---|
| **Name:** | `95dab029e45250390896` |
| **Type:** | `columnChart` |
| **Business objects:**  | `Metrics, Extra Year` | 
| **Attributes:**  | Column: `Extra Year.Extra year`<br/> Measure: `Metrics.Life Expectancy For Chart` | 

[Up](#report-sections)




### Container 64e8a0b80ae9323e10fe 

| Param  | Value  |
|---|---|
| **Name:** | `64e8a0b80ae9323e10fe` |
| **Type:** | `pivotTable` |
| **Business objects:**  | `Legend` | 
| **Attributes:**  | Aggregation: `Sum(Legend.Bubble01)`<br/> Aggregation: `Sum(Legend.Bubble02)`<br/> Aggregation: `Sum(Legend.Bubble03)`<br/> Aggregation: `Sum(Legend.Bubble04)`<br/> Aggregation: `Sum(Legend.Bubble05)`<br/> Column: `Legend.Metric` | 

[Up](#report-sections)




### Container d4d069eaeabe387e1830 

| Param  | Value  |
|---|---|
| **Name:** | `d4d069eaeabe387e1830` |
| **Type:** | `treemap` |
| **Business objects:**  | `Population, Country, Buckets, Metrics` | 
| **Attributes:**  | Aggregation: `Sum(Population.Population)`<br/> Column: `Country.Country Code`<br/> Measure: `Metrics.Life Expectancy`<br/> Column: `Buckets.Bucket`<br/> Aggregation: `Min(Country.Country)` | 

[Up](#report-sections)




### Container 6ca4a836ba33a9971a5d 

| Param  | Value  |
|---|---|
| **Name:** | `6ca4a836ba33a9971a5d` |
| **Type:** | `barChart` |
| **Business objects:**  | `Buckets, Indicators` | 
| **Attributes:**  | Column: `Buckets.Bucket`<br/> Aggregation: `CountNonNull(healthappended.Country)` | 

[Up](#report-sections)




### Container 105e65704650a1cb6ef7 

| Param  | Value  |
|---|---|
| **Name:** | `105e65704650a1cb6ef7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 21d97658b8cb28599421 

| Param  | Value  |
|---|---|
| **Name:** | `21d97658b8cb28599421` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container aeb3540e90de0d70f628 

| Param  | Value  |
|---|---|
| **Name:** | `aeb3540e90de0d70f628` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 19d594667503eb8b1946 

| Param  | Value  |
|---|---|
| **Name:** | `19d594667503eb8b1946` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 9756133212a7c7087e48 

| Param  | Value  |
|---|---|
| **Name:** | `9756133212a7c7087e48` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 7715b7e288d84dc8f902 

| Param  | Value  |
|---|---|
| **Name:** | `7715b7e288d84dc8f902` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container df52ad9be48697dc54e0 

| Param  | Value  |
|---|---|
| **Name:** | `df52ad9be48697dc54e0` |
| **Type:** | `card` |
| **Business objects:**  | `Metrics` | 
| **Attributes:**  | Measure: `Metrics.Life Expectancy` | 

[Up](#report-sections)




### Container 7bb8f6272cd55ccedd12 

| Param  | Value  |
|---|---|
| **Name:** | `7bb8f6272cd55ccedd12` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Child Mortality

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection0818163179037b4c900f` |
| **Display Name** | `Child Mortality` |
| **Filters** | Name: `Filter2` Type: `Categorical` Column: `Country.Country Code` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Country\", \"Name\": \"c\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"Not\": {\"Expression\": {\"In\": {\"Expressions\": [{\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"c\"}}, \"Property\": \"Country Code\"}}], \"Values\": [[{\"Literal\": {\"Value\": \"null\"}}]]}}}}}]}"')<br/>Name: `Filter` Type: `Categorical` Column: `Sex.Sex` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Sex\", \"Name\": \"s\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"In\": {\"Expressions\": [{\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"s\"}}, \"Property\": \"Sex\"}}], \"Values\": [[{\"Literal\": {\"Value\": \"\'Both sexes\'\"}}]]}}}]}"')<br/>Name: `Filter1` Type: `Advanced` Column: `Years.Years` [<sup>def</sup>](## '"{\"From\": [{\"Entity\": \"Years\", \"Name\": \"y\", \"Type\": 0}], \"Version\": 2, \"Where\": [{\"Condition\": {\"And\": {\"Left\": {\"Comparison\": {\"ComparisonKind\": 1, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"y\"}}, \"Property\": \"Years\"}}, \"Right\": {\"Literal\": {\"Value\": \"1990D\"}}}}, \"Right\": {\"Comparison\": {\"ComparisonKind\": 3, \"Left\": {\"Column\": {\"Expression\": {\"SourceRef\": {\"Source\": \"y\"}}, \"Property\": \"Years\"}}, \"Right\": {\"Literal\": {\"Value\": \"2017D\"}}}}}}}]}"') |
| **Ordinal** | `1` |
| **Visual containers number** | `18` |

[Up](#report-sections)



### Container 105e65704650a1cb6ef7 

| Param  | Value  |
|---|---|
| **Name:** | `105e65704650a1cb6ef7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 21d97658b8cb28599421 

| Param  | Value  |
|---|---|
| **Name:** | `21d97658b8cb28599421` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container aeb3540e90de0d70f628 

| Param  | Value  |
|---|---|
| **Name:** | `aeb3540e90de0d70f628` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 19d594667503eb8b1946 

| Param  | Value  |
|---|---|
| **Name:** | `19d594667503eb8b1946` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 9756133212a7c7087e48 

| Param  | Value  |
|---|---|
| **Name:** | `9756133212a7c7087e48` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 7715b7e288d84dc8f902 

| Param  | Value  |
|---|---|
| **Name:** | `7715b7e288d84dc8f902` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 06b0d57417f0ab72c8fc 

| Param  | Value  |
|---|---|
| **Name:** | `06b0d57417f0ab72c8fc` |
| **Type:** | `scatterChart` |
| **Business objects:**  | `Country, Population, Metrics, Year` | 
| **Attributes:**  | Column: `Country.Country`<br/> Aggregation: `Sum(Population.Population)`<br/> Measure: `Metrics.Life Expectancy`<br/> Measure: `Metrics.Child Mortality Rate`<br/> Column: `Country.Country Code`<br/> Column: `Year.Year`<br/> Aggregation: `Min(Country.Country)` | 

[Up](#report-sections)




### Container f300565a41c419ab7749 

| Param  | Value  |
|---|---|
| **Name:** | `f300565a41c419ab7749` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.GDP Red` | 

[Up](#report-sections)




### Container 8c2291cf00f8e997ef23 

| Param  | Value  |
|---|---|
| **Name:** | `8c2291cf00f8e997ef23` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GEH Goal`<br/> Measure: `Metrics.Goverment Expenditure on Health (%)` | 

[Up](#report-sections)




### Container 39767e40110edf6d6b66 

| Param  | Value  |
|---|---|
| **Name:** | `39767e40110edf6d6b66` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Immunizations`<br/> Measure: `Metrics.IMM Red` | 

[Up](#report-sections)




### Container 8ce76a6c7491357aa440 

| Param  | Value  |
|---|---|
| **Name:** | `8ce76a6c7491357aa440` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.CFR Red`<br/> Measure: `Metrics.Cholera Fatality Rate (%)` | 

[Up](#report-sections)




### Container 32200cdbe47612c0dcd2 

| Param  | Value  |
|---|---|
| **Name:** | `32200cdbe47612c0dcd2` |
| **Type:** | `tableEx` |
| **Business objects:**  | `Country` | 
| **Attributes:**  | Column: `Country.Country` | 

[Up](#report-sections)




### Container 8351276cd98d8d3b0f92 

| Param  | Value  |
|---|---|
| **Name:** | `8351276cd98d8d3b0f92` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container c602df1209ee0829f9ce 

| Param  | Value  |
|---|---|
| **Name:** | `c602df1209ee0829f9ce` |
| **Type:** | `barChart` |
| **Business objects:**  | `Buckets, Metrics` | 
| **Attributes:**  | Column: `Buckets.Bucket`<br/> Measure: `Metrics.CLE` | 

[Up](#report-sections)




### Container 3f7255adfc50379f827c 

| Param  | Value  |
|---|---|
| **Name:** | `3f7255adfc50379f827c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container bced312d882d2655986d 

| Param  | Value  |
|---|---|
| **Name:** | `bced312d882d2655986d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b499354d0abba1d0dba3 

| Param  | Value  |
|---|---|
| **Name:** | `b499354d0abba1d0dba3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 44d2a56c9f4b03e69d25 

| Param  | Value  |
|---|---|
| **Name:** | `44d2a56c9f4b03e69d25` |
| **Type:** | `textFilter25A4896A83E0487089E2B90C9AE57C8A` |
| **Business objects:**  | `Country` | 
| **Attributes:**  | Column: `Country.Country` | 

[Up](#report-sections)


## Key Drivers

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection2ca59a708fedf6ab4fa4` |
| **Display Name** | `Key Drivers` |
| **Filters** | Name: `Filter1` Type: `Categorical` Column: `Indicators.Safe drinking water services (% of population)` [<sup>def</sup>](## '"{\"Column\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Indicators\"}}, \"Property\": \"Safe drinking water services (% of population)\"}}"')<br/>Name: `Filter` Type: `Advanced` Column: `Date Hierarchy.Year` [<sup>def</sup>](## '"{\"HierarchyLevel\": {\"Expression\": {\"Hierarchy\": {\"Expression\": {\"PropertyVariationSource\": {\"Expression\": {\"SourceRef\": {\"Entity\": \"Year\"}}, \"Name\": \"Variation\", \"Property\": \"Date\"}}, \"Hierarchy\": \"Date Hierarchy\"}}, \"Level\": \"Year\"}}"') |
| **Ordinal** | `2` |
| **Visual containers number** | `18` |

[Up](#report-sections)



### Container d45dd42752ef7cfcc64b 

| Param  | Value  |
|---|---|
| **Name:** | `d45dd42752ef7cfcc64b` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 36faabfe55345e2144cd 

| Param  | Value  |
|---|---|
| **Name:** | `36faabfe55345e2144cd` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 2faaece5bc034736545d 

| Param  | Value  |
|---|---|
| **Name:** | `2faaece5bc034736545d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container fc31d18c401bde438831 

| Param  | Value  |
|---|---|
| **Name:** | `fc31d18c401bde438831` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 8607dac80516e0367e67 

| Param  | Value  |
|---|---|
| **Name:** | `8607dac80516e0367e67` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 575ed909acc5ddd2a879 

| Param  | Value  |
|---|---|
| **Name:** | `575ed909acc5ddd2a879` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 2b21fbf0f63ecc1ff4f9 

| Param  | Value  |
|---|---|
| **Name:** | `2b21fbf0f63ecc1ff4f9` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container e8079ea363e79fbb7507 

| Param  | Value  |
|---|---|
| **Name:** | `e8079ea363e79fbb7507` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 8bb6316ac729e68144f7 

| Param  | Value  |
|---|---|
| **Name:** | `8bb6316ac729e68144f7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container ccdb647d7565ac99ffa5 

| Param  | Value  |
|---|---|
| **Name:** | `ccdb647d7565ac99ffa5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 1906c395fcecddedf7b3 

| Param  | Value  |
|---|---|
| **Name:** | `1906c395fcecddedf7b3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container f0900968d29fac31abf6 

| Param  | Value  |
|---|---|
| **Name:** | `f0900968d29fac31abf6` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 4bbd54482e4bdaa114d3 

| Param  | Value  |
|---|---|
| **Name:** | `4bbd54482e4bdaa114d3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container e927cc565ae3ced57fd5 

| Param  | Value  |
|---|---|
| **Name:** | `e927cc565ae3ced57fd5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 855201fbc25b1da8d08e 

| Param  | Value  |
|---|---|
| **Name:** | `855201fbc25b1da8d08e` |
| **Type:** | `textFilter25A4896A83E0487089E2B90C9AE57C8A` |
| **Business objects:**  | `Country` | 
| **Attributes:**  | Column: `Country.Country` | 

[Up](#report-sections)




### Container 8f92a8b0035b98603e84 

| Param  | Value  |
|---|---|
| **Name:** | `8f92a8b0035b98603e84` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Year, Metrics` | 
| **Attributes:**  | Column: `Year.Year`<br/> Measure: `Metrics.Life Expectancy 2` | 

[Up](#report-sections)




### Container 483d3d92bb067605e03d 

| Param  | Value  |
|---|---|
| **Name:** | `483d3d92bb067605e03d` |
| **Type:** | `barChart` |
| **Business objects:**  | `Sex, Metrics` | 
| **Attributes:**  | Column: `Sex.Sex`<br/> Measure: `Metrics.LE-100`<br/> Measure: `Metrics.Life Expectancy 2` | 

[Up](#report-sections)




### Container 1c0a2af96d0960019b6a 

| Param  | Value  |
|---|---|
| **Name:** | `1c0a2af96d0960019b6a` |
| **Type:** | `keyDriversVisual` |
| **Business objects:**  | `Indicators` | 
| **Attributes:**  | Measure: `Indicators.Life expectancy`<br/> Column: `Indicators.Female pupils below minimum reading proficiency at end of primary (%)`<br/> Column: `Indicators.GDP per capita (US $)`<br/> Column: `Indicators.Net national income per capita`<br/> Column: `Indicators.People using safely managed drinking water services (% of population)`<br/> Column: `Indicators.Percentage of female population with no education`<br/> Column: `Indicators.Safe drinking water services (% of population)`<br/> Column: `Indicators.Year` | 

[Up](#report-sections)


## Root Causes

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection7f65473376d6aed1a9d8` |
| **Display Name** | `Root Causes` |
| **Filters** |  |
| **Ordinal** | `3` |
| **Visual containers number** | `10` |

[Up](#report-sections)



### Container e1b47e6c5f5a6d3d9ed1 

| Param  | Value  |
|---|---|
| **Name:** | `e1b47e6c5f5a6d3d9ed1` |
| **Type:** | `decompositionTreeVisual` |
| **Business objects:**  | `Metrics, Variance Analysis, Country` | 
| **Attributes:**  | Measure: `Metrics.Life Expectancy YoY% 2`<br/> Column: `Variance Analysis.GDP per capita`<br/> Column: `Variance Analysis.Maternal Mortality`<br/> Column: `Variance Analysis.Tuberculosis Incidents`<br/> Column: `Variance Analysis.Neonatal Mortality`<br/> Column: `Variance Analysis.Malaria Cases`<br/> Column: `Country.Continent` | 

[Up](#report-sections)




### Container b4d8552348b0a83a9b80 

| Param  | Value  |
|---|---|
| **Name:** | `b4d8552348b0a83a9b80` |
| **Type:** | `CardBrowser8D7CFFDA2E7E400C9474F41B9EDBBA58` |
| **Business objects:**  | `Flags, Country` | 
| **Attributes:**  | Column: `Flags.Country`<br/> Column: `Flags.ImageURL`<br/> Aggregation: `Min(Country.Region)` | 

[Up](#report-sections)




### Container bcb04372e8d8f1b321ab 

| Param  | Value  |
|---|---|
| **Name:** | `bcb04372e8d8f1b321ab` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 364b88354cdfe21d9389 

| Param  | Value  |
|---|---|
| **Name:** | `364b88354cdfe21d9389` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container faf7cb7cdf4e90e11b98 

| Param  | Value  |
|---|---|
| **Name:** | `faf7cb7cdf4e90e11b98` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 90a9b4bc75e659463e36 

| Param  | Value  |
|---|---|
| **Name:** | `90a9b4bc75e659463e36` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b2fe2cd45ab37255e152 

| Param  | Value  |
|---|---|
| **Name:** | `b2fe2cd45ab37255e152` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 40b8a513b4f818d47964 

| Param  | Value  |
|---|---|
| **Name:** | `40b8a513b4f818d47964` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 8d93005c6db248cd9781 

| Param  | Value  |
|---|---|
| **Name:** | `8d93005c6db248cd9781` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b6a5d3712063990ba4a3 

| Param  | Value  |
|---|---|
| **Name:** | `b6a5d3712063990ba4a3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## GDP Analysis

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectiona99246b922db09a477b7` |
| **Display Name** | `GDP Analysis` |
| **Filters** |  |
| **Ordinal** | `4` |
| **Visual containers number** | `12` |

[Up](#report-sections)



### Container bcb04372e8d8f1b321ab 

| Param  | Value  |
|---|---|
| **Name:** | `bcb04372e8d8f1b321ab` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 364b88354cdfe21d9389 

| Param  | Value  |
|---|---|
| **Name:** | `364b88354cdfe21d9389` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container faf7cb7cdf4e90e11b98 

| Param  | Value  |
|---|---|
| **Name:** | `faf7cb7cdf4e90e11b98` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 90a9b4bc75e659463e36 

| Param  | Value  |
|---|---|
| **Name:** | `90a9b4bc75e659463e36` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b2fe2cd45ab37255e152 

| Param  | Value  |
|---|---|
| **Name:** | `b2fe2cd45ab37255e152` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 40b8a513b4f818d47964 

| Param  | Value  |
|---|---|
| **Name:** | `40b8a513b4f818d47964` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 9737d6b53d07bec8a030 

| Param  | Value  |
|---|---|
| **Name:** | `9737d6b53d07bec8a030` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container c103b08eacb73e7338a7 

| Param  | Value  |
|---|---|
| **Name:** | `c103b08eacb73e7338a7` |
| **Type:** | `scatterChart` |
| **Business objects:**  | `Metrics, Country, Population` | 
| **Attributes:**  | Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.Life Expectancy 2`<br/> Column: `Country.Country`<br/> Column: `Country.Region`<br/> Aggregation: `Sum(Population.Population)` | 

[Up](#report-sections)




### Container d9226e2da6780008095a 

| Param  | Value  |
|---|---|
| **Name:** | `d9226e2da6780008095a` |
| **Type:** | `areaChart` |
| **Business objects:**  | `Year, Metrics, Country` | 
| **Attributes:**  | HierarchyLevel: `Year.Date.Variation.Date Hierarchy.Year`<br/> HierarchyLevel: `Year.Date.Variation.Date Hierarchy.Quarter`<br/> HierarchyLevel: `Year.Date.Variation.Date Hierarchy.Month`<br/> HierarchyLevel: `Year.Date.Variation.Date Hierarchy.Day`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Column: `Country.Continent` | 

[Up](#report-sections)




### Container 6eedbc64bc4400d0309a 

| Param  | Value  |
|---|---|
| **Name:** | `6eedbc64bc4400d0309a` |
| **Type:** | `clusteredBarChart` |
| **Business objects:**  | `Metrics, Country` | 
| **Attributes:**  | Measure: `Metrics.GDP Per Capita (USD)`<br/> Column: `Country.Country`<br/> Column: `Country.Continent` | 

[Up](#report-sections)




### Container 242d6ec09d756570d709 

| Param  | Value  |
|---|---|
| **Name:** | `242d6ec09d756570d709` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 3b07577e6ea620ae543d 

| Param  | Value  |
|---|---|
| **Name:** | `3b07577e6ea620ae543d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Dashboard

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection41c4e6d5920e25ef64d4` |
| **Display Name** | `Dashboard` |
| **Filters** |  |
| **Ordinal** | `5` |
| **Visual containers number** | `35` |

[Up](#report-sections)



### Container 30c22cde244e8c5d29a9 

| Param  | Value  |
|---|---|
| **Name:** | `30c22cde244e8c5d29a9` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Life Expectancy`<br/> Measure: `Metrics.LE-Goal` | 

[Up](#report-sections)




### Container 71694abd09640a8dc50f 

| Param  | Value  |
|---|---|
| **Name:** | `71694abd09640a8dc50f` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GEH Goal`<br/> Measure: `Metrics.Goverment Expenditure on Health (%)` | 

[Up](#report-sections)




### Container 2c56081e1b496591b6bd 

| Param  | Value  |
|---|---|
| **Name:** | `2c56081e1b496591b6bd` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Immunizations`<br/> Measure: `Metrics.IMM Red` | 

[Up](#report-sections)




### Container 8742b121c06f42395718 

| Param  | Value  |
|---|---|
| **Name:** | `8742b121c06f42395718` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.CFR Red`<br/> Measure: `Metrics.Child Mortality Rate` | 

[Up](#report-sections)




### Container e0506c325848dc316dec 

| Param  | Value  |
|---|---|
| **Name:** | `e0506c325848dc316dec` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.GDP Red` | 

[Up](#report-sections)




### Container 3822012e5329eecd6c16 

| Param  | Value  |
|---|---|
| **Name:** | `3822012e5329eecd6c16` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Life Expectancy`<br/> Measure: `Metrics.LE-Goal` | 

[Up](#report-sections)




### Container 9bfcce77ead1838036e3 

| Param  | Value  |
|---|---|
| **Name:** | `9bfcce77ead1838036e3` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.GDP Red` | 

[Up](#report-sections)




### Container ac40c208d7c7402f30e2 

| Param  | Value  |
|---|---|
| **Name:** | `ac40c208d7c7402f30e2` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GEH Goal`<br/> Measure: `Metrics.Goverment Expenditure on Health (%)` | 

[Up](#report-sections)




### Container 094553561fed06ee3415 

| Param  | Value  |
|---|---|
| **Name:** | `094553561fed06ee3415` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Immunizations`<br/> Measure: `Metrics.IMM Red` | 

[Up](#report-sections)




### Container 5c78314bee97d0a0bdb7 

| Param  | Value  |
|---|---|
| **Name:** | `5c78314bee97d0a0bdb7` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.CFR Red`<br/> Measure: `Metrics.Child Mortality Rate` | 

[Up](#report-sections)




### Container 5befa2c3be43ac844468 

| Param  | Value  |
|---|---|
| **Name:** | `5befa2c3be43ac844468` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Life Expectancy`<br/> Measure: `Metrics.LE-Goal` | 

[Up](#report-sections)




### Container 2a4d02ece2aa6626e6d9 

| Param  | Value  |
|---|---|
| **Name:** | `2a4d02ece2aa6626e6d9` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.GDP Red` | 

[Up](#report-sections)




### Container c8295edcfb9fe353ed42 

| Param  | Value  |
|---|---|
| **Name:** | `c8295edcfb9fe353ed42` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GEH Goal`<br/> Measure: `Metrics.Goverment Expenditure on Health (%)` | 

[Up](#report-sections)




### Container 55aace4b670eda42ab6f 

| Param  | Value  |
|---|---|
| **Name:** | `55aace4b670eda42ab6f` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Immunizations`<br/> Measure: `Metrics.IMM Red` | 

[Up](#report-sections)




### Container c2f1b126f4511a330ba3 

| Param  | Value  |
|---|---|
| **Name:** | `c2f1b126f4511a330ba3` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.CFR Red`<br/> Measure: `Metrics.Child Mortality Rate` | 

[Up](#report-sections)




### Container 649bb133dc2ca6d8d858 

| Param  | Value  |
|---|---|
| **Name:** | `649bb133dc2ca6d8d858` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Life Expectancy`<br/> Measure: `Metrics.LE-Goal` | 

[Up](#report-sections)




### Container 062da38267256450df5e 

| Param  | Value  |
|---|---|
| **Name:** | `062da38267256450df5e` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.GDP Red` | 

[Up](#report-sections)




### Container 62dd84a6a714f4eafe26 

| Param  | Value  |
|---|---|
| **Name:** | `62dd84a6a714f4eafe26` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GEH Goal`<br/> Measure: `Metrics.Goverment Expenditure on Health (%)` | 

[Up](#report-sections)




### Container a27d889f8e7df0331d6b 

| Param  | Value  |
|---|---|
| **Name:** | `a27d889f8e7df0331d6b` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Immunizations`<br/> Measure: `Metrics.IMM Red` | 

[Up](#report-sections)




### Container a313db85cde7579f35b0 

| Param  | Value  |
|---|---|
| **Name:** | `a313db85cde7579f35b0` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.CFR Red`<br/> Measure: `Metrics.Child Mortality Rate` | 

[Up](#report-sections)




### Container 16d7182a26b66268fe91 

| Param  | Value  |
|---|---|
| **Name:** | `16d7182a26b66268fe91` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Life Expectancy`<br/> Measure: `Metrics.LE-Goal` | 

[Up](#report-sections)




### Container 5a467da711991f636fef 

| Param  | Value  |
|---|---|
| **Name:** | `5a467da711991f636fef` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GDP Per Capita (USD)`<br/> Measure: `Metrics.GDP Red` | 

[Up](#report-sections)




### Container b92502163d522f9c342a 

| Param  | Value  |
|---|---|
| **Name:** | `b92502163d522f9c342a` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.GEH Goal`<br/> Measure: `Metrics.Goverment Expenditure on Health (%)` | 

[Up](#report-sections)




### Container 51073d4eec9e1d365d0f 

| Param  | Value  |
|---|---|
| **Name:** | `51073d4eec9e1d365d0f` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.Immunizations`<br/> Measure: `Metrics.IMM Red` | 

[Up](#report-sections)




### Container 6ae83d1eea71adb2761f 

| Param  | Value  |
|---|---|
| **Name:** | `6ae83d1eea71adb2761f` |
| **Type:** | `kpi` |
| **Business objects:**  | `Metrics, Years` | 
| **Attributes:**  | Column: `Years.Years`<br/> Measure: `Metrics.CFR Red`<br/> Measure: `Metrics.Child Mortality Rate` | 

[Up](#report-sections)




### Container 670b0d3b9a7086935e0a 

| Param  | Value  |
|---|---|
| **Name:** | `670b0d3b9a7086935e0a` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 882b5cb309328b5820e2 

| Param  | Value  |
|---|---|
| **Name:** | `882b5cb309328b5820e2` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b71f7e9945cbbdd9660c 

| Param  | Value  |
|---|---|
| **Name:** | `b71f7e9945cbbdd9660c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 3fe79b0a7d0c9167241c 

| Param  | Value  |
|---|---|
| **Name:** | `3fe79b0a7d0c9167241c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 9e7c5fc4ea44664aa63d 

| Param  | Value  |
|---|---|
| **Name:** | `9e7c5fc4ea44664aa63d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 01171b4fd53814552049 

| Param  | Value  |
|---|---|
| **Name:** | `01171b4fd53814552049` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container af207fc723904db071ae 

| Param  | Value  |
|---|---|
| **Name:** | `af207fc723904db071ae` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 16a1ff6247617e470ad8 

| Param  | Value  |
|---|---|
| **Name:** | `16a1ff6247617e470ad8` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 32a1af77bcd4d93d349e 

| Param  | Value  |
|---|---|
| **Name:** | `32a1af77bcd4d93d349e` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 8cea3b11c21c1c977910 

| Param  | Value  |
|---|---|
| **Name:** | `8cea3b11c21c1c977910` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Tooltip

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection7c2fc1fb381618b20e95` |
| **Display Name** | `Tooltip` |
| **Filters** |  |
| **Ordinal** | `6` |
| **Visual containers number** | `11` |

[Up](#report-sections)



### Container 9d9a56640e625aa0e399 

| Param  | Value  |
|---|---|
| **Name:** | `9d9a56640e625aa0e399` |
| **Type:** | `gauge` |
| **Business objects:**  | `Metrics` | 
| **Attributes:**  | Measure: `Metrics.Life Expectancy` | 

[Up](#report-sections)




### Container cca09ee5472200d59109 

| Param  | Value  |
|---|---|
| **Name:** | `cca09ee5472200d59109` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 4f0e2a2dad7a1d17787e 

| Param  | Value  |
|---|---|
| **Name:** | `4f0e2a2dad7a1d17787e` |
| **Type:** | `pivotTable` |
| **Business objects:**  | `Country` | 
| **Attributes:**  | Column: `Country.World`<br/> Aggregation: `Min(Country.Country)` | 

[Up](#report-sections)




### Container aa8292e0b0a8e5283eeb 

| Param  | Value  |
|---|---|
| **Name:** | `aa8292e0b0a8e5283eeb` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container ab16191c39a3a6d7a4ca 

| Param  | Value  |
|---|---|
| **Name:** | `ab16191c39a3a6d7a4ca` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b15e82820991ce6e44c3 

| Param  | Value  |
|---|---|
| **Name:** | `b15e82820991ce6e44c3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 3b915f38dde73360b050 

| Param  | Value  |
|---|---|
| **Name:** | `3b915f38dde73360b050` |
| **Type:** | `gauge` |
| **Business objects:**  | `Metrics` | 
| **Attributes:**  | Measure: `Metrics.Life Expectancy` | 

[Up](#report-sections)




### Container 88a38374c70ee606b076 

| Param  | Value  |
|---|---|
| **Name:** | `88a38374c70ee606b076` |
| **Type:** | `card` |
| **Business objects:**  | `Metrics` | 
| **Attributes:**  | Measure: `Metrics.Life Expectancy` | 

[Up](#report-sections)




### Container 58bb16bd0002003eb00d 

| Param  | Value  |
|---|---|
| **Name:** | `58bb16bd0002003eb00d` |
| **Type:** | `card` |
| **Business objects:**  | `Metrics` | 
| **Attributes:**  | Measure: `Metrics.Life Expectancy` | 

[Up](#report-sections)




### Container f6cf7c54d07eabeab414 

| Param  | Value  |
|---|---|
| **Name:** | `f6cf7c54d07eabeab414` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 1103beada495091a252d 

| Param  | Value  |
|---|---|
| **Name:** | `1103beada495091a252d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)


## Resources

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection429176b3a10e44511357` |
| **Display Name** | `Resources` |
| **Filters** |  |
| **Ordinal** | `7` |
| **Visual containers number** | `10` |

[Up](#report-sections)



### Container bcb04372e8d8f1b321ab 

| Param  | Value  |
|---|---|
| **Name:** | `bcb04372e8d8f1b321ab` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 364b88354cdfe21d9389 

| Param  | Value  |
|---|---|
| **Name:** | `364b88354cdfe21d9389` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container faf7cb7cdf4e90e11b98 

| Param  | Value  |
|---|---|
| **Name:** | `faf7cb7cdf4e90e11b98` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 90a9b4bc75e659463e36 

| Param  | Value  |
|---|---|
| **Name:** | `90a9b4bc75e659463e36` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container b2fe2cd45ab37255e152 

| Param  | Value  |
|---|---|
| **Name:** | `b2fe2cd45ab37255e152` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 40b8a513b4f818d47964 

| Param  | Value  |
|---|---|
| **Name:** | `40b8a513b4f818d47964` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 9737d6b53d07bec8a030 

| Param  | Value  |
|---|---|
| **Name:** | `9737d6b53d07bec8a030` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 242d6ec09d756570d709 

| Param  | Value  |
|---|---|
| **Name:** | `242d6ec09d756570d709` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 3b07577e6ea620ae543d 

| Param  | Value  |
|---|---|
| **Name:** | `3b07577e6ea620ae543d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)




### Container 67464206ce06d30c3726 

| Param  | Value  |
|---|---|
| **Name:** | `67464206ce06d30c3726` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#report-sections)







----
<p align="center">
Generated at 27.03.2024 13:01:36 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 
</p>