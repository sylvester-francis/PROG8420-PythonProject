"""
Code created by Parvathy Suresh
Student ID : 8735728
Created date : 20 April 2022
Last Modified date : 20 April 2022
Last Modified by  : Parvathy Suresh
"""

from menuhelper import *

'''Insert New Building'''
def insert_building():
    query_building = {}
    query_building['buildingName'] = "Elixir"
    query_building['Address'] = "1376 Old Zeller"
    query_building['City'] = "Guelph"
    query_building['postalCode'] = "N2A"
    query_building['province'] = "ON"
    query_building['isFurnished'] = True
    query_building['isParkingAvailable'] = True
    query_building['storageAreaAvailable'] = True
    query_building['petFriendly'] = True
    query_building['ownerId'] = ObjectId('621eee8586ed827ec88459b9')
    building_request = building.create_buildingInfo(query_building)

    query_building = {}
    query_building['buildingName'] = "Clonton Ave."
    query_building['Address'] = "186 Pebble Creek"
    query_building['City'] = "Cambrigde"
    query_building['postalCode'] = "K3S"
    query_building['province'] = "ON"
    query_building['isFurnished'] = True
    query_building['isParkingAvailable'] = False
    query_building['storageAreaAvailable'] = True
    query_building['petFriendly'] = False
    query_building['ownerId'] = ObjectId('624b07c103cae6f735ad7074')
    building_request = apartment.create_apartmentInfo(query_building)

    if building_request != None:
        print("\n New Building added successfully")
    else:
        print("\n Error in adding New Building, please try again")

'''Insert New apartment'''
def insert_apartment():
    query_apartment = {}
    query_apartment['buildingId'] = ObjectId('626029ae3f9a59da65bae3b2')
    query_apartment['unitType'] = "Single Room"
    query_apartment['rentId'] = ObjectId('621f008d86ed827ec8845a6b')
    query_apartment['noOfWashrooms'] = 2
    #query_apartment['userId'] = ObjectId('621eee8586ed827ec88459b5')
    query_apartment['isFurnished'] = True
    query_apartment['isAvailable'] = True
    query_apartment['hasEnsuiteWashroom'] = True
    query_apartment['hasEnsuiteLaundry'] = True
    query_apartment['rentalPrice'] = "$ 1200"
    apartment_request = apartment.create_apartmentInfo(query_apartment)

    query_apartment = {}
    query_apartment['buildingId'] = ObjectId('626029ae3f9a59da65bae3b3')
    query_apartment['unitType'] = "Two Rooms"
    query_apartment['rentId'] = ObjectId('621f008d86ed827ec8845a6d')
    query_apartment['noOfWashrooms'] = 1
    #query_apartment['userId'] = ObjectId('621eee8586ed827ec88459b8')
    query_apartment['isFurnished'] = True
    query_apartment['isAvailable'] = False
    query_apartment['hasEnsuiteWashroom'] = True
    query_apartment['hasEnsuiteLaundry'] = False
    query_apartment['rentalPrice'] = "$ 1100"
    apartment_request = apartment.create_apartmentInfo(query_apartment)

    if apartment_request != None:
        print("\n New Apartment added successfully")
    else:
        print("\n Error in adding New Apartment, please try again")

def menu():
    print("\n ********************************************************************************** \n")
    print("\n 1. Add Building ")
    print("\n 2. Add Apartment ")
    print("\n 3. Exit application")
    print("\n ********************************************************************************** \n")
    choice = input("\n Please enter your option ")
    if choice == '1':
        insert_building()
    elif choice == '2':
        insert_apartment()
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