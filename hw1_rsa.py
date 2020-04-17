from pyrsa import list_all_ed, encrypt, decrypt, gen_d

p = int(input('p：'))
q = int(input('q：'))
print("Key pairs for chosen:")
print(list_all_ed(p,q))
n = p*q
e = int(input('secret key：'))
d = gen_d(p,q,e)
print('The key pair you chosed is: {}'.format([e,d]))
num = 10
cipher_num = encrypt(num,e,n)
print(decrypt(cipher_num,d,n))