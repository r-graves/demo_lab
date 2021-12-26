#!/usr/bin/env python
import pandas as pd

def boxing_day(list1):
    frame1 = pd.DataFrame(list1)
    return(frame1)

lsi = ['Hello','this','is','a','quick','and','dirty','program','I','built','on','Boxing', 'day', '2021']

boxing_out = (boxing_day(lsi))

print(boxing_out)