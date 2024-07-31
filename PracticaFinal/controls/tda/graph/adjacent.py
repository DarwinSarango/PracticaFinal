from math import nan    
class Adjacent():
    def __init__(self):
        self.__weight = nan
        self.__destination = nan

    @property
    def _weight(self):
        return self.__weight
 
    @_weight.setter
    def _weight(self, value):
        self.__weight = value

    @property
    def _destination(self):
        return self.__destination

    @_destination.setter
    def _destination(self, value):
        self.__destination = value
        
    def __str__(self) -> str:
        return "Destination: " + str(self.__destination) + " Weight: " + str(self.__weight)


    
