import numpy as np

#generating impossible points
def impossible_points_generation(count_points = 5, shape_plane = np.array([21, 21])):
    '''
    count_points: number of impossible points
    shape_plane: field surface size
    '''
    points = []
    
    for _ in range(count_points):
        points.append(tuple(np.random.randint(shape_plane)))
        
    return points

#The class that defines the field
class Field(): 
    def __init__(self, data, impossible_points = []):
        '''
        data: field data
        impossible_points: impossible points on the surface
        
        Class Parameters:
        data: field data 
        impossible_points: impossible points on the surface
        size: field size
        '''
        
        self.data = data
        self.impossible_points = impossible_points
        
        self.size = data.shape
        self.all_bounds = [self.size[0] + 1, self.size[1] + 1, self.size[0] + 1, self.size[1] + 1, self.size[2] + 1] 