p = 29
ints = [14, 6, 11] 


def find_quad(x, mod):
    for i in range(mod-1):
        if (i*i) % mod == x:
            return i
    return 0        

print([find_quad(ints[i], p) for i in range(len(ints))])
