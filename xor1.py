i1 = "label"
i2 = 13
k = [ chr(13 ^ ord(i1[x])) for x in range(len(i1))]

print(k)

import pwn
print(pwn.xor(i1, i2))



