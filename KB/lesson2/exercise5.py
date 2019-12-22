#!/usr/bin/env python

with open('show_ip_bgp_summ.txt') as f:
    show_ip_bgp_summ = f.readlines()

first_line = show_ip_bgp_summ[0]
last_line = show_ip_bgp_summ[-1]
split_first = first_line.split()
split_last = last_line.split()
asn = split_first[-1]
peer = split_last[0]

print('\n')
print('Local ASN = {}'.format(asn))
print('BGP peer = {}'.format(peer))
print('\n')
