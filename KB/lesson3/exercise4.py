#!/usr/bin/env python

arp_table = [
    ('10.220.88.1', '0062.ec29.70fe'),
    ('10.220.88.20', 'c89c.1dea.0eb6'),
    ('10.220.88.21', '1c6a.7aaf.576c'),
    ('10.220.88.28', '5254.aba8.9aea'),
    ('10.220.88.29', '5254.abbe.5b7b'),
    ('10.220.88.30', '5254.ab71.e119'),
    ('10.220.88.32', '5254.abc7.26aa'),
    ('10.220.88.33', '5254.ab3a.8d26'),
    ('10.220.88.35', '5254.abfb.af12'),
    ('10.220.88.37', '0001.00ff.0001'),
    ('10.220.88.38', '0002.00ff.0001'),
    ('10.220.88.39', '6464.9be8.08c8'),
    ('10.220.88.40', '001c.c4bf.826a'),
    ('10.220.88.41', '001b.7873.5634')]

print('\n')

mac = []
new_mac = []
for x in arp_table:
    mac = (x[1])
    elements = mac.split('.')
    new_mac = []
    for part in elements:
        part_list = list(part.upper())
        part_list.insert(2, ':')
        part_list = ('').join(part_list)
        new_mac.append(part_list)

    new_mac = (':').join(new_mac)
    print(new_mac)

print('\n')
