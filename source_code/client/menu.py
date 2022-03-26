"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 27 February 2022
Last Modified date : 27 February 2022
Last Modified by  : Sylvester Francis
"""
from userhelper import *



'''Main menu 
Purpose: The below function is used to display the main menu 
Params : None
Return value : None
'''
def menu():
    print("\n ********************************************************************************** \n")
    print(" \n Welcome to the Real Estate Rental Management System")
    print(" \n Please choose one of the following options to continue")
    print("\n ********************************************************************************** \n")
    print("\n 1. Login ")
    print("\n 2. Signup ")
    print("\n 3. Exit application")
    print("\n ********************************************************************************** \n")
    choice = input("\n Please enter your option ")
    if choice == '1':
        login_helper()
    elif choice == '2':
        signup_helper()
    elif choice == '3':
        exit_application()
    else:
        print("Invalid option please run the application again")
        sys.exit(1)

def exit_application():
    print("\n Exiting the application")
    sys.exit(1)

if __name__ =='__main__':
    menu()
