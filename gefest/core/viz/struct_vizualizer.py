import matplotlib.pyplot as plt

from gefest.core.structure.domain import Domain
from gefest.core.structure.structure import Structure


class StructVizualizer:
    def __init__(self, domain: Domain):
        self.domain = domain

    def plot_structure(self, struct: Structure, info, start_point, end_point, coord_wells = [[], []], invalid_points = [[], []]):
        
        for poly in struct.polygons:
            self.plot_poly(poly, info, start_point, end_point)
        
        boundary = self.domain.bound_poly
        x = [pt.x for pt in boundary.points]
        y = [pt.y for pt in boundary.points]

        plt.scatter(invalid_points[0], invalid_points[1], marker = '+', c = 'r', label = 'Invalid point')
        plt.scatter(coord_wells[0], coord_wells[1], marker = 'o', c = 'y', label = 'Location of wells')
        
        plt.plot(x, y)
        plt.legend()

    def plot_poly(self, poly, info, start_point, end_point):
        type = info['type']
        fitness = info['fitness']

        x = [start_point[0]]
        x += [pt.x for pt in poly.points]
        x += [end_point[0]]

        y = [start_point[1]]
        y += [pt.y for pt in poly.points]
        y += [end_point[1]]
        
        plt.plot(x, y, label=f'{type}, NPV_road = {fitness:.3f}')

        plt.scatter(x[0], y[0], c = 'g', label = 'Starting point of the road')
        plt.scatter(x[-1], y[-1], c = 'r', label = 'Ending point of the road')
        plt.legend()
