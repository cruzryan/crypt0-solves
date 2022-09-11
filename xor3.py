d = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

import pwn
for i in range(255):
    f = pwn.xor(d,i)
    print(''.join([chr(f[x]) for x in range(len(f))]))