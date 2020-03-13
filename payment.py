import math;
import time
class Payment:
    def __init__(self,DigiTicket):
        self.paymentId = str(time.time())+'_'+DigiTicket.veh.type+'_'+str(DigiTicket.space.id)
        self.mode = 'Cash' 
        self.time = DigiTicket.time
    
    # calculate the cost with the help of time diff and vehicle charge factor ( which depends on vehicle type)
    def calculateCost(self,DigiTicket):
        timediff=math.ceil((time.time()-self.time)/3600);
        vehicleChargeFactor=DigiTicket.veh.getVehicleChargeFactor(DigiTicket.veh.type);
        return vehicleChargeFactor*timediff;
