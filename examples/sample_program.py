import pycuber as pc
from pycuber.solver import CFOPSolver

c = pc.Cube()  # create a Cube object
alg = pc.Formula()  # algorithms are represented by Formula objects
random_alg = alg.random()  # generate a random algorithm
c(random_alg)  # apply that algorithm to the cube to shuffle it

solver = CFOPSolver(c)  # create the solver for the cube


solution = solver.solve()  # solve it, faster than Feliks, usually...

print(solution)
