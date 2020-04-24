#!/usr/bin/env python

import jinja2

isakmp_vars = {
    'encryption_type': 'aes',
    'dh_group': '5',
    'isakmp_enable': True,
}

isakmp_template = '''

{% if isakmp_enable %}
crypto isakmp policy 10
  encr {{ encryption_type }}
  authentication pre-share
  group {{ dh_group }}
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}

'''

template = jinja2.Template(isakmp_template)
print(template.render(isakmp_vars))
