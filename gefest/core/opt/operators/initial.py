from copy import deepcopy
from multiprocessing import Pool

from gefest.core.algs.postproc.resolve_errors import postprocess
from gefest.core.opt.constraints import check_constraints
from gefest.core.structure.domain import Domain
from gefest.core.structure.structure import get_random_structure

MAX_ITER = 50000
NUM_PROC = 1


def initial_pop_random(size: int, domain: Domain, initial_state=None, invalid_points = []):
    # Method for initialization of population

    population_new = []

    if initial_state is None:
        while len(population_new) < size:
            print('init', len(population_new))
            if NUM_PROC > 1:
                with Pool(NUM_PROC) as p:
                    new_items = p.map(get_pop_worker, [domain, invalid_points] * size)
            else:
                new_items = []
                for i in range(size):
                    new_items.append(get_pop_worker(domain, invalid_points))

            for structure in new_items:
                population_new.append(structure)
                if len(population_new) == size:
                    return population_new
    else:
        for _ in range(size):
            population_new.append(deepcopy(initial_state))
    return population_new


def get_pop_worker(domain, invalid_points):
    # Create a random structure and postprocess it
    structure = get_random_structure(domain=domain, invalid_points = invalid_points)
    structure = postprocess(structure, domain)
    constraints = check_constraints(structure=structure, domain=domain)
    max_attempts = 3  # Number of postprocessing attempts
    while not constraints:
        structure = postprocess(structure, domain)
        constraints = check_constraints(structure=structure, domain=domain)
        max_attempts -= 1
        if max_attempts < 0:
            # If the number of attempts is over,
            # a new structure is created on which postprocessing is performed
            structure = get_random_structure(domain=domain, invalid_points = invalid_points)
            structure = postprocess(structure, domain)
            constraints = check_constraints(structure=structure, domain=domain)
    return structure
