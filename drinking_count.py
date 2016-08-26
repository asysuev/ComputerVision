
import os, sys
def add_drink(count1, count2):
    x = 0
    while 1:
        x = raw_input('team number ')
        if int(x) == 1:
            count1+=1
        if int(x) == 2:
            count2+=1
        if int(x) == 3:
            break
    return (count1, count2)
