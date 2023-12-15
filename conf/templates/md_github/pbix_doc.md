----

[Home](./index.md) > [{{filename}}]({{filename}}.md)

[Information](#information) | [Model information](#model-information) | [Model relationships](#model-relationships) | [Report sections](#report-sections) | [Business objects](#business-objects) | [Measures](#measures) | [Relationships](#relationships) | [Hierarchies](#hierarchies) | [Columns](#columns) | 

----

# Information

Documentation for file **{{filename}}**.

# Model information
{% if properties %}

| Param  | Value  |
|---|---|
| **Analyzed pbix file name** | `{{filename}}` | 
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
{%- if i.IsActive -%} id{{i.ToTableID}}(["{{str_slicer(tables_idx[str(i.ToTableID)]['Name'])}}[{{columns_idx[str(i.ToColumnID)]['ExplicitName']}}]"]) --> id{{i.FromTableID}}(["{{str_slicer(tables_idx[str(i.FromTableID)]['Name'])}}[{{columns_idx[str(i.FromColumnID)]['ExplicitName']}}]"])
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

# Report sections
{% if report_sections %}
{% for i in report_sections -%}

## {{i.displayName}}

| Param  | Value  |
|---|---|
| **ID** | `{{i.id}}` |
| **Name** | `{{i.name}}` |
| **Display Name** | `{{i.displayName}}` |
| **Filters** | `{{i.filters}}` |
| **Ordinal** | `{{i.ordinal}}` |
| **Visual containers number** | `{{len(i.visualContainers)}}` |

[Up](#)

{% for c in i.visualContainers  -%}

{% set config = get_visual_config_info(c.config) %}
{% if config %}
### Container {{config['name']}} 

| Param  | Value  |
|---|---|
| **Name:** | `{{config['name']}}` |
| **Type:** | `{{config['type']}}` |
| **Business objects:**  | `{{join(config['entities'])}}` | 
| **Attributes:**  | {{joinnl(config['selected_items'])}} | 

[Up](#)
{% else %}
There are no visual information or we have insufficient permissions.
{% endif %}

{% endfor -%}

{% endfor -%}

{#

#}
{% else %}
There are no report sections information or we have insufficient permissions.
{% endif %}


# Business objects
{% if tables %}
| ID | NAME | DESCRIPTION | 
|----|------|-------------|
{% for i  in tables if not i.IsHidden -%}
| {{ i.ID }} | {{i.Name}} | {{re_nan(i.Description)}} |
{% endfor -%}

{% else %}
There are no business objects information or we have insufficient permissions.
{% endif %}


[Up](#)
# Measures

{% if measures %}
<table>
    <tr>
        <th> ID </th><th> TABLE </th><th> NAME </th><th> DESCRIPTION </th><th> EXPRESSION </th><th> IS_HIDDEN </th><th> STATE </th>
    </tr>
{% for i  in measures if i.Expression != '-NaN-' -%}
    <tr>
        <td> {{ i.ID }} </td><td> {{str_slicer(tables_idx[str(i.TableID)]['Name'])}} </td><td> {{ i.Name}} </td><td> {{ re_nan(i.Description) }} </td><td> <code> {{i.Expression}} </code></td><td> {{i.IsHidden}} </td><td>  {{i.State}} </td> 
    </tr>
{% endfor -%}
</table>
{% else %}
There are no measures or we have insufficient permissions.
{% endif %}



[Up](#)
# Relationships 
{% if relationships %}

| ID | FROM_TABLE | TO_TABLE | FROM:TO CARDINALITY | NAME | IS_ACTIVE  |
|----|------------|----------|---------------------|------|------------|
{% for i  in relationships -%}
| {{ i.ID }} | {{str_slicer(tables_idx[str(i.FromTableID)]['Name'])}}[{{columns_idx[str(i.FromColumnID)]['ExplicitName']}}] | {{str_slicer(tables_idx[str(i.ToTableID)]['Name'])}}[{{columns_idx[str(i.ToColumnID)]['ExplicitName']}}] | {{i.FromCardinality}}:{{i.ToCardinality}} | {{ i.Name}} | {{ i.IsActive }} |
{% endfor -%}

{% else %}
There are no relationships information or we have insufficient permissions.
{% endif %}

[Up](#)
# Hierarchies 

{% if hierarchies %}

| ID | TABLE | NAME | DESCRIPTION  | IS_HIDDEN | 
|----|----------|------|--------------|-----------|
{% for i  in hierarchies -%}
| {{ i.ID }} |{{str_slicer(tables_idx[str(i.TableID)]['Name'])}} | {{ i.Name}} | {{ re_nan(i.Description) }} | {{i.IsHidden}} | 
{% endfor -%}

{% else %}
There are no hierarchies information or we have insufficient permissions.
{% endif %}

[Up](#)
# Columns 

{% if columns %}
<table>
    <tr>
        <th> ID </th><th> TABLE </th><th> EXPLICIT_NAME </th><th> DESCRIPTION </th><th> IS_HIDDEN </th><th> EXPRESSION </th>
    </tr>
{% for i  in columns if not i.IsHidden -%}
    <tr>
        <td> {{i.ID}} </td><td> {{str_slicer(tables_idx[str(i.TableID)]['Name'])}} </td><td> {{str_slicer(i.ExplicitName)}} </td><td> {{re_nan(i.Description)}} </td><td> {{i.IsHidden}} </td><td><code> {{re_nan(i.Expression)}} </code></td>
    </tr>

{% endfor -%}
</table>

{% else %}
There are no columns information or we have insufficient permissions.
{% endif %}

{% include "footer.md" %}