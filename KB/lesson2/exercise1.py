#!/usr/bin/env python

f = open('show_version.txt')
entire_file = f.read()
print('\n')
print(entire_file)
print('\n')
print('The variable that contains the entire file is of type {}'.format(type(entire_file)))
print('\n')
f.close()


with open('show_version.txt') as f:
    all_lines = f.readlines()

print('\n')
print(all_lines)
print('\n')
print('The variable that contains all the lines is of type {}'.format(type(all_lines)))
print('\n')
