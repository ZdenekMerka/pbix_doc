# Relationships 

| ID| MODEL_ID | NAME | IS_ACTIVE  | TYPE | CROSS_FILTERING_BEHAVIOR | JOIN_ON_DATE_BEHAVIOR | RELY_ON_REFERENTIAL_INTEGRITY | FROM_TABLE_ID | FROM_COLUMN_ID |FROM_CARDINALITY |TO_TABLE_ID |TO_COLUMN_ID |TO_CARDINALITY |STATE |RELATIONSHIP_STORAGE_ID |RELATIONSHIP_STORAGE_2_ID |MODIFIED_TIME |REFRESHED_TIME |SECURITY_FILTERING_BEHAVIOR |
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------| 
{% for i  in relationships -%}
| {{ i.ID }} | {{ i.ModelID}} | {{ i.Name}} | {{ i.IsActive }} | {{i.Type}} | {{i.CrossFilteringBehavior}} | {{i.JoinOnDateBehavior}} | {{i.RelyOnReferentialIntegrity}} |  [{{ i.FromTableID}}](./table_{{i.FromTableID}}) |  [{{ i.FromColumnID}}](#{{i.FromColumnID}}) |  {{i.FromCardinality}} |   {{i.ToTableID}} |   {{i.ToColumnID}} |   {{i.ToCardinality}} |   {{i.State}} |   {{i.RelationshipStorageID}} |   {{i.RelationshipStorage2ID}} |   {{i.ModifiedTime}} |   {{i.RefreshedTime}} |   {{i.SecurityFilteringBehavior}} |  
{% endfor -%}

{# all possible columns of columns 
ID
ModelID
Name
IsActive
Type
CrossFilteringBehavior
JoinOnDateBehavior
RelyOnReferentialIntegrity
FromTableID
FromColumnID
FromCardinality
ToTableID
ToColumnID
ToCardinality
State
RelationshipStorageID
RelationshipStorage2ID
ModifiedTime
RefreshedTime
SecurityFilteringBehavior
#}