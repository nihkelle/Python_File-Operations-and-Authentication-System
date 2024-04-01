#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Nihkelle Scott


# In[2]:


# Code 01 
import csv
try:
    with open('multi.csv', 'r') as inputFile:
        inputCSV = csv.reader(inputFile)
        for row in inputCSV:
            currentRowContests = set(row)
except FileNotFoundError:
    print("File not found.")


# In[5]:


# Code 02
loginData = {"admin": "password", "user52": "1234", "support": "Support" }
userName = input("Enter username: ")
passWord = input("Enter password: ")
if userName in loginData:
    if loginData[userName] == passWord:
        print("Password matches. Login allowed.")
    else:
        print("Invalid login.")
        with open('login_error_log.txt', 'w') as loginErrorOutput:
            loginErrorOutput.write("Invalid login: " + userName)
else:
    print("User not found.")


# In[ ]:




