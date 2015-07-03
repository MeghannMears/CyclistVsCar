'''
Created on 20 Jun 2015

@author: meghann
'''

import csv

drivingStyles=('Urban', 'Extra urban', 'Combined')
fuelTypes=('Petrol', 'Diesel', 'Pasta', 'Potatoes')

fuelEnergyDensity = dict()
fuelEnergyDensity['Petrol'] = 32400 # kJ/L
fuelEnergyDensity['Diesel'] = 35800 # kJ/L
fuelEnergyDensity['Pasta'] = 15533 # kJ/kg = 3710 kcal/kg
fuelEnergyDensity['Potatoes'] = 3224 # kJ/kg = 770 kcal/kg

fuelUnits = dict()
fuelUnits['Petrol'] = 'L'
fuelUnits['Diesel'] = 'L'
fuelUnits['Pasta'] = 'kg'
fuelUnits['Potatoes'] = 'kg'

fuelDefaultCost = dict()
fuelDefaultCost['Petrol'] = 1.17
fuelDefaultCost['Diesel'] = 1.21
fuelDefaultCost['Pasta'] = 1.20
fuelDefaultCost['Potatoes'] = 1.00


# Import and process car data
carImport = csv.reader(open('cardata.csv', 'r'), delimiter=',')

carData = [] # Create empty list for data and append from file
for row in carImport:
    carData.append(row)

carData.pop(0) # Remove title row

# Make dicts
manufacturerModels = dict()
modelVariants = dict()
lookupUrban = dict()
lookupExtraUrban = dict()
lookupCombined = dict()
lookupFuelType = dict()
manufacturers = []
models = []

for i in range(len(carData)):
    # Add model to manufacturer dictionary
    if carData[i][0] in manufacturerModels:
        if carData[i][1] not in manufacturerModels[carData[i][0]]:
            manufacturerModels[carData[i][0]].append(carData[i][1])
    else:
        manufacturerModels[carData[i][0]] = [carData[i][1]]
        manufacturers.append(carData[i][0])
        
    #Add variant to model dictionary
    if carData[i][1] in modelVariants:        
        modelVariants[carData[i][1]].append(carData[i][2])
    else:
        modelVariants[carData[i][1]] = [carData[i][2]]
        models.append(carData[i][1])
    
    t = (carData[i][0], carData[i][1], carData[i][2])
    lookupUrban[t] = carData[i][4]
    lookupExtraUrban[t] = carData[i][5]
    lookupCombined[t] = carData[i][6]
    lookupFuelType[t] = carData[i][3]
            
manufacturers.sort()

    