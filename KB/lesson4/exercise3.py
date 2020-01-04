#!/usr/bin/env python

import re

with open('show_version.txt') as f:
    version = f.read()

os_version = re.match('.*Version (.*),', version).group(1)
serial_no = re.search('Processor board ID (.*)$', version, re.M).group(1)
config_reg = re.search('Configuration register is (.*)$', version, re.M).group(1)

print()
print('OS Version: {}'.format(os_version))
print('Serial Number: {}'.format(serial_no))
print('Config Register: {}'.format(config_reg))
print()
