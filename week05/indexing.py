#%%
import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
#
# x[:, 1]
#
# x[slice(0, 2, 1), 1]
#
# x[(slice(0, 2, 1), 1)]
#
# x[slice(0, 2, 1), slice(1, 2, 1)]
#
# x[..., 1]
#
# x[::1, 1]
#
# x[[0, 1], 1]
#
# x[:, -2]
#
# x[:, 1:2]
#
# x[:, [1]]


#%%


# What is the ... syntax doing? Again, it is the literal equivalent of an actual python object: what is it?
#
# some of these indexing operations are truly equivalent to the “obvious” one, x[:, 1]. List them.
#
# Classify these operations (i) in basic and advanced operations, and (ii) by the shape of their output. Explain.
#
# I’d like my array a = x[:, 1:2] to have a shape of (2, ) like most of the other operations listed above. What can I
# do to reshape it?
a = x[:, 1:2]
print(a)
print(f"a.flatten() = {a.flatten()}")
print(f"a.flatten().shape = {a.flatten().shape}")
