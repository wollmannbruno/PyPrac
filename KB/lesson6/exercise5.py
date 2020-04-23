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

cmd = 'show ip arp'

net_connect = ConnectHandler(**switch_1)
output = net_connect.send_command(cmd, use_textfsm=True)
net_connect.disconnect()

print('-' * 40)
print(output)
