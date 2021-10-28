#%% imports
import time
import numpy as np
import random
import matplotlib.pyplot as plt

#%% helper functions


def coords_py(n):
    return [[random.random(), random.random()] for i in range(n)]


c1 = coords_py(10)
print(c1)


def coords_np(n):
    return np.random.rand(n, 2)


c2 = coords_np(10)
print(c2)


def monte_carlo_pi_estimate(coordinates):
    inliers = 0
    for c in coordinates:
        if (c[0] ** 2 + c[1] ** 2) < 1:
            inliers += 1
    return 4 * inliers / len(coordinates)


def make_n_list(start, end):
    """ [1e(start), 1e(start+1), ... 1e(end)]"""
    return [10 ** i for i in range(start, end + 1)]


def mc_timer(listen):
    print("n,  py,  np")
    np_times = []
    for n in listen:
        # #  pure python
        # start_time = time.perf_counter()
        # py_pi = monte_carlo_pi_estimate(coords_py(n))
        # py_time = time.perf_counter() - start_time
        #  numpy
        start_time = time.perf_counter()
        np_pi = monte_carlo_pi_estimate(coords_np(n))
        np_time = time.perf_counter() - start_time
        #  print result
        # print(
        #     f"{n:.0e}, \t {py_time:.2e}, \t {np_time:.2e} \t\t\t py_pi = {py_pi}, \t\t np_pi = {np_pi}"
        # )
        np_times.append(np_time)
    return np_times


#%% timer loop

n_list = make_n_list(1, 7)
np_times = mc_timer(n_list)

# n,         py,         np
# 1e+01, 	 4.38e-05, 	 7.45e-05
# 1e+02, 	 1.13e-04, 	 1.63e-04
# 1e+03, 	 1.03e-03, 	 1.59e-03
# 1e+04, 	 9.47e-03, 	 1.34e-02
# 1e+05, 	 9.30e-02, 	 1.05e-01
# 1e+06, 	 8.30e-01, 	 1.10e+00
# 1e+07, 	 1.09e+01, 	 1.13e+01

#  with n > 1e8 makes np take more than 100s


#%% plotting

plt.plot(n_list, np_times)
plt.xlabel("N")
plt.ylabel("time [s]")
plt.show()
#  it's a straight line with constant incline
