# Hierarchies 

| ID| TABLE_ID | NAME | DESCRIPTION  | IS_HIDDEN | STATE | HIERARCHY_STORAGE_ID | MODIFIED_TIME | STRUCTURE_MODIFIED_TIME | REFRESHED_TIME | DISPLAY_FOLDER |
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
{% for i  in hierarchies -%}
| {{ i.ID }} | [{{ i.TableID}}](./table_{{i.TableID}}) | {{ i.Name}} | {{ i.Description }} | {{i.IsHidden}} | {{i.State}} | {{i.HierarchyStorageID}} | {{i.ModifiedTime}} |  {{i.StructureModifiedTime}} |  {{i.RefreshedTime}} | 
{% endfor -%}


{# all possible columns of Hierarchies
ID
TableID
Name
Description
IsHidden
State
HierarchyStorageID
ModifiedTime
StructureModifiedTime
RefreshedTime
DisplayFolder
    HideMembers
    LineageTag
    SourceLineageTag
#}