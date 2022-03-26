"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 26 February 2022
Last Modified by  : Sylvester Francis
"""
import sys
sys.path.append("..")
import backend.User as user
from getpass import getpass
from helper import clear
userTypes = {1:'Tenant',2:'Owner',3:'Staff'}

''' Login helper
Purpose: The below function is used as a helper function for login 
Params : None
Return value : None
'''
def login_helper():
    clear()
    print("\n ********************************************************************************** \n")
    print(" \n Login")
    print("\n ********************************************************************************** \n")
    username = input("\n Enter your username: ")
    password = getpass("\n Enter the password: ")
    print(username,password)

def signup_helper():
    clear()
    print("\n ********************************************************************************** \n")
    print(" \n Signup")
    print("\n ********************************************************************************** \n")
    firstname = input("\nEnter your First Name: ")
    lastname  = input("\nEnter your Last Name:  ")
    email     = input("\n Enter your Email ID:  ")
    username  = input("\n Enter your preferred username: ")
    password  = getpass("\n Enter your password: ")
    confirmpassword = getpass("\n Re-enter the password: ")
    if password == confirmpassword:
        print("\n Password matches")
    else:
        print("\n Password doesnot match")
    select_userType = input("\n Please select the type of user: \n1.Tenant \n2.Owner \n3.Staff \n Please type one of the following options(1,2 or 3)")
    userType =''
    if select_userType == '1':
        userType = userTypes[1]
    elif select_userType == '2':
        userType= userTypes[2]
    elif select_userType == '3':
        userType= userTypes[3]
    else:
        print("\n Invalid option")
    phno = input("\n Enter your phone number: ")
    data = {}
    data.update({'FirstName':firstname,'LastName':lastname,'email':email,'username':username,'password':password,'userType':userType,'phoneNumber':phno})
    print(data)
    

    

