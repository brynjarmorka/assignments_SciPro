"""
This is

'101010' ->  42

'10000.1' -> 16.5

'1011101101.10101011' -> 749.66796875
"""

#%%
import numpy as np
import matplotlib.pyplot as plt


def binary_to_decimal(binary):
    """
    calculate the start 2-exponent.
    loop through the bits and add 2**exp to summen.
    can loop thorugh the whole, because the exponent goes negative.
    :param binary: string of '1', '0' or '.'
    :return: float
    """
    summen = 0.0
    bin_split = binary.split(".")
    exp = len(bin_split[0]) - 1  # calculate the start exponent
    for bin in binary:
        if bin == "1":
            summen += 2 ** exp
        # add nothing when 0
        exp -= 1  # reduce the exponent by 1
        if bin == ".":
            exp += 1
    return summen


def bse(binary):  # best_standard_ever()
    """
    32 bits long sequence of bits,
    the first 5 bits (starting from the left) being used to give the position of the dot,
    and the remaining 27 bits used to represent the number.
    Uses the function over, binary_to_decimal()
    :param binary: string
    :return: float
    """
    if len(binary) != 32:
        raise ValueError(f"Please use 32 bit number, len(binary) = {len(binary)}")
    dot_pos = int(binary_to_decimal(binary[:5]))  # five first are dot
    number = str(binary[5:])  # cut off the dot position
    return binary_to_decimal(number[:dot_pos] + "." + number[dot_pos:])


def bse_check():
    print(f"highest number = {bse('11111111111111111111111111111111')}")
    print(f"next highest number is {bse('11111111111111111111111111111110')}")
    print(f"highest decimal number is {bse('11010111111111111111111111111111')}")
    print("(here we are wasting some values because 11111 = 31, and dot_max = 27")

    print(f"lowest number = {bse('00000000000000000000000000000001')}")
    print(f"2. lowest number = {bse('00000000000000000000000000000010')}")
    print("The difference between two possible numbers change when the dot is moved,")
    print("but not when the dot is static.")


def list_all_dot_pos():
    return [bin(i)[2:].zfill(5) for i in range(28)]
    # only 27 possible values for the dot. 28-31 are superficial


def precision_test():
    all_dots = list_all_dot_pos()  # will be the list of all possible dots
    prec = []
    zero = "".zfill(27)
    one = "1".zfill(27)
    ones = []
    for dot_pos in all_dots:
        z = dot_pos + zero  # the zero value
        o = dot_pos + one  # the one value
        prec.append(bse(o) - bse(z))
        ones.append(bse(o))

    plt.loglog(ones, prec, ".")
    plt.grid(1)
    plt.show()

    print(
        "No, we should not use this BSE, because the precision with one decimal is terrible"
    )


precision_test()

# %% plotting of precision

# bse_check()
