----

[Home](../index.md) 

----

# Home PBIX Doc

Information from PBIX files.

## Links to PBIX files documentation
{% if filenames_pbix %}
{% for i  in filenames_pbix -%}

* [{{i}}](./{{i}}) 
{%- endfor -%}
{% endif -%}

{% include "footer.md" %}