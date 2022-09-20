# Given the following set of linear congruences:

# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

# Find the integer a such that x ≡ a mod 935

import numpy as np

mods = [5,11,17]
a = [2,3,5]

def mult_inv(i1, mod):
    d = 1
    for i in range(2,100):
        if i*i1 % mod == 1:
            return i
    return d

def CRMT():
    m = np.prod(mods)
    M = [1 for _ in range(len(mods))]
    
    for i in range(len(mods)):
        for k in range(len(mods)):
            if i != k:
                M[i] = M[i]*mods[k]

    y = [M[i]%mods[i] for i in range(len(mods))]

    invs = [0 for _ in range(len(mods))]
    for i in range(len(y)):
        #Wow, you can actually preform a mod multiplicative inverse like this
        invs[i] = pow(y[i], -1, mods[i])

    x = 0

    for i in range(len(invs)):
        x = x + (a[i]*M[i]*invs[i])
    
    ans = x - m
    return ans
        

if __name__ == "__main__":
    #Make it mod 935
    print(CRMT() % 935)