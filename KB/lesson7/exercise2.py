#!/usr/bin/env python

import jinja2

ospf_vars = {
    'ospf_process_id': 10,
    'ospf_priority': 100,
    'ospf_active_interfaces': ['Vlan1', 'Vlan2'],
    'ospf_area0_networks': ['10.10.10.0/24', '10.10.20.0/24', '10.10.30.0/24'],
}

ospf_template_file = 'ospf_template.j2'
with open(ospf_template_file) as f:
    ospf_template = f.read()

template = jinja2.Template(ospf_template)
print(template.render(ospf_vars))
