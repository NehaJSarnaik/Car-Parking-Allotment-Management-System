import time
import unittest
from park import *
from parkingFloor import ParkingFloor
from payment import Payment
from parking import *


class TestParking(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		print("testing start")
		cls.busSpace =2 
		cls.carSpace =2 
		cls.bikeSpace=3
		cls.parkingLot = ParkingLot('Metro Station Parking','Near Metro Station Parking')
		cls.floor = ParkingFloor('floor',cls.carSpace,cls.busSpace,cls.bikeSpace)
		cls.parkingLot.addLevel(cls.floor)
		cls.gate = Gate(1)
		cls.vehicle = Vehicle(56,'bus')
		cls.ticket = Ticket(cls.vehicle)
		cls.parkingLot.processEntry(cls.ticket,cls.gate)
		cls.payment=Payment(cls.ticket)
		# setupDone=True;

	
	def testParkingLot(cls):
		cls.assertEqual('Metro Station Parking',cls.parkingLot.name)

	def testParkingFloorName(cls):
		floorName=cls.floor.name
		cls.assertEqual('floor',floorName)
		
	def testParkingFloorFreeSpace(cls):
		for e in cls.floor.freeSpace['bus']:
			cls.assertEqual(1,e.id)
			break

	def testParkingFloorTakenSpace(cls):
		for e in cls.floor.takenSpace['bus']:
			cls.assertEqual(0,e)
			break

	def testVehicleClass(cls):
		cls.assertEqual('bus',cls.vehicle.type)
		cls.assertEqual(56,cls.vehicle.id)

	def testVehicleChargeFactor(cls):
		vehChargeFactor=cls.vehicle.getVehicleChargeFactor(cls.vehicle.type)
		cls.assertEqual(300,vehChargeFactor)

	def testPayment(cls):
		time.sleep(1)
		cls.assertEqual(300,cls.payment.calculateCost(cls.ticket))

	def testProcessExit(cls):
		cls.parkingLot.processExit(cls.ticket,1)

	def testTicketClass(cls):
		cls.assertEqual(5402,cls.ticket.id)
		cls.assertEqual('Complete',cls.ticket.status)
	

if __name__ == "__main__":
	unittest.main()

#python -m unittest test_parking