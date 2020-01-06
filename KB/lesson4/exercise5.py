#!/usr/bin/env python

import re

with open('show_ipv6_intf.txt') as f:
    show_int = f.read()

ipv6_addr = re.search(r'IPv6 address:(.*)IPv6 subnet:', show_int, re.DOTALL).group(1)
ipv6_addr = ipv6_addr.split()
print()
for x in ipv6_addr:
    if ':' in x:
        print(x)

print()
