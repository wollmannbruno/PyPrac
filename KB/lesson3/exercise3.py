#!/usr/bin/env python

with open('show_lldp_neighbors_detail.txt') as f:
    lines = f.readlines()

found_name, found_port = (False, False)
for x in lines:
    if x.startswith('System Name'):
        elements = x.split(':')
        sys_name = elements[1].strip()
        found_name = True
    elif x.startswith('Port id'):
        elements = x.split(':')
        port_id = elements[1].strip()
        found_port = True

    if found_name and found_port:
        break

print('\n')
print('System name = {}'.format(sys_name))
print('Port id = {}'.format(port_id))
print('\n')
