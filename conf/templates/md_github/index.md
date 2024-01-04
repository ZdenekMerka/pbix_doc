----

[Home](../index.md) 

----

# Home PBIX Doc

Information from PBIX files.

## Links to PBIX files documentation
{% if filenames_pbix %}
| PBIX File name | DMV | Reports  | generated | 
|---|---|---|---|
{% for i  in filenames_pbix -%}
| {{i.name}} | [DMV](./{{urlquote(i.name)}}) |  [Report](./{{urlquote(i.name)}}_report) | {{i.datetime_extracted}} |
{% endfor -%}
{% endif -%}

{% include "footer.md" %}