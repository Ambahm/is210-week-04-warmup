#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" rawinput() string value converted to integer """

QUESTION = 'What is the answer to the life the universe and everything? '

# printig question and converting to integer

MY_INTEGER = int(raw_input(QUESTION))
print type(MY_INTEGER)   # Checking type of value stored in variable
