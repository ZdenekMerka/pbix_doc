# Tables

| ID| MODEL_ID | NAME | DATA_CATEGORY  | DESCRIPTION | IS_HIDDEN | TABLE_STORAGE_ID | MODIFIED_TIME | STRUCTURE_MODIFIED_TIME | SYSTEM_FLAGS |
|--------------|-------------|-------------|---------------------:|-----------------:|--------------:|----------------:|---------------:|---------------:|---------------:| 
{% for i  in tables -%}
| {{ i.ID }} | {{ i.ModelID}} | {{ i.Name}} | {{ i.DataCategory }} | {{i.Description}} | {{i.IsHidden}} | {{i.TableStorageID}} | {{i.ModifiedTime}} |  {{i.StructureModifiedTime}} |  {{i.SystemFlags}} | 
{% endfor -%}

{# another possible params
ShowAsVariationsOnly
IsPrivate
DefaultDetailRowsDefinitionID
AlternateSourcePrecedence
RefreshPolicyID
CalculationGroupID
ExcludeFromModelRefresh
LineageTag
SourceLineageTag
SystemManaged
#}