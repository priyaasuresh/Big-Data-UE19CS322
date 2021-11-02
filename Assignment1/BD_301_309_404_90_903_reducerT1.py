#!/usr/bin/env python3

import sys as s

present_value=0
present_key=None

for l in s.stdin:
    l=l.strip()
    key,val=l.split('\t',1)
    try:
        val=(int)(val)
        key=(int)(key)
    except ValueError:
        continue

    temp= present_key==key
    if(temp):
         present_value+=1
    else:
        if(present_key in range(0,24) ):
            print('%s\t%s' % ( present_key, present_value))
        present_value=val
        present_key=key
if( present_key):
    print('%s\t%s' % ( present_key,  present_value))
