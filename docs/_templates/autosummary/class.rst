{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :members:
   :show-inheritance:
   {#- These classes inherit docstrings from the raw qt source, which generates rst syntax errors when building the docs #}
   {% if objname not in ["progress", "cancelable_progress"] -%}
   :inherited-members:
   {%- endif %}

   {% block methods %}

   {% if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
   {% for item in methods %}
   {% if not item.startswith('_') %}
      ~{{ name }}.{{ item }}
   {% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Attributes') }}

   .. autosummary::
   {% for item in attributes %}
      {{ item|get_attributes(name, module) }}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   .. rubric:: {{ _('Details') }}
