#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""if else statement."""

BL_PRESSURE = int(raw_input('Enter your Blood Pressure : '))

# Take action as per selected menu-option

if BL_PRESSURE <= 89:
    BP_STATUS = 'LOW'
elif BL_PRESSURE <= 119:
    BP_STATUS = 'IDEAL'             # print ("IDEAL BP...")
elif BL_PRESSURE == 139:
    BP_STATUS = 'WARNING'            # print ("...WARNING...")
elif BL_PRESSURE == 159:
    BP_STATUS = 'HIGH'              # print ("...HIGH...")
else:
    BP_STATUS = 'EMERGENCY'          # print ("... EMERGENCY...")

# {}.format(BP_STATUS) gets input from if else statement

BP_STATUS = 'Yor Blood Pressure status is currently {}'.format(BP_STATUS)
print BP_STATUS
