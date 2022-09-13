#Multiplicative inverse of g
#3 * d = 1 mod 13

def mult_inv(i1, mod):
    d = 1
    for i in range(2,100):
        if i*i1 % mod == 1:
            return i
    return d

print(mult_inv(3,13))
