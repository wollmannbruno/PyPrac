#!/usr/bin/env python

import jinja2

vlan_vars = {
    'vlan_number': 50,
    'vlan_name': 'blue50',
}

vlan_template = '''

{%- for i in range(1,9) %}
vlan {{ vlan_number }}{{ i }}
  name {{ vlan_name }}{{ i }}
{%- endfor %}

'''

template = jinja2.Template(vlan_template)
print(template.render(vlan_vars))
