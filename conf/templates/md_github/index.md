----

[Home](../home.md) > [{{filename}}](index.md)

[Information](#information) | [Model information](#model-information) | [Model relationships](#model-relationships) | [Business objects](#business-objects) | [Measures](#measures) | [Relationships](#relationships) | [Hierarchies](#hierarchies) | [Columns](#columns) | 

----

# Information

Documentation for file **{{filename}}**.

# Model information
{% if properties %}

| Param  | Value  |
|---|---|
| **Catalog name** | `{{properties['CATALOG_NAME']}}` | 
| **Port** | `{{port}}`|
| **Description** | `{{properties['DESCRIPTION']}}` | 
| **Date modified** | `{{properties['DATE_MODIFIED']}}` | 
| **Compatibility level** | `{{properties['COMPATIBILITY_LEVEL']}}` | 

{% else %}
There are no model information or we have insufficient permissions.
{% endif %}
[Up](#)
# Model relationships
{% if relationships %}
```mermaid
graph LR;

{% for i  in relationships -%}
{%- if i.IsActive -%} id{{i.ToTableID}}(["{{tables_idx[str(i.ToTableID)]['Name']}}[{{columns_idx[str(i.ToColumnID)]['ExplicitName']}}]"]) --> id{{i.FromTableID}}(["{{tables_idx[str(i.FromTableID)]['Name']}}[{{columns_idx[str(i.FromColumnID)]['ExplicitName']}}]"])
{% endif -%}
{#
# {{ i.IsActive }} 
# {{tables_idx[str(i.FromTableID)]['Name']}}[{{columns_idx[str(i.FromColumnID)]['ExplicitName']}}] 
# {{columns_idx[str(i.FromColumnID)]['ExplicitName']}} 
# {{i.FromCardinality}} 
# {{tables_idx[str(i.ToTableID)]['Name']}}[{{columns_idx[str(i.ToColumnID)]['ExplicitName']}}] 
# {{columns_idx[str(i.ToColumnID)]['ExplicitName']}} 
# {{i.ToCardinality}} 
#}
{%- endfor -%}
```

{% else %}
There are no relationships information or we have insufficient permissions.
{% endif %}

[Up](#)
# Business objects
{% if tables %}
| ID| NAME | DESCRIPTION | MODIFIED_TIME | STRUCTURE_MODIFIED_TIME |
|---|-------------|-----------------:|---------------: |---------------:|
{% for i  in tables if not i.IsHidden -%}
| {{ i.ID }} | {{ i.Name}} | {{i.Description}} | {{i.ModifiedTime}} |  {{i.StructureModifiedTime}} |
{% endfor -%}

{% else %}
There are no business objects information or we have insufficient permissions.
{% endif %}


[Up](#)
# Measures

{% if measures %}
| ID | TABLE | NAME | DESCRIPTION | EXPRESSION | IS_HIDDEN | STATE |
|----|-------|------|-------------|------------|-----------|-------|
{% for i  in measures if i.Expression != '-NaN-' -%}
| {{ i.ID }} | {{tables_idx[str(i.TableID)]['Name']}} | {{ i.Name}} | {{ i.Description }} | {{i.Expression}} | {{i.IsHidden}} |  {{i.State}} |  
{% endfor -%}

{% else %}
There are no measures or we have insufficient permissions.
{% endif %}

[Up](#)
# Relationships 
{% if relationships %}

| ID | FROM_TABLE_ID | FROM_CARDINALITY | TO_TABLE_ID | TO_CARDINALITY | NAME | IS_ACTIVE  |
|----|---------------|------------------|-------------|----------------|------|------------|
{% for i  in relationships -%}
| {{ i.ID }} | {{tables_idx[str(i.FromTableID)]['Name']}}[{{columns_idx[str(i.FromColumnID)]['ExplicitName']}}] | {{i.FromCardinality}} | {{tables_idx[str(i.ToTableID)]['Name']}}[{{columns_idx[str(i.ToColumnID)]['ExplicitName']}}] | {{i.ToCardinality}} | {{ i.Name}} | {{ i.IsActive }} |
{% endfor -%}

{% else %}
There are no relationships information or we have insufficient permissions.
{% endif %}

[Up](#)
# Hierarchies 

{% if hierarchies %}

| ID | TABLE_ID | NAME | DESCRIPTION  | IS_HIDDEN | 
|----|----------|------|--------------|-----------|-
{% for i  in hierarchies -%}
| {{ i.ID }} |{{tables_idx[str(i.TableID)]['Name']}} | {{ i.Name}} | {{ i.Description }} | {{i.IsHidden}} | 
{% endfor -%}

{% else %}
There are no hierarchies information or we have insufficient permissions.
{% endif %}

[Up](#)
# Columns 

{% if columns %}
| ID | TABLE_ID | EXPLICIT_NAME | SOURCE_COLUMN | COLUMN_ORIGIN_ID | DATA_CATEGORY | DESCRIPTION | IS_HIDDEN | STATE | IS_UNIQUE | TYPE | EXPRESSION |
|----|----------|---------------|---------------|------------------|---------------|-------------|-----------|-------|-----------|------|------------|
{% for i  in columns -%}
| {{i.ID}} | {{tables_idx[str(i.TableID)]['Name']}} | {{i.ExplicitName}} | {{i.SourceColumn}} | {{i.ColumnOriginID}} | {{i.DataCategory}} | {{i.Description}} | {{i.IsHidden}} | {{i.State}} | {{i.IsUnique}} | {{i.Type}} | {{i.Expression}} |
{% endfor -%}

{% else %}
There are no columns information or we have insufficient permissions.
{% endif %}


----
{% include "footer.md" %}