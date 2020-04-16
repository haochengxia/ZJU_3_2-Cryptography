# target: check that encryption & key expandasion in SM4 are both invertible.

# Part 1 proof of key expandasion

from pysm4 import encrypt, decrypt, get_round_keys, reduction_mk

clear_num = 0x0123456789abcdeffedcba9876543210
mk = 0x0123456789abcdeffedcba9876543210

round_key = get_round_keys(mk)
re_mk = reduction_mk(round_key)
proof_key_expand = (mk == re_mk)
print("Reduction mk equals to origin mk:")
print(proof_key_expand)

# Part 2 proof of encryption

cipher_num = encrypt(clear_num, mk)
flag = (clear_num == decrypt(cipher_num, mk))
print("Reduction plaintext equals to origin plaintext:")
print(flag)

print(hex(re_mk))
