import sys

def GenReport():
    print("\n ********************************************************************************** \n")
    print(" \n Generate Report")
    print(" \n Please choose one of the following options to continue")
    print("\n ********************************************************************************** \n")
    print("\n 1. No of occupied people ")
    print("\n 2. Frequency of people paying rent ")
    print("\n 3. Lease expiring ")
    print("\n ********************************************************************************** \n")
    choice = input("\n Please enter your option ")
    if choice == '1':
        occupiedPeople()
    elif choice == '2':
        frequencyPeople()
    elif choice == '3':
         leaseExp()
    else:
        print("Invalid option please run the application again")
        sys.exit(1)


def graph1():
    pass
def graph2():
    pass
def graph3():
    pass

def occupiedPeople():
    pass
def frequencyPeople():
    pass
def leaseExp():
    pass

if __name__ == '__main__':
    GenReport()