import time
class Space:
    def __init__(self,spaceType,spaceId):
        self.id = spaceId
        self.type = spaceType

class Ticket:
    def __init__(self,vehicle):
        self.id = 5346+vehicle.id #self.generateId() 
        self.veh = vehicle

        self.space = None
        self.time = time.time()
        self.status = 'Active'
        self.payment = None

    # using repr to print the totla payment and vehicle type 
    def __repr__(self):
        return 'payment:%d \nVehicle Type:%s ' % (self.payment, self.veh.type)

    # do the process of allocating the space to a vehicle
    def allocateSpace(self,space):
        self.space = space

    # do the processing of the payment and make the status complete
    def processPayment(self,totlalPayment):
        self.status = 'Complete'
        self.payment = totlalPayment


class Gate:
    def __init__(self,id):
        self.id = id

    # print the ticket with required things like ticket id, vehicle id etc
    def printTicket(self,DigiTicket):
        print('Ticket ID=',DigiTicket.id)
        print('Vehicle ID = ',DigiTicket.veh.id)
        print('space ID =',DigiTicket.space.id)
        print('Ticket ID =',DigiTicket.id)
        print('Ticket Time =',time.ctime(DigiTicket.time))

    # to display any message
    def display(self,message):
        print(message)