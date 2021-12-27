#!/usr/bin/env python
import pandas as pd

def boxing_day(list1):
    #build the initial dataframe
    frame1 = pd.DataFrame(data=list1)
    return(frame1)

def build_two(in_len):
    #determine the elements to add to the dataframe
    print(in_len)
    new_record = []
    while len(new_record) < in_len:
        written_in = input("What do you want to add: ")
        new_record.append(written_in)
    boxing_add(new_record)

def boxing_add(list2):
    #append the new list to the existing dataframe
    if len(list2) != len(boxing_out):
        print("lengths of the two lists are not the same "+ str(len(list2))+" vs "+str(len(boxing_out)))
    else:
        print('The Lists are equal, this should work')
        boxing_out.insert(1,'appended',list2)

lsi = ['Hello','this','is','a','quick','and','dirty','program','I','built','on','Boxing', 'day', '2021']

# lsi = ['Quick', 'program','here']

if __name__ == '__main__':
    boxing_out = (boxing_day(lsi))
    in_length = len(boxing_out)
    build_two(in_length)
    boxing_out = build_two(in_length)

    print(boxing_out)