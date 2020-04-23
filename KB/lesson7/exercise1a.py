#!/usr/bin/env python

import jinja2

vlan_vars = {
    'vlan_number': '400',
    'vlan_name': 'red400',
}

vlan_template = '''

vlan {{ vlan_number }}
  name {{ vlan_name }}

'''

template = jinja2.Template(vlan_template)
print(template.render(vlan_vars))
