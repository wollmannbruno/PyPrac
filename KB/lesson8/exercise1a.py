#!/usr/bin/env python

import datetime
import ipaddress
import sys
from pprint import pprint

print('-' * 50)
print('datetime file')
print(datetime.__file__)
print('-' * 50)
print('ipaddress file')
print(ipaddress.__file__)
print('-' * 50)
print('sys path')
pprint(sys.path)
