#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# General Libraries
import sys
import clr
import pandas as pd

# Osisoft Libraries 
sys.path.append("C:\\Program Files\\PIPC\\AF\\PublicAssemblies\\4.0\\")
clr.AddReference("Osisoft.AFSDK")
from Osisoft.AF.PI import *
from Osisoft.AF.Search import *
from Osisoft.AF.Asset import *
from Osisoft.AF.Data import *

# connecting on server
def connectToPIServer(piserver):
    try:
        global currentServer
        
        servers = PIServers()
        currentServer = servers[piserver]
            
        # if it was ok, so return success to the user
        print(f"It was connected to the server: {currentServer}")
    except:
        # if it wasn't ok, so return fail to the user
        print(f"It wasn't possible to connect to the server: {currentServer}")
        
        
# Inserting a new value 
def setValueOnTag(tag, value):
    try:
        # inserting in afValue the AFValue() class
        afValue = AFValue()
        
        # inserting the value on afValue.Value
        afValue.Value = value
        
        # trying to find the pi point on the current server
        findPIPoint = PIPoint.FindPIPoint(currentServer, tag)
        
        # updating the value on the tag
        findPIPoint.UpdateValue(afValue, AFUpdateOption.Replace, AFBufferOption.BufferIfPossible)
        
        # if it was ok, so return success to the user
        print("Success")
    except:
        # if it wasn't ok, so return fail to the user
        print("Failed")


# reading file where the tags are defined
file = pd.read_csv("file.csv", sep = ';')

# getting only the column where the tags are
mappedTags = file['column_tagname']

# connecting on server
connectToPIServer("server_name")

print("Start Message")
for tag in mappedTags:
    try:
        # phrase to context the user about the current tag
        print("Insert the value on the tag: " + tag)
        
        # getting input value
        value = float(input("Insert a value: "))
        
        # using this function to insert value on the tag
        setValueOnTag(tag, value)
        
        # if it was ok, so return success to the user
        print("Success")
    except: 
        # if it wasn't ok, so return fail to the user
        print("Failed")

