#!/usr/bin/env python

with open('show_vlan.txt') as f:
    lines = f.readlines()

vlans = []

for line in lines:
    if line.startswith('V') or line.startswith('-') or line.startswith(' '):
        continue

    components = line.split()
    pair = (components[0], components[1])
    vlans.append(pair)

print('\n')
print(vlans)
print('\n')
