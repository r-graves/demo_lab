#!/usr/bin/env python
import pandas as pd

def boxing_day(list1):
    frame1 = pd.DataFrame(list1)
    return(frame1)

def build_two(in_len):
    print(in_len)
    new_record = []
    while len(new_record) < in_len:
        written_in = input("What do you want to add: ")
        new_record.append(written_in)
    return(new_record)

def boxing_add(list2):
    if len(list2) != len(boxing_out):
        print("lengths of the two lists are not the same "+ str(len(list2))+" vs "+str(len(boxing_out)))
    else:
        print('The Lists are equal, this should work')
        boxing_out.insert(1,'new_var',list2)

#lsi = ['Hello','this','is','a','quick','and','dirty','program','I','built','on','Boxing', 'day', '2021']
lsi = ['Quick', 'program','here']

boxing_out = (boxing_day(lsi))
in_length = len(boxing_out)
list2 = build_two(in_length)
boxing_add(list2)
print(boxing_out)