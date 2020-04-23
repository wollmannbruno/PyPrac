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

cmds = ['logging monitor 6', 'ip domain-name brunowollmann.com']

net_connect = ConnectHandler(**switch_1)
output1 = net_connect.send_config_set(cmds)
output2 = net_connect.send_config_from_file('changes.txt')
net_connect.disconnect()

print('-' * 40)
print(output1)
print('-' * 40)
print(output2)
