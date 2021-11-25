import metutils
import test_metutils
import numpy as np


def test_roundtrip_f2c():
    vals = np.random.randint(-100, 1000, 20)
    for val in vals:
        assert val == metutils.f2c(metutils.c2f(val))
