import math as m
import numpy as np
import pandas as pd

def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
    R = 6371 # Radius of the earth in km
    dLat, dLon = deg2rad(lat2-lat1), deg2rad(lon2-lon1)
    a = m.sin(dLat/2) * m.sin(dLat/2) + m.cos(deg2rad(lat1)) * m.cos(deg2rad(lat2)) * m.sin(dLon/2) * m.sin(dLon/2)
    c = 2 * m.atan2(m.sqrt(a), m.sqrt(1-a))
    d = R * c
    return d

def deg2rad(deg):
    return deg * (m.pi/180)

def loadData(path):
    cargo = pd.read_csv(path+'/cargo.csv', delimiter=',')
    trucks = pd.read_csv(path+'/trucks.csv',delimiter=',')
    return cargo, trucks

def getCostMatrix(cargo, trucks):
    cargo_origins = cargo[:,3:5] 
    trucks_origins = trucks[:,-2:]
    C = np.zeros((trucks.shape[0],cargo.shape[0]))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            C[i,j] = getDistanceFromLatLonInKm(trucks_origins[i,0],trucks_origins[i,1],cargo_origins[j,0],cargo_origins[j,1])
    return C

class task_exception(Exception):
    pass