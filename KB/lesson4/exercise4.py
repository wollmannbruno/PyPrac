#!/usr/bin/env python

import re

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

model = re.search(r'^Cisco (?P<name>\d+)', show_version, re.M).group('name')
memory = re.search(r'with (?P<memory>.*) b', show_version, re.M).group('memory')

print()
print('Model Number: {}'.format(model))
print('Memory: {}'.format(memory))
print()
