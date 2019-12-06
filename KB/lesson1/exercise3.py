#!/usr/bin/env python

from __future__ import print_function, unicode_literals

ip_addr = '2001:db88:dead:beef:abba:2846:aa7b:fff8'
IP_ADDR = '2001:db8::88'
IPv6_addr = '2001:db8:dead:beef:abba::b0b'

print ()
print ('{:39} == {:30} {}'.format(ip_addr, IP_ADDR, ip_addr == IP_ADDR))
print ('{:39} != {:30} {}'.format(ip_addr, IPv6_addr, ip_addr != IPv6_addr))
print ()
