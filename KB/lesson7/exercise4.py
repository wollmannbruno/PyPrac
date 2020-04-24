#!/usr/bin/env python

import jinja2
import yaml
from pprint import pprint

yaml_file = 'int_dict.yml'
with open(yaml_file) as f:
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)

jinja_file = 'int_config.j2'
with open(jinja_file) as f:
    int_template = f.read()

template = jinja2.Template(int_template)
print(template.render(yaml_data))
