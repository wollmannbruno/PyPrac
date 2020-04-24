#!/usr/bin/env python

import yaml
from pprint import pprint

yaml_file = 'int_dict.yml'
with open(yaml_file) as f:
    contents = yaml.load(f, Loader=yaml.FullLoader)

pprint(contents)
