----

[Home](./index.md) > [{{filename}}_report]({{urlquote(filename)}}_report.md)

|[Report sections](#report-sections) |

----


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


{% include "footer.md" %}