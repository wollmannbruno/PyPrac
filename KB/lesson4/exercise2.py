#!/usr/bin/env python

houston_dc = [
    '172.30.4.5',
    '172.20.4.5',
    '172.16.8.252',
    '10.10.1.4',
    '10.77.67.30',
    '10.137.18.99',
    '192.168.14.31',
    '192.168.88.71',
    '192.168.168.254',
    '172.20.4.5',
    '10.137.18.99',
    '192.168.14.31',
]

atlanta_dc = [
    '172.30.4.5',
    '172.20.4.5',
    '172.16.8.252',
    '192.168.144.144',
    '192.168.9.9',
    '192.168.254.254',
    '10.199.200.201',
    '10.250.249.248',
    '10.48.47.46',
]

chicago_dc = [
    '192.168.14.31',
    '192.168.88.71',
    '192.168.168.254',
    '10.199.200.201',
    '10.250.249.248',
    '10.48.47.46',
    '172.17.248.99',
    '172.28.47.64',
    '172.27.66.88',
    '172.30.4.5',
]

houston_dc = set(houston_dc)
atlanta_dc = set(atlanta_dc)
chicago_dc = set(chicago_dc)

print()
print('Addresses in both Houston and Atlanta: {}'.format(houston_dc & atlanta_dc))
print('Addresses in all 3 DCs: {}'.format(houston_dc & atlanta_dc & chicago_dc))
print('Addresses unique to Chicago: {}'.format(chicago_dc - houston_dc - atlanta_dc))
print()
