"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 28 March 2022
Last Modified by  : Parvathy Suresh
"""

import backend.User as user


'''Tenant Actions'''

def viewProfile(data):
    print(" \n view profile called")
    q = {}
    q['username'] = data['username']
    q['password'] = data['password']
    current_User = user.get_one_user(q)
    print("\n ******************************User Details***************************************** \n")
    print("\n First Name : {0} \n Last Name: {1} \n Email: {2} \n User name: {3} \n Phone Number: {4} ".format(current_User['FirstName'],current_User['LastName'],current_User['email'],current_User['username'],current_User['phoneNumber']))
    print("\n ********************************************************************************** \n")
def viewapartment():
    print("\n view apartment called")
def raise_service_req():
    print("\n raise service req called")
def raise_sublet_req():
    print("\n raise sublet req called")
def pay_rent():
    print("\n pay rent called")

'''Owner Actions'''
def BuildingInfo():
    print("\n Building info called")
def GenReport():
    print("\n Gen report called")
def CheckEmpInfo():
    print("\n Check emp info called")
def DisplayRentInfo():
    print("\n Display Rent Info called")
def DisplayApartmentInformation():
    print("\n DisplayApartmentInfomation called")


'''Staff Actions'''
def check_sublease():
    print("\n Check sublease called")
def check_service():
    print("\n Check service called")
def display_apartment():
    print("\n Display apartment")



