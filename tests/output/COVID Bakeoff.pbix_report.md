----

[Home](./index.md) > [COVID Bakeoff.pbix_report](COVID%20Bakeoff.pbix_report.md)

|[Report sections](#report-sections) |

----


# Report sections

## Global Vaccinations

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection7bdccf651d98bc34a50d` |
| **Display Name** | `Global Vaccinations` |
| **Filters** | `[{"name":"Filter78d8b4de5d2e0a98aeb7","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Countries"}},"Property":"Country"}},"filter":{"Version":2,"From":[{"Name":"c","Entity":"Countries","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"Country"}}],"Values":[[{"Literal":{"Value":"null"}}]]}}}}}]},"type":"Categorical","howCreated":1,"objects":{"general":[{"properties":{"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}]}},{"name":"Filterf730e423025a13632cbb","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Countries"}},"Property":"Population"}},"filter":{"Version":2,"From":[{"Name":"c","Entity":"Countries","Type":0}],"Where":[{"Condition":{"Comparison":{"ComparisonKind":1,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"Population"}},"Right":{"Literal":{"Value":"1000000L"}}}}}]},"type":"Advanced","howCreated":1}]` |
| **Ordinal** | `0` |
| **Visual containers number** | `8` |

[Up](#)



### Container ddcbc8f094b45898734c 

| Param  | Value  |
|---|---|
| **Name:** | `ddcbc8f094b45898734c` |
| **Type:** | `lineStackedColumnComboChart` |
| **Business objects:**  | `Dates, OWID COVID data` | 
| **Attributes:**  | Column: Dates.Date<br/> Measure: OWID COVID data.Cases 7d Mvg Avg per million<br/> Measure: OWID COVID data.Share of Population vaccinated<br/> Measure: OWID COVID data.Daily Change (for formatting) | 

[Up](#)




### Container fcb8ffb4d02bed39ca81 

| Param  | Value  |
|---|---|
| **Name:** | `fcb8ffb4d02bed39ca81` |
| **Type:** | `map` |
| **Business objects:**  | `Countries, OWID COVID data` | 
| **Attributes:**  | Column: Countries.COUNTRY<br/> Measure: OWID COVID data.Share of Population vaccinated<br/> Column: Countries.Continent | 

[Up](#)




### Container 519ef34108ec0583040c 

| Param  | Value  |
|---|---|
| **Name:** | `519ef34108ec0583040c` |
| **Type:** | `barChart` |
| **Business objects:**  | `Countries, OWID COVID data` | 
| **Attributes:**  | Column: Countries.COUNTRY<br/> Aggregation: Sum(Countries.Population)<br/> Measure: owid-covid-data.Measure | 

[Up](#)




### Container 622d8d411cb970245b80 

| Param  | Value  |
|---|---|
| **Name:** | `622d8d411cb970245b80` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 3539983f0735879e9bab 

| Param  | Value  |
|---|---|
| **Name:** | `3539983f0735879e9bab` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container bb0df01c43a0310bc0e7 

| Param  | Value  |
|---|---|
| **Name:** | `bb0df01c43a0310bc0e7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container fe5aff94e14edca2c3c5 

| Param  | Value  |
|---|---|
| **Name:** | `fe5aff94e14edca2c3c5` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 5e331d513983020b450b 

| Param  | Value  |
|---|---|
| **Name:** | `5e331d513983020b450b` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## Cases/Vaccines animation

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectiond98e33c37b4b84be4c71` |
| **Display Name** | `Cases/Vaccines animation` |
| **Filters** | `[{"name":"Filter2e9285e275a8d5bee683","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Countries"}},"Property":"Country"}},"filter":{"Version":2,"From":[{"Name":"c","Entity":"Countries","Type":0}],"Where":[{"Condition":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"Country"}}],"Values":[[{"Literal":{"Value":"'United States'"}}]]}}}]},"type":"Categorical","howCreated":5}]` |
| **Ordinal** | `1` |
| **Visual containers number** | `8` |

[Up](#)



### Container d97b3d9fcb3933228dd5 

| Param  | Value  |
|---|---|
| **Name:** | `d97b3d9fcb3933228dd5` |
| **Type:** | `scatterChart` |
| **Business objects:**  | `States, Cases per US State, Dates` | 
| **Attributes:**  | Column: States.State<br/> Measure: Cases per US State.Full vaccinations per hundred<br/> Measure: Cases per US State.Change from 12/27<br/> Column: Dates.Start of week<br/> Measure: Cases per US State.% Fully Vacc'd | 

[Up](#)




### Container c9b375b77ee90a500d9d 

| Param  | Value  |
|---|---|
| **Name:** | `c9b375b77ee90a500d9d` |
| **Type:** | `tableEx` |
| **Business objects:**  | `Cases per US State, States` | 
| **Attributes:**  | Column: States.State<br/> Column: States.Flag<br/> Measure: Cases per US State.% Fully Vacc'd<br/> Measure: Cases per US State.% One+ Shots | 

[Up](#)




### Container 48bd049742ed42450d63 

| Param  | Value  |
|---|---|
| **Name:** | `48bd049742ed42450d63` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container bafc37cdd0426e5d2b1a 

| Param  | Value  |
|---|---|
| **Name:** | `bafc37cdd0426e5d2b1a` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 6160c3f43aa17718cc9a 

| Param  | Value  |
|---|---|
| **Name:** | `6160c3f43aa17718cc9a` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 27467d84a6ca4263093e 

| Param  | Value  |
|---|---|
| **Name:** | `27467d84a6ca4263093e` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 7d22164a640142e07ee3 

| Param  | Value  |
|---|---|
| **Name:** | `7d22164a640142e07ee3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 21943438d0631b302128 

| Param  | Value  |
|---|---|
| **Name:** | `21943438d0631b302128` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## US Vaccinations

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectionad3b556fac31b946e0c1` |
| **Display Name** | `US Vaccinations` |
| **Filters** | `[]` |
| **Ordinal** | `2` |
| **Visual containers number** | `17` |

[Up](#)



### Container ff141d62080ee0093753 

| Param  | Value  |
|---|---|
| **Name:** | `ff141d62080ee0093753` |
| **Type:** | `tableEx` |
| **Business objects:**  | `Cases per US State, States` | 
| **Attributes:**  | Column: States.State<br/> Column: States.Flag<br/> Aggregation: Avg(States.Average Temperature )<br/> Measure: Cases per US State.% Fully Vacc'd | 

[Up](#)




### Container fd55bac8bed0e0839138 

| Param  | Value  |
|---|---|
| **Name:** | `fd55bac8bed0e0839138` |
| **Type:** | `lineStackedColumnComboChart` |
| **Business objects:**  | `States, Dates, Cases per US State` | 
| **Attributes:**  | Column: Dates.Date<br/> Measure: Cases per US State.Cases per million 7d avg<br/> Measure: Cases per US State.Full vaccinations per hundred<br/> Column: States.State (by cases)<br/> Measure: Cases per US State.Daily Change US (for formatting) | 

[Up](#)




### Container 0162742b4a9ea636b1aa 

| Param  | Value  |
|---|---|
| **Name:** | `0162742b4a9ea636b1aa` |
| **Type:** | `shapeMap` |
| **Business objects:**  | `States` | 
| **Attributes:**  | Column: States.State<br/> Aggregation: CountNonNull(States.Average Temperature ) | 

[Up](#)




### Container b33722933088628b099c 

| Param  | Value  |
|---|---|
| **Name:** | `b33722933088628b099c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 680ca02c81deb525780e 

| Param  | Value  |
|---|---|
| **Name:** | `680ca02c81deb525780e` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 33b5f3ffbae906c84310 

| Param  | Value  |
|---|---|
| **Name:** | `33b5f3ffbae906c84310` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container b5ef6399410706e87ed0 

| Param  | Value  |
|---|---|
| **Name:** | `b5ef6399410706e87ed0` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 5979aee1094b093d4540 

| Param  | Value  |
|---|---|
| **Name:** | `5979aee1094b093d4540` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 46396bdbbdec0797860c 

| Param  | Value  |
|---|---|
| **Name:** | `46396bdbbdec0797860c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 18dcc26163d31548ab0a 

| Param  | Value  |
|---|---|
| **Name:** | `18dcc26163d31548ab0a` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 37f0d1f4a4e9c89c7a3c 

| Param  | Value  |
|---|---|
| **Name:** | `37f0d1f4a4e9c89c7a3c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container ab70b341856d3c14c37d 

| Param  | Value  |
|---|---|
| **Name:** | `ab70b341856d3c14c37d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 5d28c15f216eb4b0e5cb 

| Param  | Value  |
|---|---|
| **Name:** | `5d28c15f216eb4b0e5cb` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 833a99a20b29ec64727c 

| Param  | Value  |
|---|---|
| **Name:** | `833a99a20b29ec64727c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 5f352452dae53e652601 

| Param  | Value  |
|---|---|
| **Name:** | `5f352452dae53e652601` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 43d203491a07ebb4132b 

| Param  | Value  |
|---|---|
| **Name:** | `43d203491a07ebb4132b` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 68100741a5d1174e79be 

| Param  | Value  |
|---|---|
| **Name:** | `68100741a5d1174e79be` |
| **Type:** | `lineStackedColumnComboChart` |
| **Business objects:**  | `Dates, Cases per US State, States` | 
| **Attributes:**  | Column: Dates.Date<br/> Measure: Cases per US State.Cases per million 7d avg<br/> Measure: Cases per US State.Full vaccinations per hundred<br/> GroupRef: States.March Temperatures | 

[Up](#)


## <- Demo 1 | Demo 2 ->

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection2ebf34c58e6cb05ff932` |
| **Display Name** | `<- Demo 1 | Demo 2 ->` |
| **Filters** | `[]` |
| **Ordinal** | `3` |
| **Visual containers number** | `0` |

[Up](#)

## Vaccinations analysis (start)

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection9348de90cdb7d56fa044` |
| **Display Name** | `Vaccinations analysis (start)` |
| **Filters** | `[{"name":"Filterb8365039dd10ecbe7c44","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Dates"}},"Property":"Date"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Dates","Type":0}],"Where":[{"Condition":{"And":{"Left":{"Comparison":{"ComparisonKind":2,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Date"}},"Right":{"DateSpan":{"Expression":{"Literal":{"Value":"datetime'2020-04-04T00:00:00'"}},"TimeUnit":5}}}},"Right":{"Comparison":{"ComparisonKind":4,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Date"}},"Right":{"DateSpan":{"Expression":{"Literal":{"Value":"datetime'2021-04-07T00:00:00'"}},"TimeUnit":5}}}}}}}]},"type":"Advanced","howCreated":1}]` |
| **Ordinal** | `4` |
| **Visual containers number** | `13` |

[Up](#)



### Container bb138ed8833603195536 

| Param  | Value  |
|---|---|
| **Name:** | `bb138ed8833603195536` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 2fcdf3582ac016120092 

| Param  | Value  |
|---|---|
| **Name:** | `2fcdf3582ac016120092` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 1c5bb13fad005304cd28 

| Param  | Value  |
|---|---|
| **Name:** | `1c5bb13fad005304cd28` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 3fac96590354093397a3 

| Param  | Value  |
|---|---|
| **Name:** | `3fac96590354093397a3` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Cases per US State, Dates` | 
| **Attributes:**  | Column: Dates.Date<br/> Aggregation: Sum(Cases per US State.distributed_per_hundred) | 

[Up](#)




### Container eea85a81620bbc38e636 

| Param  | Value  |
|---|---|
| **Name:** | `eea85a81620bbc38e636` |
| **Type:** | `barChart` |
| **Business objects:**  | `States, Cases per US State` | 
| **Attributes:**  | Column: States.State<br/> Measure: Cases per US State.Vaccines distributed | 

[Up](#)




### Container 2a0bb1f10210cc293b42 

| Param  | Value  |
|---|---|
| **Name:** | `2a0bb1f10210cc293b42` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container f5c62cb204b088304ce3 

| Param  | Value  |
|---|---|
| **Name:** | `f5c62cb204b088304ce3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 76b642e9c6400276bd9b 

| Param  | Value  |
|---|---|
| **Name:** | `76b642e9c6400276bd9b` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container a78e58c4c15018c09d07 

| Param  | Value  |
|---|---|
| **Name:** | `a78e58c4c15018c09d07` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 7e8e5a39a93a31ed4025 

| Param  | Value  |
|---|---|
| **Name:** | `7e8e5a39a93a31ed4025` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container a1ae05fd5413a37c2478 

| Param  | Value  |
|---|---|
| **Name:** | `a1ae05fd5413a37c2478` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 488871e07527783d00d3 

| Param  | Value  |
|---|---|
| **Name:** | `488871e07527783d00d3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container e0467c667eac32333562 

| Param  | Value  |
|---|---|
| **Name:** | `e0467c667eac32333562` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## Vaccinations analysis (Finished)

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectiona9739bd9d6eec7056cdc` |
| **Display Name** | `Vaccinations analysis (Finished)` |
| **Filters** | `[{"name":"Filterb8365039dd10ecbe7c44","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Dates"}},"Property":"Date"}},"filter":{"Version":2,"From":[{"Name":"d","Entity":"Dates","Type":0}],"Where":[{"Condition":{"And":{"Left":{"Comparison":{"ComparisonKind":2,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Date"}},"Right":{"DateSpan":{"Expression":{"Literal":{"Value":"datetime'2020-04-04T00:00:00'"}},"TimeUnit":5}}}},"Right":{"Comparison":{"ComparisonKind":4,"Left":{"Column":{"Expression":{"SourceRef":{"Source":"d"}},"Property":"Date"}},"Right":{"DateSpan":{"Expression":{"Literal":{"Value":"datetime'2021-04-07T00:00:00'"}},"TimeUnit":5}}}}}}}]},"type":"Advanced","howCreated":1}]` |
| **Ordinal** | `5` |
| **Visual containers number** | `15` |

[Up](#)



### Container bb138ed8833603195536 

| Param  | Value  |
|---|---|
| **Name:** | `bb138ed8833603195536` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 2fcdf3582ac016120092 

| Param  | Value  |
|---|---|
| **Name:** | `2fcdf3582ac016120092` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 1c5bb13fad005304cd28 

| Param  | Value  |
|---|---|
| **Name:** | `1c5bb13fad005304cd28` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container c730b80a021077ea39c0 

| Param  | Value  |
|---|---|
| **Name:** | `c730b80a021077ea39c0` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Dates, Cases per US State` | 
| **Attributes:**  | Column: Dates.Date<br/> Aggregation: Sum(Cases per US State.Incremental cases) | 

[Up](#)




### Container 3fac96590354093397a3 

| Param  | Value  |
|---|---|
| **Name:** | `3fac96590354093397a3` |
| **Type:** | `lineChart` |
| **Business objects:**  | `Cases per US State, Dates` | 
| **Attributes:**  | Column: Dates.Date<br/> Aggregation: Sum(Cases per US State.distributed_per_hundred) | 

[Up](#)




### Container f85a91f1b042b0069d6d 

| Param  | Value  |
|---|---|
| **Name:** | `f85a91f1b042b0069d6d` |
| **Type:** | `map` |
| **Business objects:**  | `States, Cases per US State` | 
| **Attributes:**  | Column: States.State<br/> Aggregation: Sum(Cases per US State.Incremental cases) | 

[Up](#)




### Container eea85a81620bbc38e636 

| Param  | Value  |
|---|---|
| **Name:** | `eea85a81620bbc38e636` |
| **Type:** | `barChart` |
| **Business objects:**  | `States, Cases per US State` | 
| **Attributes:**  | Column: States.State<br/> Measure: Cases per US State.Vaccines distributed | 

[Up](#)




### Container 2a0bb1f10210cc293b42 

| Param  | Value  |
|---|---|
| **Name:** | `2a0bb1f10210cc293b42` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container f5c62cb204b088304ce3 

| Param  | Value  |
|---|---|
| **Name:** | `f5c62cb204b088304ce3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 76b642e9c6400276bd9b 

| Param  | Value  |
|---|---|
| **Name:** | `76b642e9c6400276bd9b` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container a78e58c4c15018c09d07 

| Param  | Value  |
|---|---|
| **Name:** | `a78e58c4c15018c09d07` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 7e8e5a39a93a31ed4025 

| Param  | Value  |
|---|---|
| **Name:** | `7e8e5a39a93a31ed4025` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container a1ae05fd5413a37c2478 

| Param  | Value  |
|---|---|
| **Name:** | `a1ae05fd5413a37c2478` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 488871e07527783d00d3 

| Param  | Value  |
|---|---|
| **Name:** | `488871e07527783d00d3` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container e0467c667eac32333562 

| Param  | Value  |
|---|---|
| **Name:** | `e0467c667eac32333562` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## Case rate influencers

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection7018f710b5d2aba96c32` |
| **Display Name** | `Case rate influencers` |
| **Filters** | `[{"name":"Filterbe118e413e550076b95c","expression":{"Column":{"Expression":{"SourceRef":{"Entity":"Countries"}},"Property":"Continent"}},"filter":{"Version":2,"From":[{"Name":"c","Entity":"Countries","Type":0}],"Where":[{"Condition":{"Not":{"Expression":{"In":{"Expressions":[{"Column":{"Expression":{"SourceRef":{"Source":"c"}},"Property":"Continent"}}],"Values":[[{"Literal":{"Value":"null"}}]]}}}}}]},"type":"Categorical","howCreated":1,"objects":{"general":[{"properties":{"isInvertedSelectionMode":{"expr":{"Literal":{"Value":"true"}}}}}]}}]` |
| **Ordinal** | `6` |
| **Visual containers number** | `7` |

[Up](#)



### Container a4882d869e5c72190851 

| Param  | Value  |
|---|---|
| **Name:** | `a4882d869e5c72190851` |
| **Type:** | `ImageGrid_FC5183B9_926C_45E0_B5F7_0CE9EAF1DA9B` |
| **Business objects:**  | `Countries` | 
| **Attributes:**  | Column: Countries.Flag | 

[Up](#)




### Container 1054214624737ba82845 

| Param  | Value  |
|---|---|
| **Name:** | `1054214624737ba82845` |
| **Type:** | `barChart` |
| **Business objects:**  | `OWID COVID data, Countries` | 
| **Attributes:**  | Column: Countries.Continent<br/> Measure: owid-covid-data.Total cases per mil | 

[Up](#)




### Container d51807fcaa061bb8db10 

| Param  | Value  |
|---|---|
| **Name:** | `d51807fcaa061bb8db10` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 9b9080e063b7c420e9ed 

| Param  | Value  |
|---|---|
| **Name:** | `9b9080e063b7c420e9ed` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 32b35b659eb30711c707 

| Param  | Value  |
|---|---|
| **Name:** | `32b35b659eb30711c707` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 14b55aa9d25c98ba22a7 

| Param  | Value  |
|---|---|
| **Name:** | `14b55aa9d25c98ba22a7` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 6a637aa8a9ca6572c94d 

| Param  | Value  |
|---|---|
| **Name:** | `6a637aa8a9ca6572c94d` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## Variance analysis

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSectiondf9ab418075e76cb40d6` |
| **Display Name** | `Variance analysis` |
| **Filters** | `[]` |
| **Ordinal** | `7` |
| **Visual containers number** | `8` |

[Up](#)



### Container 6a7d746ecee71d10922e 

| Param  | Value  |
|---|---|
| **Name:** | `6a7d746ecee71d10922e` |
| **Type:** | `decompositionTreeVisual` |
| **Business objects:**  | `Countries, Days with restrictions grouped` | 
| **Attributes:**  | Column: Countries.Custom<br/> Column: Days with restrictions grouped.Cancelling public events<br/> Column: Days with restrictions grouped.Face coverings required<br/> Column: Days with restrictions grouped.International travel controls<br/> Column: Days with restrictions grouped.Public transport closures<br/> Column: Days with restrictions grouped.Stay at home requirements<br/> Column: Days with restrictions grouped.Workplace closures<br/> Measure: Countries.GDP % chg 2020<br/> Column: Days with restrictions grouped.Domestic travel restrictions<br/> Column: Days with restrictions grouped.Restrictions on gathering<br/> Column: Days with restrictions grouped.School closures | 

[Up](#)




### Container 7507a59db08eb2d58b93 

| Param  | Value  |
|---|---|
| **Name:** | `7507a59db08eb2d58b93` |
| **Type:** | `tableEx` |
| **Business objects:**  | `Countries` | 
| **Attributes:**  | Column: Countries.FlagURL<br/> Column: Countries.COUNTRY<br/> Measure: Countries.GDP % chg 2020<br/> Measure: Countries.GDP Chg | 

[Up](#)




### Container 28497ae5645b04155012 

| Param  | Value  |
|---|---|
| **Name:** | `28497ae5645b04155012` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 1ddf294d2d54909ec333 

| Param  | Value  |
|---|---|
| **Name:** | `1ddf294d2d54909ec333` |
| **Type:** | `columnChart` |
| **Business objects:**  | `Dates, OWID COVID data` | 
| **Attributes:**  | Column: Dates.Date<br/> Measure: OWID COVID data.Cases 7d Avg per country | 

[Up](#)




### Container e6ce8ed40526535cc309 

| Param  | Value  |
|---|---|
| **Name:** | `e6ce8ed40526535cc309` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container c07e7e491e0a58569580 

| Param  | Value  |
|---|---|
| **Name:** | `c07e7e491e0a58569580` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container 47930533e5822735e855 

| Param  | Value  |
|---|---|
| **Name:** | `47930533e5822735e855` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)




### Container b34f69cce14e02b9e38c 

| Param  | Value  |
|---|---|
| **Name:** | `b34f69cce14e02b9e38c` |
| **Type:** | `['n/a']` |
| **Business objects:**  | `n/a` | 
| **Attributes:**  | n/a | 

[Up](#)


## Page 1

| Param  | Value  |
|---|---|
| **ID** | `` |
| **Name** | `ReportSection989e3ae600f744fd8393` |
| **Display Name** | `Page 1` |
| **Filters** | `[]` |
| **Ordinal** | `8` |
| **Visual containers number** | `1` |

[Up](#)



### Container 3968ccbce331cc920617 

| Param  | Value  |
|---|---|
| **Name:** | `3968ccbce331cc920617` |
| **Type:** | `clusteredColumnChart` |
| **Business objects:**  | `Countries` | 
| **Attributes:**  | Aggregation: Sum(Countries.Population) | 

[Up](#)







----
<p align="center">
Generated at 05.01.2024 00:32:03 by <a href='https://github.com/dop12/pbix_doc'>PBIX DOC PROJECT</a> Git version: 
</p>