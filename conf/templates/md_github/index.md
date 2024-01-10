----

[Home](../index.md) 

----

# Home PBIX Doc

Information from PBIX files.

## Global pages 
| Page | Comments | 
|---|---|
| [Business objects](./bas.md) | List of all Business objects sorted by name |
| [Measures](./measures.md) | List of all Measures sorted by name |
| [Columns](./columns.md) | List of all Columns sorted by name |

## Links to PBIX files documentation
{% if filenames_pbix %}
| PBIX File name | DMV | Reports  | generated | 
|---|---|---|---|
{% for i  in filenames_pbix -%}
| {{i.name}} | [DMV](./{{urlquote(i.name_dmv)}}) |  [Report](./{{urlquote(i.name_report)}}) | {{i.datetime_extracted}} |
{% endfor -%}
{% endif -%}

{% include "footer.md" %}