#!/usr/bin/env python


def ssh_conn(ip_addr, username, password):
    print('The IP ADDRESS is: {}'.format(ip_addr))
    print('The USERNAME is: {}'.format(username))
    print('The PASSWORD is: {}'.format(password))


print()
print('-' * 40)
ssh_conn('10.8.34.8', 'admin', 'Cisco123')
print('-' * 40)
ssh_conn(username='root', password='Juniper123', ip_addr='172.30.4.33')
print('-' * 40)
ssh_conn('192.168.106.254', 'Shrek', password='Fiona')
print('-' * 40)
print()
