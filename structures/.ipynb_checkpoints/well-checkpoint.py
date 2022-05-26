import numpy as np

#checking the correctness of the well
def check_correctness_well(well, field):
    '''
    well: current well
    field: current field
    '''
    for point in field.impossible_points:
        if point == well.start:
            return False
        
    return True


#generating well
def well_generation(size_field, r):
    '''
    size_field: size of the current field
    r: production radius from the end of the well
    '''
    x1 = np.random.randint(0, size_field[0]+1)
    x2 = np.random.randint(0, size_field[0]+1)
    
    y1 = np.random.randint(0, size_field[1]+1)
    y2 = np.random.randint(0, size_field[1]+1)
    
    z2 = np.random.randint(0, size_field[2]+1)
    
    position_start = (x1, y1)
    position_end = (x2, y2, z2)
    
    return Well(position_start, position_end, r)


#population generation for wells
def pop_well_generation(pop_size, field, well_parameters): 
    '''
    pop_size: the size of the population to be generated
    field: current field 
    road_parameters: dictionary of parameters required for setting well
    '''
    size_field = field.size
    
    count_well = well_parameters['count_well']
    r = well_parameters['r']
    
    pop = []
    for _ in range(pop_size): 
        pop_gens = 0 
        wells = []
        
        while pop_gens < count_well:
            well = well_generation(size_field, r)

            if check_correctness_well(well, field):
                wells.append(well)
                pop_gens += 1
        
        pop.append(wells)
            
    return pop
        
    
#The class that defines the well
class Well():
    def __init__(self, position_start, position_end, r):
        '''
        position_start: well start position (on the surface)
        position_end: well end position
        r: production radius from the end of the well

        Class Parameters: 
        start: well start position (on the surface)
        end: well end position
        len_wells_m: well length
        cost:
        well_cells:
        '''
        self.start = position_start
        self.end = position_end
        self.r = r
        
        self.start_end = [self.start[0], self.start[1], self.end[0], self.end[1], self.end[2]]
        
        self.len_wells_m = np.sqrt((20 * (self.start[0] - self.end[0])) ** 2 + (10 * (self.start[1] - self.end[1])) ** 2 + 
                                   (2 * self.end[2]) ** 2) / 3.28
        self.cost = self.len_wells_m * 300
        
        self.well_cells = [(x_i, y_i, z_i) for x_i in range(max(0, int(self.end[0]) - r), min(int(self.end[0]) + r, 20))              
                           for y_i in range(max(0, int(self.end[1]) - r), min(20, int(self.end[1]) + r)) 
                           for z_i in range(max(0,int(self.end[2]) - r), min(20, int(self.end[2]) + r))]