#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

# logical opertor boolean() check

if (LOOKS_NICE is True and EXPENSE <= MAX_EXPENSE)or GET_OUT_ALIVE is False:
    SACRIFICE = True    # Result is true if 'and' and one of the 'or' is TRUE

print SACRIFICE
