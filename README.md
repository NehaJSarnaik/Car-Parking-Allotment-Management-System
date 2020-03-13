# Car-Parking-Allotment-Management-System
Parking allotment management, with the help of python’s core classes and features. In this a parking allotment will be designed with the help of taking some user inputs like parking lot name and address and then add floor to this parking Lot and then add a level to it.
When someone wants to park a vehicle it ask for how many vehicles user want to park. According to entered vehicle it ask for the type of the vehicle and the vehicle number and generate a ticket for parking and park it. It repeats the process for all the vehicles user wants to park and if space is not available then it will not park that vehicle.
After parking vehicles if user wants to unpark a vehicle then it ask for the enter the vehicle number to unpark . And upon entering a vehicle number it checks if a vehicle is present with this vehicle number in the parking then it will start the un parking process otherwise it will return a message saying this vehicle is not parked. 

Un parking process contains two tasks

●	Process the payment

○	In this process it will calculate the fare price with the help of calculate factor which depends on the vehicle type and multiply this calculated factor the hourly time difference from the vehicle parking and the current time
○	And finally it will generate the receipt with the fare price and mark the payment successful.
 

●	Free the space 

○	In this subtask it removes that space from space taken and add that space in the free space where other vehicle can be parked
