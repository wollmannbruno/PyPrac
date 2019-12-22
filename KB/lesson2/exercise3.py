#!/usr/bin/env python

from pprint import pprint

with open('show_arp.txt') as f:
    arp = f.readlines()

arp = arp[1:]
print('\n')
pprint(arp)

three_arps = arp[:3]
print('\n')
pprint(three_arps)
print('\n')

big_str = '\n'.join(three_arps)
with open('arp_entries.txt', 'w') as f:
    f.write(big_str)
