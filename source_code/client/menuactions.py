"""
Code created by Sylvester Francis
Student ID : 8735728
Created date : 26 March 2022
Last Modified date : 04 April 2022
Last Modified by  : Parvathy Suresh
"""

import backend.User as user
import backend.apartment as apartment
import backend.Building as building
import backend.RentalInfo as rental
import backend.sublet as sublet
import backend.service as service
from bson.objectid import ObjectId
from prettytable import PrettyTable


'''Tenant Actions'''
def viewProfile(data):
    q = {}
    q['username'] = data['username']
    q['password'] = data['password']
    current_User = user.get_one_user(q)
    print("\n ******************************User Details***************************************** \n")
    print("\n First Name : {0} \n Last Name: {1} \n Email: {2} \n User name: {3} \n Phone Number: {4} ".format(current_User['FirstName'],current_User['LastName'],current_User['email'],current_User['username'],current_User['phoneNumber']))
    print("\n ********************************************************************************** \n")
def viewapartment(data):
    q = {}
    q['username'] = data['username']
    q['password'] = data['password']
    current_User = user.get_one_user(q)
    query = {}
    query['buildingId'] = current_User['buildingId']
    current_Apartment = apartment.get_apartment_info(query)
    if current_Apartment!= None:
        print("\n ******************************Apartment Details***************************************** \n")
        print("\n UnitType : {0} \n rentalPrice: {1} \n NoOfWashrooms: {2} \n IsFurnished: {3} \n Has Ensuite Laundry: {4} ".format(current_Apartment['unitType'],current_Apartment['rentalPrice'],current_Apartment['noOfWashrooms'],current_Apartment['isFurnished'],current_Apartment['hasEnsuiteLaundry']))
        print("\n ********************************************************************************** \n")
    else:
        print("\n Apartment Not Found \n")

#TODO : For Parvathy
def raise_service_req(data):
    q = {}
    q['username'] = data['username']
    q['password'] = data['password']
    current_User = user.get_one_user(q)
    query = {}
    query['buildingId'] = current_User['buildingId']
    current_Apartment = apartment.get_apartment_info(query)
    query_service = {}
    query_service['userid'] = current_User['_id']
    query_service['appartmentid'] = current_Apartment['_id']
    query_service['buildingid'] = current_Apartment['buildingId']
    query_service['requiresService'] = True
    service_request = service.createService(query_service)
    if service_request != None:
        print("\n Apartment Service requested successfully")
    else:
        print("\n Error in raising Apartment Service request, please try again")
            
#TODO : For Parvathy
def raise_sublet_req(data):
    print("\n raise sublet req called")
    q = {}
    q['username'] = data['username']
    q['password'] = data['password']
    current_User = user.get_one_user(q)
    query = {}
    query['buildingId'] = current_User['buildingId']
    current_Apartment = apartment.get_apartment_info(query)
    query_sublet = {}
    query_sublet['userid'] = current_User['_id']
    query_sublet['appartmentid'] = current_Apartment['_id']
    query_sublet['buildingid'] = current_Apartment['buildingId']
    query_sublet['RequestedSublet'] = True
    sublet_request = sublet.createSubletInfo(query_sublet)
    if sublet_request != None:
        print("\n Apartment Sublease requested successfully")
    else:
        print("\n Error in raising Apartment Sublease request, please try again")

def pay_rent(data):
    error_entry = True
    while error_entry:
        try:
            amount = input("Enter the rent amount to pay: ")
            amount = int(amount)
        except ValueError:
            continue
        else:
            error_entry = False
            q = {}
            q['userId'] = ObjectId(data['_id'])
            current_Apartment = apartment.get_apartment_info(q)
            if current_Apartment!= None:
                rent_Price = current_Apartment['rentalPrice']
                res = [int(i) for i in rent_Price.split() if i.isdigit()]
                if (amount < res[0] or amount > res[0]):
                    print("Please pay the rent amount ${0}".format(res[0]))
                    error_entry = True
                else:
                    print("Rent amount paid successfully!!")
                    error_entry = False
            else:
                print("\n Invalid Amount \n")

'''Owner Actions'''
def BuildingInfo():
    building_dict = {}
    building_table = PrettyTable()
    buildings = building.get_multiple_buildingInfo()
    for b in buildings:
        building_dict.update({'Building Name':b['buildingName'],'Address':b['Address'],'City':b['City'],'PostalCode':b['postalCode'],'Province':b['province'],'Furnished':b['isFurnished'],'Parking':b['isParkingAvailable'],'Storage':b['storageAreaAvailable'],'PetFriendly':b['petFriendly']})
        building_table.field_names = building_dict.keys()
        building_table.add_row(building_dict.values())
    print(building_table)
    



def GenReport():
    building_data = building.agg_apartments()
    apartment_data = apartment.agg_users()
    rental_data = building.agg_rental_info()
    building_table = PrettyTable()
    apartment_table = PrettyTable()
    rental_table = PrettyTable()
    for d in building_data:
        building_table.field_names = d.keys()
        building_table.add_row(d.values())
    for a in apartment_data:
        apartment_table.field_names = a.keys()
        apartment_table.add_row(a.values())
    for r in rental_data:
        rental_table.field_names = r.keys()
        rental_table.add_row(r.values())
    print(building_table)
    print(apartment_table)
    print(rental_table)


# Display the staff in that Building
def CheckEmpInfo(data):
    q = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query = {}
    query['buildingId'] = current_User['buildingId']
    query['userType'] = "Staff"
    staff_info = user.get_multiple_users(query)
    for index,item in enumerate(staff_info):
        print("\n ******************************Details of Staff - {0} ********************************************* \n".format(index+1))
        print("\n FirstName : {0} \n LastName: {1} \n Email: {2} \n PhoneNumber: {3} \n ".format(item['FirstName'],item['LastName'],item['email'],item['phoneNumber']))
    print("\n ********************************************************************************** \n")

#Displays the details of the user who is paying the rent.
def DisplayRentInfo(data):
    q = {}
    query_building = {}
    query_rental = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query_building['_id'] = current_User['buildingId']
    current_Building = building.get_building_info(query_building)
    query_rental['buildingId'] =  current_User['buildingId']
    current_rental = rental.get_one_rentalInfo(query_rental)
    print("\n ******************************Rental information ********************************************* \n")
    print("\n Building Name : {0} \n Rental Period : {1} \n Rent Paid: {2} \n Advance Paid: {3} \n Deposit Paid: {4} \n Rent due on: {5} \n".format(current_Building['buildingName'],current_rental['rentalPeriod'],current_rental['rentPaid'],current_rental['advancePaid'],current_rental['depositPaid'],current_rental['rentDueOn']))


#TODO : Print statement to be modified - Rachel
#error while running the method.. please see to it
def DisplayApartmentInformation(data):
    print("\n DisplayApartmentInfomation called")
    q = {}
    query_building = {}
    query_apartment = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query_building['_id'] = current_User['buildingId']
    query_apartment['buildingId'] = current_User['buildingId']
    current_Building = building.get_building_info(query_building)
    current_apartment = apartment.get_multiple_apartmentInfo(query_apartment)
    for index,item in enumerate(current_apartment):
        print("\n ******************************Apartment information ********************************************* \n")
        print("\n Building Name : {0} \n Furnished : {1} \n Available : {2} \n Unit Type: {3} \n No. of Washrooms: {4} \n Ensuite Washroom: {5} \n Ensuite Laundry: {6}  \n Rent: {7} \n".format(current_Building['buildingName'],item['isFurnished'],item['isAvailable'],item['unitType'],item['noOfWashrooms'],item['hasEnsuiteWashroom'],item['hasEnsuiteLaundry'],item['rentalPrice']))
    print("\n ********************************************************************************** \n")


    
'''Staff Actions'''

def check_sublease():
    query = {}
    query['RequestedSublet'] = True
    sublet_info = sublet.get_multiple_subletInfos(query)
    for index,item in enumerate(sublet_info):
        q = {}
        q['_id'] = item['buildingid']
        current_Building = building.get_building_info(q)
        query_apartment = {}
        query_apartment['_id'] = item['appartmentid']
        current_apartment = apartment.get_apartment_info(query_apartment)
        query_user = {}
        query_user['_id'] = item['userid']
        current_User = user.get_one_user(query_user)
        print("\n ******************************Details of Sublease Requested User - {0} ********************************************* \n".format(index+1))
        print("\n FirstName : {0} \n LastName: {1} \n Email: {2} \n PhoneNumber: {3}  \n Apartment Unit Type: {4}  \nBuilding Name: {5}  \nBuilding Address: {6}  \nCity: {7}\n ".format(current_User['FirstName'],
        current_User['LastName'],current_User['email'],current_User['phoneNumber'],current_apartment['unitType'],
        current_Building['buildingName'],current_Building['Address'],current_Building['City']))
    print("\n ********************************************************************************** \n")

def check_service():
    print("\n Check service called")
    query = {}
    query['requiresService'] = True
    service_info = service.get_multiple_serviceInfos(query)
    for index,item in enumerate(service_info):
        q = {}
        q['_id'] = item['buildingid']
        current_Building = building.get_building_info(q)
        query_apartment = {}
        query_apartment['_id'] = item['appartmentid']
        current_apartment = apartment.get_apartment_info(query_apartment)
        query_user = {}
        query_user['_id'] = item['userid']
        current_User = user.get_one_user(query_user)
        print("\n ******************************Details of Service Requested User - {0} ********************************************* \n".format(index+1))
        print("\n FirstName : {0} \n LastName: {1} \n Email: {2} \n PhoneNumber: {3}  \n Apartment Unit Type: {4}  \nBuilding Name: {5}  \nBuilding Address: {6}  \nCity: {7}\n ".format(current_User['FirstName'],
        current_User['LastName'],current_User['email'],current_User['phoneNumber'],current_apartment['unitType'],
        current_Building['buildingName'],current_Building['Address'],current_Building['City']))
    print("\n ********************************************************************************** \n")


def display_apartment(data):
    print("\n DisplayApartmentInfomation called")
    q = {}
    query_building = {}
    query_apartment = {}
    q['_id'] = ObjectId(data['_id'])
    current_User = user.get_one_user(q)
    query_building['_id'] = current_User['buildingId']
    query_apartment['buildingId'] = current_User['buildingId']
    current_Building = building.get_building_info(query_building)
    current_apartment = apartment.get_multiple_apartmentInfo(query_apartment)
    for index,item in enumerate(current_apartment):
        print("\n ******************************Apartment information ********************************************* \n")
        print("\n Building Name : {0} \n Furnished : {1} \n Available : {2} \n Unit Type: {3} \n No. of Washrooms: {4} \n Ensuite Washroom: {5} \n Ensuite Laundry: {6}  \n Rent: {7} \n".format(current_Building['buildingName'],item['isFurnished'],item['isAvailable'],item['unitType'],item['noOfWashrooms'],item['hasEnsuiteWashroom'],item['hasEnsuiteLaundry'],item['rentalPrice']))
    print("\n ********************************************************************************** \n")

