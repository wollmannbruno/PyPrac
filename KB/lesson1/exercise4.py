#!/usr/bin/env python

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

no_lead_trail_whitespace = show_version.strip()
show_version_fields = no_lead_trail_whitespace.split()

model_no = show_version_fields[1]
serial_no = show_version_fields[-1]

is_cisco = 'Cisco'.casefold() in model_no.casefold()
is_881 = '881' in model_no

print ()
print ('Original string: "{}"'.format(show_version))
print ()
print ('Remove all leading and trailing whitespace from the string: "{}"'.format(no_lead_trail_whitespace))
print ('Split string: {}'.format(show_version_fields))
print ()
print ('Check if "Cisco" is contained in the model string (ignore capitalization): {}'.format(is_cisco))
print ('Check if "881" is in the model string: {}'.format(is_881))
print ()
print ('The serial number is {}'.format(serial_no))
print ('The model number is {}'.format(model_no))
print ()
