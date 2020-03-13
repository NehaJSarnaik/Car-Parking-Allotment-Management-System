import time
from payment import Payment
from parkingFloor import ParkingFloor
from park import *

class Vehicle:
    def __init__(self,vehId,vehType):
        self.id = vehId
        self.type = vehType
    
    # method to get the charge factor according to vehicle type 
    # for example for car we charge 200 upto 1 hour
    def getVehicleChargeFactor(self,vehType):
        switcher = {
        'bike': 100,
        'car': 200,
        'bus': 300,
        }
        return switcher.get(vehType, 100)

class ParkingLot:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.level = []

    # there are many level in this parking lot so add a level where we want to start parking
    # for example first floor parking
    def addLevel(self,floor):
        self.level.append(floor)

    # it check if a space is avalaible for a perticular vehicle in current parking floor 
    # if available then it will call to assign the space and return true else return false
    def processEntry(self,ticket,gate):
        for l in self.level:
            if l.assignSpace(ticket):
                return True
        return False

    # do the required things to unallotparking (exit ) of vehicle
    def processExit(self,DigiTicket,gate):

        payment=Payment(DigiTicket)
        # get the calculated payment
        totlalPayment=payment.calculateCost(DigiTicket);
        # do the payment processing
        DigiTicket.processPayment(totlalPayment);
        print(repr(DigiTicket));
        
    

def main():

    # take the number of space available for the given type of vehicle this number should be min 1
    busSpace =int(input ("Enter number of bus space available in your parking  :"))
    carSpace =int(input ("Enter number of car space available for your parking  :"))
    bikeSpace=int(input ("Enter number of bike space available for your parking  :"))  
    
    # create instance of parking lot and assign name and address to it
    parkingLot = ParkingLot('Metro Station Parking','Near Metro Station Parking')
    # create a floor
    newFloor = ParkingFloor('floor',carSpace,busSpace,bikeSpace)
    parkingLot.addLevel(newFloor)

    try:
        totalVehicle=int(input ("Enter number of vehicle to park :"))
    except:
        print(" Please enter correct input ")
        exit()
    gate = Gate(1)
    allTickets={}
    # run a loop to park all the vehicle acording tho the number of vehicle entered.
    for singleVehicle in range(1,totalVehicle+1):
        try:
            print()
            vehicleNo=int(input ("Enter your Vehicle"+str(singleVehicle)+" No "))
        except:
            # exception if input is not correct
            print("only integer are allowed in vehicle No ")
            exit()

        if(vehicleNo):
            vehicleType=str(input ("Enter Type Of Vehicle"+str(singleVehicle)+", currently available vehicle types are bus,car,bike "))
            if not vehicleType in ['bus','car','bike']:
                raise Exception("Sorry, This vehicle type is not allowed")
                exit()

            # create an instace of vehicle by giving vehicle no and vehicle type
            vehicle = Vehicle(vehicleNo,vehicleType)

            # create ticket for this vehicle
            ticket = Ticket(vehicle)
            allTickets[vehicleNo]=ticket;

            # do the entry process for this given vehich and ticket and print the ticket
            if parkingLot.processEntry(ticket,gate):
                gate.printTicket(ticket)
            else:
                gate.display('Space is not available right now ')


    

    print("\n")
    print(len(allTickets), " out of ",totalVehicle, " Vehicles are parked successfully ")
    print("================================================================================")
    time.sleep(3)

    input("click enter to unpark a vehicle ")

    # run the loop for all parked vehicle to unpark them
    while allTickets:
        vehicleNo=int(input ("Enter Your Vehicle No To Unpark "))
        if(vehicleNo):
            if vehicleNo in allTickets:
                print('Exit process start')
                # start the exit process for unparking a vehicle
                parkingLot.processExit(allTickets[vehicleNo],gate)
                gate.display('Payment Successful')
                # remove this vehicle's ticket from remaining allTickets
                allTickets.pop(vehicleNo)
                print("")
                print("Vehicle is unparked successfully")
                print("")
            else:
                print('This vehicle haven\'t parked')

if __name__ == '__main__':
    main()





