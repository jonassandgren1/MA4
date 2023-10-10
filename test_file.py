import random
import math
import matplotlib.pyplot as plt

# def monte_carlo_pi(n):
#     nc = 0
#     points_inside = []
#     points_outside = []

#     for _ in range(n):
#         x, y = random.uniform(-1, 1), random.uniform(-1, 1)
#         if x**2 + y**2 <= 1:
#             nc += 1
#             points_inside.append((x, y))
#         else:
#             points_outside.append((x, y))

#     pi_approx = 4 * nc / n

#     print(f"Number of points inside the circle: {nc}")
#     print(f"Approximation of π: {pi_approx}")
#     print(f"Builtin constant π: {math.pi}")

#     plt.figure()
#     plt.scatter(*zip(*points_inside), color='red')
#     plt.scatter(*zip(*points_outside), color='blue')
#     plt.gca().set_aspect('equal', adjustable='box')
#     #plt.savefig('monte_carlo_pi.png')

# monte_carlo_pi(10000)  # Change this to the number of points you want to generate

from functools import reduce
import time
import concurrent.futures as future

def monte_carlo_hyper(n, d):
    points = [[random.random() for i in range(d)] for i in range(n)] #generates n random points in d dimensions
    inside = list(filter(lambda point: sum(x**2 for x in point) <= 1, points))
    ratio = len(inside) / n
    volume = ratio * (2**d)
    return volume 

def calc_volume(d):
    return (math.pi**(d/2)) / math.gamma(d/2 + 1)

n = 10000000
d = 11

approx = monte_carlo_hyper(n, d)
calc = calc_volume(d)

    
print(f'approx volume: {approx}')
print(f'calc volume: {calc}')

from time import perf_counter as pc
import concurrent.futures as future



if __name__ == '__main__':

    start = pc()
    result = monte_carlo_hyper(n, d)
    end = pc()
    print(f'process took: {end-start} sec')

    for n_pros in [10]:
        d_new = 11
        n_new = [(1000000 // n_pros, d_new) for _ in range(n_pros)]
        start1 = pc()
        with future.ProcessPoolExecutor() as ex:
            result = list(ex.map(monte_carlo_hyper, n_new))
            for r in result:
                print(r)
                print(f'it took {end1-start1} sec')
        end1 = pc()
        print(f'for {n_pros} number of threads, it took {end1-start1} sec')
