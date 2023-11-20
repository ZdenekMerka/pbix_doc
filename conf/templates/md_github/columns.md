# Columns 

| ID| TABLE_ID | EXPLICIT_NAME | INFERRED_NAME  | EXPLICIT_DATA_TYPE | INFERRED_DATA_TYPE | DATA_CATEGORY | DESCRIPTION | IS_HIDDEN | STATE | IS_UNIQUE | IS_KEY | IS_NULLABLE | ALIGNMENT | TABLE_DETAIL_POSITION | IS_DEFAULT_LABEL | IS_DEFAULT_IMAGE | SUMMARIZE_BY | COLUMN_STORAGE_ID | TYPE | SOURCE_COLUMN | COLUMN_ORIGIN_ID | EXPRESSION | FORMAT_STRING | IS_AVAILABLE_IN_MDX | SORT_BY_COLUMN_ID | ATTRIBUTE_HIERARCHY_ID | MODIFIED_TIME | STRUCTURE_MODIFIED_TIME | REFRESHED_TIME | SYSTEM_FLAGS | KEEP_UNIQUE_ROWS | DISPLAY_ORDINAL | ERROR_MESSAGE | SOURCE_PROVIDER_TYPE | DISPLAY_FOLDER |
|--------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|
{% for i  in columns -%}
| <span id = {{i.ID}}>{{i.ID}}</span> | [{{ i.TableID}}](./table_{{i.TableID}}) | {{ i.ExplicitName}} | {{ i.InferredName }} | {{i.ExplicitDataType}} | {{i.InferredDataType}} | {{i.DataCategory}} | {{i.Description}} |  {{i.IsHidden}} |  {{i.State}} |  {{i.IsUnique}} |  {{i.IsKey}} |  {{i.IsNullable}} |  {{i.Alignment}} |  {{i.TableDetailPosition}} |  {{i.IsDefaultLabel}} |  {{i.IsDefaultImage}} |  {{i.SummarizeBy}} |  {{i.ColumnStorageID}} |  {{i.Type}} |  {{i.SourceColumn}} |  {{i.ColumnOriginID}} |  {{i.Expression}} |  {{i.FormatString}} |  {{i.IsAvailableInMDX}} |  {{i.SortByColumnID}} |  {{i.AttributeHierarchyID}} |  {{i.ModifiedTime}} |  {{i.StructureModifiedTime}} |  {{i.RefreshedTime}} |  {{i.SystemFlags}} |  {{i.KeepUniqueRows}} |  {{i.DisplayOrdinal}} |   {{i.ErrorMessage}} |   {{i.SourceProviderType}} |   {{i.DisplayFolder}} |  
{% endfor -%}

{# all possible columns of columns 
ID
TableID
ExplicitName
InferredName
ExplicitDataType
InferredDataType
DataCategory
Description
IsHidden
State
IsUnique
IsKey
IsNullable
Alignment
TableDetailPosition
IsDefaultLabel
IsDefaultImage
SummarizeBy
ColumnStorageID
Type
SourceColumn
ColumnOriginID
Expression
FormatString
IsAvailableInMDX
SortByColumnID
AttributeHierarchyID
ModifiedTime
StructureModifiedTime
RefreshedTime
SystemFlags
KeepUniqueRows
DisplayOrdinal
ErrorMessage
    SourceProviderType
    DisplayFolder
    EncodingHint
    RelatedColumnDetailsID
    AlternateOfID
    LineageTag
    SourceLineageTag
#}