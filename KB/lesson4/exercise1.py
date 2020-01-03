#!/usr/bin/env python

net_device = {'ip_addr': '172.30.4.6',
              'vendor': 'cisco',
              'username': 'admin',
              'password': 'qwerty'}

print()
print('-' * 30)
print(net_device['ip_addr'])

if net_device['vendor'] == 'cisco':
    net_device['platform'] = 'ios'
elif net_device['platform'] == 'juniper':
    net_device['platform'] = 'junos'

bgp_fields = {}
bgp_fields.update({'bgp_as': '65007',
                   'peer_as': '65008',
                   'peer_ip': '172.30.4.6'})

print('-' * 30)
for x in bgp_fields:
    print(x)

print('-' * 30)
for x in bgp_fields:
    print('{} ---> {}'.format(x, bgp_fields[x]))
print('-' * 30)
print()
