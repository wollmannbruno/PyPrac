#!/usr/bin/env python

ip_addr = input('Please enter an IP address: ')

octets = ip_addr.split('.')
octets_bin = []
octets_hex = []

# for loop not introduced in course yet, but decided to use it anyway
for x in octets:
	octets_bin.append(bin(int(x)))
	octets_hex.append(hex(int(x)))

header = ['Octet1', 'Octet2', 'Octet3', 'Octet4']

print ()
print ('{:^15}{:^15}{:^15}{:^15}'.format(*header))
print ('-' * 60)
print ('{:^15}{:^15}{:^15}{:^15}'.format(*octets))
print ('{:^15}{:^15}{:^15}{:^15}'.format(*octets_bin))
print ('{:^15}{:^15}{:^15}{:^15}'.format(*octets_hex))
print ('-' * 60)
print ()
