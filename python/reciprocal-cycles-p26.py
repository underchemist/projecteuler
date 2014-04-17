#!/usr/bin/python

def find_pattern(s):
    for i,d in enumerate(s):
        jump = 1
        if d == s[i+jump]:
            r_unit = s[i:i+jump]
            if r_unit == s[i+jump:i+2*jump]:
                return r_unit
        else:
            jump += 1
