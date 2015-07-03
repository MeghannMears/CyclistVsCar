'''
Created on 25 Jun 2015

@author: meghann
'''
import tkinter as tk
import tkinter.font
from tkinter import ttk
import lists
import energycalc


class Options(ttk.Labelframe):
    
    def __init__(self, parent):        
        ttk.LabelFrame.__init__(self, parent, text="Fuel comparison options")
        self.parent = parent
        self.fuelType = tk.StringVar()
        self.fuelQuantity = tk.StringVar()
        self.fuelQuantityUnit = tk.StringVar()
        self.fuelEnergyPerUnit = tk.StringVar()
        self.fuelEnergyPerUnitUnit = tk.StringVar()
        self.fuelEnergyTotal = tk.StringVar()
        self.fuelEnergyTotalUnit = tk.StringVar()
        self.fuelCost = tk.StringVar()
        self.fuelCostUnit = tk.StringVar()
        self.fuelTotalCost = tk.StringVar()
        self.multiplierText = tk.StringVar()
        self.initialise()
        
    def switchFuel(self):
    # Invoked when fuel type is changed
        fuel = self.fuelType.get()
        # Look up unit and energy density for fuel type and 
        # set labels accordingly
        fuelUnit = lists.fuelUnits[fuel]
        self.fuelQuantityUnit.set(fuelUnit)
        self.fuelEnergyPerUnitUnit.set('kJ/' + fuelUnit)
        self.fuelCostUnit.set('£/' + fuelUnit)
        self.fuelCost.set(lists.fuelDefaultCost[fuel])
        self.fuelEnergyPerUnit.set(lists.fuelEnergyDensity[fuel]) 
        # Call method to update calculations
        self.calcTotals()

    def calcTotals(self):
    #Invoked when fuel type, quantity or cost is changed
        # Check fields are not empty to prevent errors
        if self.fuelQuantity.get() != '' and self.fuelCost.get() != '':
            # Calculate total energy content and cost of fuel,
            # and update label text
            fuel = self.fuelType.get()
            fuelQuantity = self.fuelQuantity.get() 
            self.multiplierText.set('* ' + str(fuelQuantity) + 
                                lists.fuelUnits[fuel] + ' =')                                             
            self.fuelEnergyTotal.set(round(float(fuelQuantity) * 
                                           lists.fuelEnergyDensity[fuel]))
            self.fuelTotalCost.set(round(float(fuelQuantity) * 
                                    float(self.fuelCost.get()), 2))
        self.updateLabels()
    
    def updateLabels(self):
    # Invoked when fuel type, quantity or cost is changed
    # Invoked by calcTotals method
        fuelType = self.fuelType.get()
        fuelQuantity = self.fuelQuantity.get()
        if fuelQuantity != '' and fuelType != '':
            self.parent.comparisons.costPerKmLabel.set(
                                        'Cost to travel 1km on ' + fuelType +
                                        ' (pence/km)')
            self.parent.comparisons.kmPerPoundLabel.set(
                                            'km travelled per £1 ' + fuelType
                                            + ' km/£')
            self.parent.comparisons.totalKmLabel.set('km travelled on ' + 
                                                fuelQuantity + 
                                                self.fuelQuantityUnit.get()
                                                + ' ' + fuelType)
        else:
            self.parent.comparisons.costPerKmLabel.set(
                                'Cost to travel 1km on selected fuel (£/km)')
            self.parent.comparisons.kmPerPoundLabel.set(
                                'km travelled per £1 selected fuel (km/£)')
            self.parent.comparisons.totalKmLabel.set(
                                    'km travelled on selected fuel/quantity')
        
                
    def initialise(self):          
        # Create and pack widgets
        # First row   
        ttk.Label(self, text="Comparison fuel:").grid(column=0, row=0, 
                                                      sticky=(tk.W), padx=5)
        ttk.Combobox(self, textvariable=self.fuelType, values=lists.fuelTypes, 
                     state="readonly", width=8).grid(column=1, row=0, 
                                                     columnspan=2, 
                                                     sticky=(tk.W))        
        ttk.Label(self, text="Fuel quantity:").grid(column=3, row=0, 
                                                    sticky=(tk.W))
        ttk.Entry(self, textvariable=self.fuelQuantity,
                  width=7).grid(column=4, row=0, sticky=(tk.W))
        ttk.Label(self, textvariable=self.fuelQuantityUnit, 
                  width=3).grid(column=5, row=0, sticky=(tk.W))
        # Second row
        ttk.Label(self, text="Fuel energy content:").grid(column=0, row=1, 
                                                          sticky=(tk.W), 
                                                          padx=5)
        ttk.Label(self, textvariable=self.fuelEnergyPerUnit, 
                  width=5).grid(column=1, row=1, sticky=(tk.W))
        ttk.Label(self, textvariable=self.fuelEnergyPerUnitUnit,
                  width=4).grid(column=2, row=1, sticky=(tk.W))
        ttk.Label(self, textvariable=self.multiplierText).grid(column=3, 
                                                               row=1, 
                                                               sticky=(tk.W))
        ttk.Label(self, textvariable=self.fuelEnergyTotal, 
                  width=7).grid(column=4, row=1, sticky=(tk.W))
        ttk.Label(self, text='kJ', width=3).grid(column=5, row=1, 
                                                 sticky=(tk.W))
        # Third row
        ttk.Label(self, text="Fuel cost:").grid(column=0, row=2, 
                                                sticky=(tk.W), padx=5)
        ttk.Entry(self, textvariable=self.fuelCost, 
                  width=5).grid(column=1, row=2, sticky=(tk.W))
        ttk.Label(self, textvariable=self.fuelCostUnit, 
                  width=4).grid(column=2, row=2, sticky=(tk.W))
        ttk.Label(self, textvariable=self.multiplierText).grid(column=3, 
                                                               row=2, 
                                                               sticky=(tk.W))
        ttk.Label(self, textvariable=self.fuelTotalCost, 
                  width=7).grid(column=4, row=2, sticky=(tk.W))
        ttk.Label(self, text='£', width=3).grid(column=5, row=2, 
                                                sticky=(tk.W))
        # Column & row config
        self.columnconfigure(0, weight=3, pad=5)
        self.columnconfigure(1, weight=2, pad=2)
        self.columnconfigure(2, weight=1, pad=25)
        self.columnconfigure(3, weight=3, pad=5)
        self.columnconfigure(4, weight=2, pad=2)
        self.columnconfigure(5, weight=1, pad=5)
        self.rowconfigure(0, weight=1, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, weight=1, pad=5)
        
    def initialiseContents(self):
    # Set tracers and initialise values
        # Change default values and units when fuel type is changed
        self.fuelType.trace('w', lambda name, index, mode: 
                            self.switchFuel())
        # Calculate total energy and costs when fuel quantity
        # or cost is changed
        self.fuelQuantity.trace('w', lambda name, index, mode: 
                            self.calcTotals())
        self.fuelCost.trace('w', lambda name, index, mode: 
                            self.calcTotals())
        # Update fuel comparison calculations when fuel, quantity or
        # cost changed
        self.fuelEnergyPerUnit.trace('w', lambda name, index, mode:
                            energycalc.comparison(self.parent, 'Both',
                                    self.parent.options.fuelEnergyPerUnit, 
                                    self.parent.options.fuelEnergyTotal, 
                                    self.parent.options.fuelCost, 
                                    self.parent.options.fuelQuantity, 
                                    self.parent.comparisons.carEnergyUse,
                                    self.parent.comparisons.cyclistEnergyUse))
        self.fuelEnergyTotal.trace('w', lambda name, index, mode:
                            energycalc.comparison(self.parent, 'Both',
                                    self.parent.options.fuelEnergyPerUnit, 
                                    self.parent.options.fuelEnergyTotal, 
                                    self.parent.options.fuelCost, 
                                    self.parent.options.fuelQuantity, 
                                    self.parent.comparisons.carEnergyUse,
                                    self.parent.comparisons.cyclistEnergyUse))
        self.fuelTotalCost.trace('w', lambda name, index, mode:
                            energycalc.comparison(self.parent, 'Both',
                                    self.parent.options.fuelEnergyPerUnit, 
                                    self.parent.options.fuelEnergyTotal, 
                                    self.parent.options.fuelCost, 
                                    self.parent.options.fuelQuantity, 
                                    self.parent.comparisons.carEnergyUse,
                                    self.parent.comparisons.cyclistEnergyUse))
        # Set initial values (invoke tracer methods)
        self.fuelType.set('Petrol')
        self.fuelQuantity.set('1')        

            
class CyclistData(ttk.Labelframe):
    
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text="Cyclist data")
        self.parent = parent
        self.cyclistWeight = tk.StringVar()
        self.bikeWeight = tk.StringVar()
        self.velocity = tk.StringVar()
        self.initialise()
           
    def initialise(self):
        # Create and pack widgets
        # First row
        ttk.Label(self, text="Cyclist weight:").grid(column=0, row=0, 
                                                     sticky=(tk.W), padx=5)
        ttk.Entry(self, textvariable=self.cyclistWeight, 
                  width=5).grid(column=1, row=0)
        ttk.Label(self, text="kg").grid(column=2, row=0, sticky=(tk.W))
        # Second row
        ttk.Label(self, text="Bike weight:").grid(column=0, row=1, 
                                                  sticky=(tk.W), padx=5)
        ttk.Entry(self, textvariable=self.bikeWeight, 
                  width=5).grid(column=1, row=1)
        ttk.Label(self, text="kg").grid(column=2, row=1, sticky=(tk.W))
        # Third row
        ttk.Label(self, text="Velocity:").grid(column=0, row=2, sticky=(tk.W),
                                               padx=5)
        ttk.Entry(self, textvariable=self.velocity, 
                  width=5).grid(column=1, row=2)
        ttk.Label(self, text="km/hr").grid(column=2, row=2, sticky=(tk.W))
        # Column & row config
        self.columnconfigure(0, weight=2, pad=5)
        self.columnconfigure(1, weight=1, pad=2)
        self.columnconfigure(2, weight=1, pad=5)
        self.rowconfigure(0, weight=1, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, weight=1, pad=5)
        
    def initialiseContents(self):
    # Set tracers
        # Update energy efficiency data in comparisons frame when
        # weights or velocity change
        self.cyclistWeight.trace('w', lambda name, index, mode: 
                            energycalc.cyclistEnergyUse(self.parent, 
                                                        self.cyclistWeight,
                                                        self.bikeWeight,
                                                        self.velocity))       
        self.bikeWeight.trace('w', lambda name, index, mode: 
                            energycalc.cyclistEnergyUse(self.parent, 
                                                        self.cyclistWeight,
                                                        self.bikeWeight,
                                                        self.velocity))
        self.velocity.trace('w', lambda name, index, mode: 
                            energycalc.cyclistEnergyUse(self.parent, 
                                                        self.cyclistWeight,
                                                        self.bikeWeight,
                                                        self.velocity))
        self.cyclistWeight.set('')
              
class CarData(ttk.Frame):
    
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text="Car data")
        self.parent = parent
        self.useCarLookup = tk.StringVar()
        self.carManuf = tk.StringVar()
        self.carModel = tk.StringVar()
        self.carVariant = tk.StringVar()
        self.carFuel = tk.StringVar()
        self.drivingStyle = tk.StringVar()
        self.carEfficiency = tk.StringVar()
        self.initialise()
 
    def switchCarLookup(self):
    # Turn car lookup options on (use lookup) or off (enter  fuel
    # type and efficiency manually).
    # Invoked by radio buttons.
        if self.useCarLookup.get() == 'True':
            self.carManufSelect['state'] = 'readonly'
            self.carModelSelect['state'] = 'readonly'
            self.carVariantSelect['state'] = 'readonly' 
            self.drivingStyleCombo['state'] = 'readonly'  
            self.carManufLabel['state'] = 'enabled'
            self.carModelLabel['state'] = 'enabled'
            self.carVariantLabel['state'] = 'enabled' 
            self.drivingStyleLabel['state'] = 'enabled'    
            self.carEfficiencyEntry.grid_remove()
            self.carEfficiencyLabel.grid(column=0, row=0)
            self.carFuelCombo.grid_remove()
            self.carFuelLookupLabel.grid(column=1, row=3, sticky=(tk.W))
            self.carEfficiency.set('-')
            self.carFuel.set('-')
        else:
            self.carManufSelect['state'] = 'disabled'
            self.carModelSelect['state'] = 'disabled'
            self.carVariantSelect['state'] = 'disabled'
            self.drivingStyleCombo['state'] = 'disabled'
            self.carManufLabel['state'] = 'disabled'
            self.carModelLabel['state'] = 'disabled'
            self.carVariantLabel['state'] = 'disabled'
            self.drivingStyleLabel['state'] = 'disabled' 
            self.carManuf.set('')
            self.carModel.set('')
            self.carVariant.set('')
            self.drivingStyle.set('')
            self.carEfficiencyLabel.grid_remove()
            self.carEfficiencyEntry.grid(column=0, row=0)
            self.carFuelLookupLabel.grid_remove()
            self.carFuelCombo.grid(column=1, row=3, sticky=(tk.W))
            
    def switchModels(self):
    # Fill models combobox with relevant items when manufacturer 
    # is selected or changed. Also empties variants combobox and 
    # resets selections and lookups.
    # Invoked by manufacturer combobox.
        if self.carManuf.get() != '':
            self.carModelSelect['values'] = \
                lists.manufacturerModels[self.carManuf.get()]
            self.carVariantSelect['values'] = ''
            self.carModel.set('')
            self.carVariant.set('')
            self.carFuel.set('-')
            self.carEfficiency.set('-')
        
    def switchVariants(self):
    # Fill variants combobox with relevant items when model is selected
    # or changed. Also resets selection and lookups.
    # Invoked by model combobox.
        if (self.carModel.get() != '' and 
            self.carModel.get() != 'Select a manufacturer'):
            self.carVariantSelect['values'] = \
                lists.modelVariants[self.carModel.get()]
            self.carVariant.set('')
            self.carFuel.set('-')
            self.carEfficiency.set('-')
 
    def fuelLookup(self):
    # Look up fuel efficiency once driving style and car variant 
    # are set. Also looks up fuel type from variant.
    # Invoked by variant combobox and driving style combobox.
        if (self.carVariant.get() != '' and 
            self.carVariant.get() != 'Select a model'):
            self.carFuel.set(lists.lookupFuelType[(self.carManuf.get(), 
                                                   self.carModel.get(), 
                                                   self.carVariant.get())])
            if self.drivingStyle.get() == 'Urban':
                self.carEfficiency.set(lists.lookupUrban 
                                       [(self.carManuf.get(), 
                                         self.carModel.get(), 
                                         self.carVariant.get())])
            elif self.drivingStyle.get() == 'Extra urban':
                self.carEfficiency.set(lists.lookupExtraUrban 
                                       [(self.carManuf.get(), 
                                         self.carModel.get(), 
                                         self.carVariant.get())])
            elif self.drivingStyle.get() == 'Combined':
                self.carEfficiency.set(lists.lookupCombined 
                                       [(self.carManuf.get(), 
                                         self.carModel.get(), 
                                         self.carVariant.get())])
        
    def initialise(self):
        # Create and pack widgets
        # First row
        self.useLookupButton = ttk.Radiobutton(self, 
                                               text="Use fuel data lookup", 
                                               variable=self.useCarLookup, 
                                               value='True')
        self.useLookupButton.grid(column=0, row=0, columnspan=2, padx=5)          
        ttk.Radiobutton(self, text="Enter fuel data manually", 
                        variable=self.useCarLookup, 
                        value='False').grid(column=2, row=0, columnspan=2)
        # Second row
        self.carManufLabel = ttk.Label(self, text="Manufacturer:")
        self.carManufLabel.grid(column=0, row=1, sticky=(tk.W), padx=5)
        self.carManufSelect = ttk.Combobox(self, textvariable=self.carManuf, 
                                           values=lists.manufacturers, 
                                           state='readonly', width=20)
        self.carManufSelect.grid(column=1, row=1, sticky=(tk.W))
        self.carModelLabel = ttk.Label(self, text="Model:")
        self.carModelLabel.grid(column=2, row=1, sticky=(tk.W))
        self.carModelSelect = ttk.Combobox(self, textvariable=self.carModel, 
                                           values=['Select a manufacturer'], 
                                           state='readonly', width=24)
        self.carModelSelect.grid(column=3, row=1, sticky=(tk.W))
        # Third row
        self.carVariantLabel = ttk.Label(self, text="Description:")
        self.carVariantLabel.grid(column=0, row=2, sticky=(tk.W), padx=5)
        self.carVariantSelect = ttk.Combobox(self, 
                                             textvariable=self.carVariant, 
                                             values=['Select a model'], 
                                             state='readonly', width=60)
        self.carVariantSelect.grid(column=1, row=2, columnspan=3, 
                                   sticky=(tk.W))
        # Fourth row
        self.carFuelLabel = ttk.Label(self, text="Fuel type:")
        self.carFuelLabel.grid(column=0, row=3, sticky=(tk.W), padx=5)
        self.carFuelLookupLabel = ttk.Label(self, textvariable=self.carFuel)
        self.carFuelLookupLabel.grid(column=1, row=3, sticky=(tk.W))
        self.carFuelCombo = ttk.Combobox(self, textvariable=self.carFuel, 
                                         values=['Petrol', 'Diesel'], 
                                         state='readonly', width=10)
        self.drivingStyleLabel = ttk.Label(self, text="Driving style:")
        self.drivingStyleLabel.grid(column=2, row=3, sticky=(tk.W))
        self.drivingStyleCombo = ttk.Combobox(self, 
                                              textvariable=self.drivingStyle, 
                                              values=lists.drivingStyles, 
                                              state='readonly', width=12)
        self.drivingStyleCombo.grid(column=3, row=3, sticky=(tk.W))
        # Fifth row
        ttk.Label(self, text="Fuel efficiency:").grid(column=0, row=4, 
                                                      sticky=(tk.W), padx=5)
        self.carEfficiencyFrame = ttk.Frame(self)
        self.carEfficiencyFrame.grid(column=1, row=4, sticky=(tk.W))
        self.carEfficiencyLabel = ttk.Label(self.carEfficiencyFrame, 
                                            textvariable=self.carEfficiency, 
                                            width=5)
        self.carEfficiencyLabel.grid(column=1, row=0, sticky=(tk.W))
        self.carEfficiencyEntry = ttk.Entry(self.carEfficiencyFrame, 
                                            textvariable=self.carEfficiency, 
                                            width=5)
        ttk.Label(self.carEfficiencyFrame, text="L/100km").grid(column=2, 
                                                                row=0, 
                                                                sticky=(tk.W))
        # Column & row config    
        self.columnconfigure(0, weight=2, pad=5)
        self.columnconfigure(1, weight=3, pad=25)
        self.columnconfigure(2, weight=2, pad=5)
        self.columnconfigure(3, weight=3, pad=5)
        self.rowconfigure(0, weight=1, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, weight=1, pad=5) 
        self.rowconfigure(3, weight=1, pad=5)
        self.rowconfigure(4, weight=1, pad=5)              
        
    def initialiseContents(self):
    # Set tracers and initialise values
        # Turn fields on/off when switching between lookup and manual entry
        self.useCarLookup.trace('w', lambda name, index, mode: 
                                self.switchCarLookup())
        # Set default option for using fuel data lookup
        self.useLookupButton.invoke() 
        # Change models list when manufacturer changed/reset other fields
        self.carManuf.trace('w', lambda name, index, mode: 
                            self.switchModels())
        # Change variants list when model changed/reset other fields
        self.carModel.trace('w', lambda name, index, mode: 
                            self.switchVariants())
        # Look up fuel type and efficiency when variant/driving style set
        self.carVariant.trace('w', lambda name, index, mode: 
                              self.fuelLookup())
        self.drivingStyle.trace('w', lambda name, index, mode: 
                                self.fuelLookup())
        # Update calculations in comparisons frame when fuel type or
        # efficiency changed
        self.carEfficiency.trace('w', lambda name, index, mode: 
                                 energycalc.carEnergyUse(self.parent, 
                                                         self.carFuel, 
                                                         self.carEfficiency))
        self.carFuel.trace('w', lambda name, index, mode: 
                           energycalc.carEnergyUse(self.parent, 
                                                   self.carFuel, 
                                                   self.carEfficiency))
        self.carEfficiency.set('-')       
                        
                
class Comparisons(ttk.Frame):
    
    def __init__(self, parent):
        ttk.LabelFrame.__init__(self, parent, text="Energy use comparison")
        self.parent = parent
        self.cyclistEnergyUse = tk.StringVar()
        self.carEnergyUse = tk.StringVar()
        self.cyclistDistance = tk.StringVar()
        self.carDistance = tk.StringVar()
        self.cyclistCost = tk.StringVar()
        self.carCost = tk.StringVar()
        self.cyclistDistCost = tk.StringVar()
        self.carDistCost = tk.StringVar()
        self.cyclistComparisonDist = tk.StringVar()
        self.carComparisonDist = tk.StringVar()
        self.costPerKmLabel = tk.StringVar()
        self.kmPerPoundLabel = tk.StringVar()
        self.totalKmLabel = tk.StringVar()
        self.initialise()    
    
    def initialise(self):
        # Define font for italic labels 
        italics = tkinter.font.Font(font=str(tkinter.font.Font(
                                        font='TkDefaultFont').configure()))
        italics['slant'] = 'italic'
        italics['size'] = -12
        # Create and pack widgets
        # First row
        ttk.Label(self, text="Cyclist").grid(column=1, row=0)
        ttk.Label(self, text=" Car ").grid(column=2, row=0)
        # Second row
        italicLabel1 = ttk.Label(self, 
                                 text="Calculated from cyclist and car data:")            
        italicLabel1['font'] = italics
        italicLabel1.grid(column=0, row=1, sticky=(tk.W), padx=5)    
        # Third row
        ttk.Label(self, text="Fuel kJ used per km travelled (kJ/km)").grid(
                                            column=0, row=2, sticky=(tk.E))
        ttk.Label(self, textvariable=self.cyclistEnergyUse).grid(column=1, 
                                                                 row=2)
        ttk.Label(self, textvariable=self.carEnergyUse).grid(column=2, row=2)
        # Fourth row
        ttk.Label(self, text="Meters travelled per kJ fuel (m/kJ)").grid(
                                            column=0, row=3, sticky=(tk.E))
        ttk.Label(self, textvariable=self.cyclistDistance).grid(column=1, 
                                                                row=3)
        ttk.Label(self, textvariable=self.carDistance).grid(column=2, row=3)
        # Fifth row
        italicLabel2 = ttk.Label(self, 
                            text="Calculated from selected fuel comparison options:")            
        italicLabel2['font'] = italics
        italicLabel2.grid(column=0, row=4, sticky=(tk.W), padx=5)    
        # Sixth row
        ttk.Label(self, textvariable=self.costPerKmLabel).grid(column=0, 
                                                               row=5, 
                                                               sticky=(tk.E))
        ttk.Label(self, textvariable=self.cyclistCost).grid(column=1, row=5)
        ttk.Label(self, textvariable=self.carCost).grid(column=2, row=5)
        # Seventh row
        ttk.Label(self, textvariable=self.kmPerPoundLabel).grid(column=0, 
                                                               row=6, 
                                                               sticky=(tk.E))
        ttk.Label(self, textvariable=self.cyclistDistCost).grid(column=1, 
                                                                row=6)
        ttk.Label(self, textvariable=self.carDistCost).grid(column=2, row=6)
        # Eighth row     
        ttk.Label(self, textvariable=self.totalKmLabel).grid(column=0, row=7, 
                                                             sticky=(tk.E))
        ttk.Label(self, textvariable=self.cyclistComparisonDist).grid(
                                                            column=1, row=7)
        ttk.Label(self, textvariable=self.carComparisonDist).grid(column=2, 
                                                                  row=7)
        # Info button
        ttk.Button(self, text="Read info", 
                   command=self.parent.showInfo).grid(column=3, row=0, 
                                                      rowspan=8)
        # Column & row config    
        self.columnconfigure(0, weight=5, pad=10)
        self.columnconfigure(1, weight=1, pad=10, minsize=70)
        self.columnconfigure(2, weight=1, pad=10, minsize=70)
        self.columnconfigure(3, weight=1, pad=50)
        self.rowconfigure(0, weight=1, pad=5)
        self.rowconfigure(1, weight=1, pad=5)
        self.rowconfigure(2, weight=1, pad=5) 
        self.rowconfigure(3, weight=1, pad=10)
        self.rowconfigure(4, weight=1, pad=5)
        self.rowconfigure(5, weight=1, pad=5) 
        self.rowconfigure(6, weight=1, pad=5)
        self.rowconfigure(7, weight=1, pad=5)
     
    def initialiseContents(self):   
        # Update fuel comparison calculations when efficiency changes
        self.carEnergyUse.trace('w', lambda name, index, mode:
                                 energycalc.comparison(self.parent, 'Car',
                                        self.parent.options.fuelEnergyPerUnit, 
                                        self.parent.options.fuelEnergyTotal, 
                                        self.parent.options.fuelCost, 
                                        self.parent.options.fuelQuantity, 
                                        self.carEnergyUse, 
                                        self.cyclistEnergyUse))
        
        self.cyclistEnergyUse.trace('w', lambda name, index, mode:
                                 energycalc.comparison(self.parent, 'Cyclist',
                                        self.parent.options.fuelEnergyPerUnit, 
                                        self.parent.options.fuelEnergyTotal, 
                                        self.parent.options.fuelCost, 
                                        self.parent.options.fuelQuantity, 
                                        self.carEnergyUse, 
                                        self.cyclistEnergyUse))
        

class InfoWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.blurb = ("CyclistVsCar v0.1 (03/07/2015)\n"
            "Written by Meghann Mears\n"
            "\n"
            "This app estimates and compares the energy efficiency of a\n"
            "human cyclist and a car. It also compares how much it would\n"
            "cost to run a cyclist on car fuel and vice versa. There are\n"
            "a lot of assumptions made in the calculations: it's just for\n"
            "fun, so please don't take the figures too seriously!\n"
            "\n"
            "Cyclist energy efficiency is calculated using the formula \n"
            "given by Kerry Irons and makes assumptions about bike type,\n"
            "road surface, riding position, gradient, weather conditions\n"
            "and many other factors. Internet forums seem to suggest that\n"
            "this formula give reasonable results, however.\n"
            "\n"
            "Car fuel efficiencies are from the (current) latest version\n"
            "of data provided by the UK Government, and only includes cars\n"
            "for sale as of August 2014. For older cars you will need to\n"
            "look up and enter efficiency data manually. It's generally\n"
            "accepted that the figures obtained in official testing give\n"
            "much better efficiency than is seen in normal car use.\n"
            "\n"
            "I haven't (yet) put validation on the text entry boxes. If you\n"
            "try to put something other than a positive number in, it won't\n"
            "work and you won't get an error message (except in console).\n"
            "\n"
            "Links:\n"
            "\n"
            "Car efficiency data & explanation of methods:\n"
            "http://carfueldata.direct.gov.uk/downloads/default.aspx\n"
            "http://www.dft.gov.uk/vca/fcb/faqs-fuel-consumptio.asp\n"
            "\n"
            "Kerry Irons formula & discussion:\n"
            "http://forums.roadbikereview.com/racing-training-nutrition-\n"
            "triathlons/calories-burned-per-mile-formula-question-28863."
                "html\n"
            "\n"
            "Project on GitHub:\n"
            "https://github.com/MeghannMears/CyclistVsCar") 
        self.initialise()
        
    def initialise(self):
        ttk.Label(self, text=self.blurb).grid(row=0, column=0)
        ttk.Button(self, text="Close info", 
                   command=self.destroy).grid(row=1, column=0)
        self.columnconfigure(0, pad=10)
        self.rowconfigure(0, pad=10)
        self.rowconfigure(1, pad=10)

class MainApplication(ttk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent            
        self.initialise()
            
    def showInfo(self):
    # Opens information window when button is pressed
        InfoWindow(self)
        
    def initialise(self):
        # Initialise
        self.options = Options(self)                
        self.cyclistData = CyclistData(self)
        self.carData = CarData(self)
        self.comparisons = Comparisons(self)
        # Pack
        self.options.grid(column=1, row=1)        
        self.cyclistData.grid(column=0, row=1)
        self.carData.grid(column=0, row=0, columnspan=2)
        self.comparisons.grid(column=0, row=2, columnspan=2)
        # Column & row config
        self.columnconfigure(0, weight=1, pad=10)
        self.columnconfigure(1, weight=3, pad=10)
        self.rowconfigure(0, weight=2, pad=10)
        self.rowconfigure(1, weight=1, pad=10)
        self.rowconfigure(2, weight=3, pad=10)
        # Run method to set tracers & initialise cvalues
        self.initialiseContents()
        
    def initialiseContents(self):
    # Sets tracers and initialises values.
    # Separated from initialise methods due to referencing objects
    # that haven't yet been created.
        self.options.initialiseContents()
        self.carData.initialiseContents()
        self.cyclistData.initialiseContents()
        self.comparisons.initialiseContents()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('CyclistVsCar')
    MainApplication(root).grid(row=0, column=0)
    root.mainloop()

