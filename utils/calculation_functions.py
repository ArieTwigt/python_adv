# standard library
from math import pow, pi
from typing import Union


def calc_circle(diameter: Union[float, int], # positional argument
                rounding: int=2               # default argument
                ) -> Union[float, int]:
    '''
    Function that returns the size of a circle:

    Inputs:
    * diameter: diameter of the circle

    Output:
    * size: size of the circle
    '''

    # validate the data type
    required_types = [float, int]

    if type(diameter) not in required_types:
        raise TypeError(f"Wrong type. Got {type(diameter)}")

    radius = diameter / 2
    size = pow(radius, 2) * pi

    size_rounded = round(size, rounding)
    return size_rounded




