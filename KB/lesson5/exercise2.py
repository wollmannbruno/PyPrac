#!/usr/bin/env python

import random


def random_ip(base_net='10.10.10.'):
    last_octet = str(random.randint(1, 254))
    host_ip = base_net + last_octet
    return host_ip


print()
print(random_ip())
print(random_ip('172.17.44.'))
print(random_ip(base_net='192.168.4.'))
print()
