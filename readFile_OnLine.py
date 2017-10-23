# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:44:07 2017

@author: Ma Xuelin
"""

from os.path import exists, getmtime, getsize
import time

def load_data():  # a Demo for load_data
    print 'load data!'
    return 0


filename = 'result.mat'   #set the filePath and fileName
while True:
    if exists(filename): # if the file exits, then get the mtime(file's edit time) 
        oldMTime = getmtime(filename)
        flag = 1 # flag for the next 'while'
        break
    else:
        flag = 0

while flag:
    if exists(filename):   # if the file exits, continue
        if getsize(filename): # if the file is not empty, continue
            if oldMTime != getmtime(filename): # if the file's mtime change, then read the new data
                load_data()
                oldMTime = getmtime(filename)
                break
            else:
                time.sleep(0.4) # if the file doesn't change, wait 0.4s
        else:
            time.sleep(0.1)# the file exits but empty, wait 0.1s
    else:
        time.sleep(0.4)# the file doesn't exit, wait 0.4s
        