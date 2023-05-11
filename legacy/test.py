import math
import itertools
import numpy as np
from fractions import Fraction

def calcWeight(list):
    num = len(list)
    numer = math.factorial(np.sum(list))
    denom = 1
    for i in range(num):
        denom = denom * math.factorial(list[i])
    weight = numer / denom
    return weight

list = [7, 0, 1, 0, 2]
print(calcWeight(list))