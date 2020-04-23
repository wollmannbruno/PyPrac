#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

print('\n')

username = input('Username: ')
password = getpass()

switch_1 = {
    'device_type': 'cisco_nxos',
    'host': '172.31.1.1',
    'username': username,
    'password': password,
}

switch_2 = {
    'device_type': 'cisco_nxos',
    'host': '172.31.1.8',
    'username': username,
    'password': password,
}

switch_3 = {
    'device_type': 'cisco_nxos',
    'host': '172.31.1.2',
    'username': username,
    'password': password,
}

switch_4 = {
    'device_type': 'cisco_nxos',
    'host': '172.31.1.9',
    'username': username,
    'password': password,
}

cmd = 'show ip arp'

for device in [switch_1, switch_2, switch_3, switch_4]:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(cmd)
    net_connect.disconnect()
    print('-' * 40)
    print(output)
