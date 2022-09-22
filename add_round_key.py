state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

import numpy as np
import pwn

mat = []

#Bad version
def add_round_key(s, k):
    return [[ pwn.xor(state[x],round_key[y]) for x in range(4)] for y in range(4)]

#More elegant version
def arr_round_key_better(s,k):
    return [[pwn.xor(sss,kkk) for (sss,kkk) in zip(ss, kk)] for ss,kk in zip(s,k)]


def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return "".join([x.decode('ascii') for x in np.array(matrix).flatten()])


print(matrix2bytes(arr_round_key_better(state, round_key)))

# print(matrix2bytes(add_round_key(state, round_key)))

# crypto{r0undk3y}