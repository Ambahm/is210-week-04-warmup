#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')  # getting input from user
MAX_LENGTH = 80
LONGSTR = 'short'
LENOUTPUT = len(MYINPUT)                  # Checking length of string variable
print LENOUTPUT                           # Verifying the numbers <=80
# You code goes here

if LENOUTPUT > MAX_LENGTH:                # condition if length >80 characters
    LONGSTR = 'long'

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
