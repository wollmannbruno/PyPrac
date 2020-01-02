#!/usr/bin/env python

import os

WINDOWS = False
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

print('\n')
base = '.'
while base.count('.') < 3:
    base = input('Enter the base /24 network: ')

network_range = []
for x in range(1, 255):
    network_range.append(base + str(x))

print('\n')
for ind, ip in enumerate(network_range):
    print('{} ---> {}'.format(ind, ip))

print('\n')

ping_range = network_range[2:6]
for host in ping_range:
    os.system('{} {}'.format(base_cmd, host))

print('\n')
