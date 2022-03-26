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