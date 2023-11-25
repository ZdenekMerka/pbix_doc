{% extends "base.md" %}

{% block index %} views{{file_type}} {% endblock index %}

{% block header %} views {% endblock header %}

{% block TOC %}
[[_TOC_]]
{% endblock TOC %}

{% block content %}
{% if views %}
Ano
{% else %}
There are no views in database or we have insufficient permissions.
{% endif %}

{% endblock content %}