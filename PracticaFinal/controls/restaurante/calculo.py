import numpy as np  
from math import radians, sin, cos, sqrt, atan2
class Distancia:
    def calcular(self, lon1, lat1, lon2, lat2):
        lon1 = np.radians(float(lon1))
        lat1 = np.radians(float(lat1))
        lon2 = np.radians(float(lon2))
        lat2 = np.radians(float(lat2))
        r = 6371
        dlon = np.subtract(lon2, lon1)
        dlat = np.subtract(lat2, lat1)
        a = np.add(np.power(np.sin(np.divide(dlat, 2)), 2),
                   np.multiply(np.cos(lat1),
                               np.multiply(np.cos(lat2),
                                           np.power(np.sin(np.divide(dlon, 2)), 2))
                              )
                  )
        c = np.multiply(2, np.arcsin(np.sqrt(a)))
        return c * r
    
    @staticmethod
    def haversine(lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(float, [lat1, lon1, lat2, lon2])
        R = 6371  # Radio de la Tierra en kilómetros
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c
