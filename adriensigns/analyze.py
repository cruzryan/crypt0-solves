from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'

def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])

    for i in flag:
        print(bin(i)[2:].zfill(8))

    # print(plaintext)
    print("\n")
    print(plaintext)
    print(len(plaintext))
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        # print(b)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


encrypt_flag(FLAG)
# print(encrypt_flag(FLAG))
