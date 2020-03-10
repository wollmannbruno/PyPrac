#!/usr/bin/env python
import pdb

macs = [
    'c89c.1dea.0eb6',
    '1c6a.7aaf.576c',
    '5254.aba8.9aea',
    '5254.abbe.5b7b',
    '52-54-ab-71-e1-19',
    '52-54-ab-c7-26-aa',
    '5254.ab3a.8d26',
    '5254.abfb.af12',
    '00-01-00-ff-00-01',
    '00-02-00-ff-00-01',
    '64-4-b-e8-8-c8',
    '001c.c4bf.826a',
    '001b.7873.5634',
    'a:b:c:d:e:f',
    '80:e6:50:d:3f:f0',
    '4e:2a:de:97:f:e9',
    '82:f:13:9b:4a:81',
    'blahblahblah'
]


def mac_normalize(mac_addr):
    normal_mac = []
    parts = []
    if ':' in mac_addr:
        components = mac_addr.split(':')
        for x in components:
            if len(x) == 1:
                x = '0' + x
            parts.append(x)
        normal_mac = ':'.join(parts).upper()

    elif '-' in mac_addr:
        components = mac_addr.split('-')
        for x in components:
            if len(x) == 1:
                x = '0' + x
            parts.append(x)
        normal_mac = ':'.join(parts).upper()

    elif '.' in mac_addr:
        components = mac_addr.split('.')
        for x in components:
            parts = list(x.upper())
            parts.insert(2, ':')
            parts = ('').join(parts)
            normal_mac.append(parts)
        normal_mac = (':').join(normal_mac)

    else:
        normal_mac = 'INVALID MAC ADDRESS'

    return normal_mac


print()
for addr in macs:
    pdb.set_trace()
    print('{:<20} = {:>20}'.format(addr, mac_normalize(addr)))
print()
