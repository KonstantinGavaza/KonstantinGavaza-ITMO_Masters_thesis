import numpy as np

#checking the correctness of the road
def check_correctness_road(road, field):   
    '''
    road: current road
    field: current field
    '''
    for point in field.impossible_points:
        if point in road.road_cells:
            return False
        
    return True
            

#generating bend points for roads
def road_generation(count_points, field, start, end):
    '''
    count_points: number of bend points near the road
    field: current field
    '''
    points = [start]
    
    for _ in range(count_points):
        points.append(tuple(np.random.randint([field.size[0], field.size[1]])))
        
    points.append(end)
    
    return Road(sorted(points))


#population generation for roads
def pop_road_generation(pop_size, field, road_parameters):
    '''
    pop_size: the size of the population to be generated
    field: current field 
    road_parameters: dictionary of parameters required for setting road
    '''
    num_gens = 0
    pop = []
    
    while num_gens < pop_size:
        count_points = np.random.randint(road_parameters['count_points'][0], road_parameters['count_points'][1] + 1)
        road = road_generation(count_points, field, road_parameters['starting_point'], road_parameters['ending_point'])
        
        if check_correctness_road(road, field):
            pop.append(road)
            num_gens += 1
    
    return pop


#The class that defines the road
class Road():
    def __init__(self, coord_points):
        '''
        coord_points: coordinates of points of bends of roads
        
        Class Parameters:
        coord: coordinates of points of bends of roads 
        count_bend: number of road bends
        road_cells: coordinates of all road cells
        '''
        self.coord = coord_points
        
        self.count_bend = len(coord_points)
        self.road_cells = self.cells_road()
        
    #finding all the cells of the road
    def cells_road(self):
        
        road_cells = []
        
        for i in range(self.count_bend - 1):
            '''
            road_cells += [(int(self.coord[i][0] + y * (self.coord[i + 1][0] - self.coord[i][0]) / self.coord[i + 1][1]),  y) for y in
                            range(self.coord[i][1], self.coord[i + 1][1])]
            '''
            road_cells += self.coord
        return road_cells