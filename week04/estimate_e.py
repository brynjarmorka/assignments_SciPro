#%%
import math

#%%
n = 100
e1 = 0
for i in range(n + 1):
    e1 += 1.0 / math.factorial(i)
    # print(e1)
print(e1)

e2 = 0
for i in range(n + 1)[::-1]:
    e2 += 1.0 / math.factorial(i)
    print(e2)
print(e2)

#
print(math.e - e1)
# print(math.e - e2)

# So e2 is closest to math.e (its the same), while e1 is (e1-e2) off.
# For e1 we start with the big numbers, thus the precision is lost,
# while for e2 we start with the tiny tiny numbers, and that sets the
# right precision from the start. Actually, e1 does not change after
# 18 iterations, while e2 uses 99 iterations to get to the right number.

# Also, e2 have higher floating point precision at the beginning,
# it starts with 1.07e-158, but when it comes closer to 0, between
# 0.0002 and 0.009 it looses some decimal precision. Further loss
# happens when e2 closes on 2.7...


# We learn that smaller floating numbers have higher precision, and
# the way floats are added together actually makes a difference for
# the precision of the result (add smaller before bigger).
