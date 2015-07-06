import lists

def cyclistEnergyUse(parent, cyclistWeight, bikeWeight, velocity):
# Calculate bike kJ/km and km/kJ
# Invoked by cyclist data frame when any field changed
    # Converted from metric input to imperial for use with Irons formula
    cyclistWeight = cyclistWeight.get()
    bikeWeight = bikeWeight.get()
    velocity = velocity.get()
    # Check fields are not empty
    if (cyclistWeight != '' and bikeWeight != '' and velocity != ''):
        # Convert metric input to imperial for Irons formula
        cyclistWeight = float(cyclistWeight) * 2.2046 # kg -> lb
        bikeWeight = float(bikeWeight) * 2.2046 # kg -> lb
        velocity = float(velocity) * 0.6214 # km/hr -> mi/hr
        # Calculate energy use (output units = kcal/hr)
        energyUse = ((0.0053 * velocity * (cyclistWeight + bikeWeight) + 
            0.0083 * velocity**3) * 7.2)
        # Convert imperial to metric
        energyUse = energyUse * 4.1868 # kcal/hr -> kJ/hr
        # Divide through velocity to get kJ/km
        energyUse = energyUse / velocity # kJ/hr -> kJ/km
        parent.comparisons.cyclistEnergyUse.set(round(energyUse))
        parent.comparisons.cyclistDistance.set(round((1/energyUse)*1000, 2))
    else:
        # Otherwise set to blank
        parent.comparisons.cyclistEnergyUse.set('-')
        parent.comparisons.cyclistDistance.set('-')
            
def carEnergyUse(parent, carFuel, carEfficiency):
# Calculate car kJ/km and km/kJ
# Invoked by car data frame when fuel type/efficiency changed
    fuel = carFuel.get()
    efficiency = carEfficiency.get()
    # Check fields are not empty or set to defaults
    if (fuel != '-' and efficiency != '-' and efficiency != ''):
        # Use energy density lookup to calculate
        if (fuel == 'Petrol' or fuel == 'Petrol / E85 (Flex Fuel)' or 
            fuel == 'Petrol Electric' or fuel == 'Petrol Hybrid'):
            energyUse = (lists.fuelEnergyDensity['Petrol'] * 
                         float(efficiency)) / 100  
        elif (fuel == 'Diesel' or fuel == 'Diesel/Electric'):
            energyUse = (lists.fuelEnergyDensity['Diesel'] * 
                         float(efficiency)) / 100               
        parent.comparisons.carEnergyUse.set(round(energyUse))
        parent.comparisons.carDistance.set(round((1/energyUse)*1000, 2))        
    else:
        # Otherwise set to blank
        parent.comparisons.carEnergyUse.set('-')
        parent.comparisons.carDistance.set('-')
            
def comparison(parent, mode, fuelEnergyPerUnit, fuelEnergyTotal, 
                  fuelCost, fuelQuantity, carEnergyUse, cyclistEnergyUse):
# Calculate car £/km, km/£, km/amount fuel  
    fuelQuantity = fuelQuantity.get()
    fuelCost = float(fuelCost.get())
    carEnergyUse = carEnergyUse.get()
    cyclistEnergyUse = cyclistEnergyUse.get()
    # Set car data
    if mode == 'Car' or mode == 'Both':
        if(carEnergyUse != '-' and carEnergyUse != '' and fuelCost != '' and 
           fuelQuantity != ''):
            costPerKm = (fuelCost/float(fuelEnergyPerUnit.get()) * 
                         float(carEnergyUse))
            parent.comparisons.carCost.set(round(costPerKm*100, 2))
            parent.comparisons.carDistCost.set(round(1/costPerKm, 2)) 
            parent.comparisons.carComparisonDist.set(round(
                        float(fuelEnergyTotal.get()) / float(carEnergyUse), 2))
        else:
            parent.comparisons.carCost.set('-')
            parent.comparisons.carDistCost.set('-') 
            parent.comparisons.carComparisonDist.set('-')
    # Set cyclist data    
    if mode == 'Cyclist' or mode == 'Both':
        if (cyclistEnergyUse != '-' and cyclistEnergyUse != '' and 
            fuelCost != '' and fuelQuantity != ''):
            costPerKm = (fuelCost/float(fuelEnergyPerUnit.get()) * 
                         float(cyclistEnergyUse))
            parent.comparisons.cyclistCost.set(round(costPerKm*100, 2))
            parent.comparisons.cyclistDistCost.set(round(1/costPerKm, 2)) 
            parent.comparisons.cyclistComparisonDist.set(round(
                                                float(fuelEnergyTotal.get()) / 
                                                float(cyclistEnergyUse), 2))
        else:
            parent.comparisons.cyclistCost.set('-')
            parent.comparisons.cyclistDistCost.set('-') 
            parent.comparisons.cyclistComparisonDist.set('-')
    