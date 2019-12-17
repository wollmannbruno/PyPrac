#!/usr/bin/env python

print('\n')
ip_addrs = ['172.20.0.44', '172.20.4.8', '10.2.176.34', '10.3.209.99', '192.168.54.185']
print('Original list:\n{}'.format(ip_addrs))

ip_addrs.append('192.168.106.63')
print('\nAppending 1 address:\n{}'.format(ip_addrs))

ip_addrs.extend(['10.88.13.1', '172.30.114.5'])
print('\nExtending with 2 addresses:\n{}'.format(ip_addrs))

ip_addrs = ip_addrs + ['8.8.8.8', '172.30.22.43']
print('\nConcatenating with 2 address:\n{}'.format(ip_addrs))

print('\nEntire list:\n{}'.format(ip_addrs))

print('\n')
print('1st address: {}'.format(ip_addrs[0]))
print('Last address: {}'.format(ip_addrs[-1]))
print('Pop 1st address: {}'.format(ip_addrs.pop(0)))
print('Pop last address: {}'.format(ip_addrs.pop()))

ip_addrs[0] = '2.2.2.2'
print('New 1st address: {}'.format(ip_addrs[0]))
print('\n')
