----

 [Home](../home.md) > [AdventureWorks_Sales](index.md)

----
[[_TOC_]]

# Information

Documentation for file **AdventureWorks_Sales.pbix**.

# Model information
{% if properties %}

| Param  | Value  |
|---|---|
| **Catalog name** | `{{properties['CATALOG_NAME']}}` | 
| **Port** | `{{port}}`|
| **Description** | `{{properties['DESCRIPTION']}}` | 
| **Date modified** | `{{properties['DATE_MODIFIED']}}` | 
| **Compatibility level** | `{{properties['COMPATIBILITY_LEVEL']}}` | 


<details>
<summary>Detail information</summary>

| Param  | Value  |
|---|---|
| **Catalog name** | `{{properties['CATALOG_NAME']}}` | 
| **Port** | `{{port}}` |
| **Full filename** | `{{full_filename}}` |
| **Description** | `{{properties['DESCRIPTION']}}` | 
| **Roles** | `{{properties['ROLES']}}` | 
| **Date modified** | `{{properties['DATE_MODIFIED']}}` | 
| **Compatibility level** | `{{properties['COMPATIBILITY_LEVEL']}}` | 
| **Type** | `{{properties['TYPE']}}` | 
| **Version** | `{{properties['VERSION']}}` | 
| **Database id** | `{{properties['DATABASE_ID']}}` | 
| **Database guid** | `{{properties['DATABASE_GUID']}}` | 
| **Date queried** | `{{properties['DATE_QUERIED']}}` | 
| **Currently used** | `{{properties['CURRENTLY_USED']}}` | 
| **Popularity** | `{{properties['POPULARITY']}}` | 
| **Weightedpopularity** | `{{properties['WEIGHTEDPOPULARITY']}}` | 
| **Clientcacherefreshpolicy** | `{{properties['CLIENTCACHEREFRESHPOLICY']}}` | 
| **Encryption level** | `{{properties['ENCRYPTION_LEVEL']}}` | 

</details>

{% else %}
There are no model information or we have insufficient permissions.
{% endif %}

# Model relationships

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

# Business object

<details>
<summary>Calculated</summary>


</details>
# Model commpm common






- analytics object [Customer](./SSAS__ssas_azure/analytics_object_Customer.md)
- analytics object [Date](./SSAS__ssas_azure/analytics_object_Date.md)
- analytics object [Geography](./SSAS__ssas_azure/analytics_object_Geography.md)
- analytics object [Product](./SSAS__ssas_azure/analytics_object_Product.md)
- analytics object [ProductCategory](./SSAS__ssas_azure/analytics_object_ProductCategory.md)
- analytics object [ProductSubcategory](./SSAS__ssas_azure/analytics_object_ProductSubcategory.md)
- analytics object [InternetSales](./SSAS__ssas_azure/analytics_object_InternetSales.md)



{% if views %}
Ano
{% else %}
There are no views in database or we have insufficient permissions.
{% endif %}

----
{% include "footer.md" %}