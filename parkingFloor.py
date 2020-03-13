from park import Space
class ParkingFloor:
    def __init__(self,name,carSpace,busSpace,bikeSpace):
        self.name = name
        self.__totalSpace = {'car':carSpace,'bus':busSpace,'bike':bikeSpace}

        self.__spaceTaken = {'car':0,'bus':0,'bike':0}

        self.freeSpace = {'car':set(),'bus':set(),'bike':set()}
        self.takenSpace = {'car':{},'bus':{},'bike':{}}
        self.__updateFreeSpace('car',carSpace)
        self.__updateFreeSpace('bus',busSpace)
        self.__updateFreeSpace('bike',bikeSpace)

    # assign space to a vehicle 
    def assignSpace(self,DigiTicket):
        # if space space is not available then return fals
        if self.__getTotalSpace(DigiTicket.veh.type) <= self.__getSpaceTaken(DigiTicket.veh.type):
            return False
        # run a loop throug the freeSpace and find the free space for the given type of vehicle 
        # and remove this space from freespace and add this to space taken
        for space in self.freeSpace[DigiTicket.veh.type]:
            if space.id not in self.takenSpace[DigiTicket.veh.type]:
                self.takenSpace[DigiTicket.veh.type][space.id] = DigiTicket
            self.__spaceTaken[DigiTicket.veh.type]+=1
            self.freeSpace[DigiTicket.veh.type].remove(space)
            DigiTicket.allocateSpace(space)
            return True
        return False

    # add freeAvailabe space for a given type 
    def __updateFreeSpace(self,type,space):
        for i in range(space):
            s = Space(type,i)
            self.freeSpace[type].add(s)

    # get total space
    def __getTotalSpace(self,type):
        return self.__totalSpace[type]

    # get already taken space
    def __getSpaceTaken(self,type):
        return self.__spaceTaken[type]