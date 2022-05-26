import numpy as np
import copy
'''
#The class that defines the simulation
class Simulation():
    def __init__(self, field, T, volume, price_oil):
        
        field: current field 
        T: period of operation
        volume: production volume per unit of time
        price_oil: oil price
        
        Class Parameters:
        field: current field 
        T: period of operation
        v: production volume per unit of time
        price_oil: oil price
        
        self.field = field
        self.T = T
        self.v = volume 
        self.price_oil = price_oil
        
    def one_simulation(self, wells):
        data = self.field.data.copy()
        
        current_ind = [len(well.well_cells) - 1 for well in wells]
        volume_oil = [] #in dollars
        price_operation = [] #in dollars 
        
        for t in range(self.T):
            oil_t = 0
            operation_t = 0

            for i, well in enumerate(wells): 
                current_v = self.v
                while current_v != 0 and data[well.well_cells[0]] != 0:
                    current_v = max(0, current_v - data[well.well_cells[current_ind[i]]])
                    data[well.well_cells[current_ind[i]]] = max(data[well.well_cells[current_ind[i]]] - current_v, 0)
                    if data[well.well_cells[current_ind[i]]] == 0:
                        current_ind[i] -= 1
                oil_t += self.v - current_v
                operation_t += 25 * (self.v - current_v) + 200

            volume_oil.append(oil_t)
            price_operation.append(operation_t)
        
        return np.array(volume_oil) * self.price_oil, np.array(price_operation)
'''
import numpy as np

def simulation(wells: 'list[well]', T: int, data_sim: np.array, v: int = 40, price_oil: float = 70):
    '''
    Simulation of oil production at the field
    
    Parameters: 
    wells: 'list[well]', list of wells in the 'well' class format
    T: int, number of days of field operation
    data_sim: np.array[float], porosity value on the grid
    v: int, volume of oil production and water injection per day (or period) (in barrels). 1 barrel = 0.159 m^3
    '''
    
    current_ind = [len(well.well_cells) - 1 for well in wells]
    volume_oil = [] #in dollars
    price_operation = [] #in dollars 
    
    for t in range(T):
        oil_t = 0
        operation_t = 0
        
        for i, well in enumerate(wells): 
            current_v = 40
            while current_v != 0 and data_sim[well.well_cells[0]] != 0:
                current_v = max(0, current_v - data_sim[well.well_cells[current_ind[i]]])
                data_sim[well.well_cells[current_ind[i]]] = max(data_sim[well.well_cells[current_ind[i]]] - current_v, 0)
                if data_sim[well.well_cells[current_ind[i]]] == 0:
                    current_ind[i] -= 1
            oil_t += 40 - current_v
            operation_t += 25 * (40 - current_v) + 200
            
        volume_oil.append(oil_t)
        price_operation.append(operation_t)
    
    return np.array(volume_oil) * price_oil, np.array(price_operation)    