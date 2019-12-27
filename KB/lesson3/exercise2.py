#!/usr/bin/env python

with open('show_arp.txt') as f:
    lines = f.readlines()

counter = 0
print('\n')
for line in lines:
    if line.startswith('P'):
        continue

    line = line.split()
    ip = line[1]
    mac = line[3]

    if ip == '10.220.88.1':
        print('Default gateway IP/Mac: {}/{}'.format(ip, mac))
        counter += 1
        if counter > 1:
            break

    if ip == '10.220.88.30':
        print('Arista3 IP/Mac is: {}/{}'.format(ip, mac))
        counter += 1
        if counter > 1:
            break

print('\n')
