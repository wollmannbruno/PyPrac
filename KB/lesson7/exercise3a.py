#!/usr/bin/env python

import yaml

yaml_file = 'int_list.yml'
with open(yaml_file) as f:
    contents = yaml.load(f, Loader=yaml.FullLoader)

print(contents)
