#!/usr/bin/env python


def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print('-' * 40)
    print('The IP ADDRESS is: {}'.format(ip_addr))
    print('The USERNAME is: {}'.format(username))
    print('The PASSWORD is: {}'.format(password))
    print('The DEVICE TYPE is: {}'.format(device_type))
    print('-' * 40)


print()
ssh_conn2('10.8.34.8', 'admin', 'Cisco123')
ssh_conn2('172.30.4.33', 'root', 'Juniper123', 'juniper')

device = {'ip_addr': '192.168.106.254',
          'username': 'Shrek',
          'password': 'Fiona'}

ssh_conn2(**device)
print()
