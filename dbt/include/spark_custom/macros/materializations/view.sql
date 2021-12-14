{% materialization view, adapter='spark_custom' -%}
    {{ return(create_or_replace_view()) }}
{%- endmaterialization %}
