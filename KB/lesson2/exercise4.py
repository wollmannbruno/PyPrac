#!/usr/bin/env python

with open('show_ip_int_brief.txt') as f:
    ints = f.readlines()

fast4 = ints[5].split()
intfast4 = (fast4[0], fast4[1])

print('\n')
print(intfast4)
print('\n')
