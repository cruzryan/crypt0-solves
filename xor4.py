import pwn

encrypted_msg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted_msg = bytes.fromhex(encrypted_msg)

flag_start = "crypto{"

key_arr = []

for i in range(len(flag_start)):
    key_arr.append(pwn.xor(flag_start[i], encrypted_msg[i]))
key_arr.append(ord("y"))

kl = (key_arr*10)[:len(encrypted_msg)]

flag = []

for i in range(len(kl)):
    flag.append(pwn.xor(encrypted_msg[i], key_arr[i % len(key_arr)]))

print("".join([chr(x) for x in range(len(kl))]))

#crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}


#Solution v2
k1 = pwn.xor("crypto{".encode(), encrypted_msg)[:len("crypto{")]
k2 = pwn.xor("}".encode(), encrypted_msg[-1])
key = k1 + k2
flag = pwn.xor(key, encrypted_msg)

#Elegant solution
print(flag)