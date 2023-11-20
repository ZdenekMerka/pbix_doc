# Measures 
| ID| TABLE_ID | NAME | DESCRIPTION | DATA_TYPE | EXPRESSION | FORMAT_STRING | IS_HIDDEN | STATE | MODIFIED_TIME | STRUCTURE_MODIFIED_TIME | KPIID | IS_SIMPLE_MEASURE | ERROR_MESSAGE | DISPLAY_FOLDER |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
{% for i  in measures -%}
| {{ i.ID }} | [{{ i.TableID}}](./table_{{i.TableID}}) | {{ i.Name}} | {{ i.Description }} | {{i.DataType}} | {{i.Expression}} | {{i.FormatString}} | {{i.IsHidden}} |  {{i.State}} |  {{i.ModifiedTime}} |  {{i.StructureModifiedTime}} |   {{i.KPIID}} |   {{i.IsSimpleMeasure}} |   {{i.ErrorMessage}} |   {{i.DisplayFolder}} |  
{% endfor -%}


{# all possible columns of measures 
DetailRowsDefinitionID
DataCategory
LineageTag
SourceLineageTag
#}