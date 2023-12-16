----

[Home](../index.md) 

----

# Home PBIX Doc

Information from PBIX files.

## Links to PBIX files documentation
{% if filenames_pbix %}
{% for i  in filenames_pbix -%}
* [{{i.name}}](./{{urlquote(i.name)}}) generated at {{i.datetime_extracted}} 
{% endfor -%}
{% endif -%}

{% include "footer.md" %}