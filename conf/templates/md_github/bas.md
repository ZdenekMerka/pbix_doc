----

[Home](./index.md) >  [Business objects](./bas.md)

----

# All Business objects
{% if tables_global %}
| Name | PBIX File name | ID | Description | 
|----|------|-------------|
{% for i  in tables_global if not i.IsHidden -%}
| {{i.Name}} | [{{i.filename}}]({{urlquote(i.filename)}}_dmv.md) | {{ i.ID }} | {{re_nan(i.Description)}} |
{% endfor -%}

{% else %}
There are no business objects information or we have insufficient permissions.
{% endif %}

[Up](#all-business-objects)

{% include "footer.md" %}