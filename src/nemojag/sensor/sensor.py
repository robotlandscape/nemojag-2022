'''
    This class represents a sensor.
    Any sensor (perhaps not the camera though).
'''
from abc import abstractmethod


class Sensor:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype
    
    def getName(self):
        return self.name
    
    def getDataType(self):
        return self.datatype

    '''
    This method should return a value from the sensor.
    '''
    @abstractmethod
    def pullData(self):
        pass