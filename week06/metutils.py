def f2c(tf):
    """Converts degrees Fahrenheit to degrees Celsius"""
    r = (tf - 32) * 5 / 9
    return r


def c2f(tc):
    """
    Converts degrees Celsius to Farenheit
    :param tc: temp C
    :return: temp F
    """
    r = (tc * 9 / 5) + 32
    return r
