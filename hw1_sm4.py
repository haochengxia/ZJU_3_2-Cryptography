# target: check that encryption & key expandasion in SM4 are both invertible.

# Part 1 proof of key expandasion

from pysm4 import encrypt, decrypt, get_round_keys, reduction_mk, encrypt_ecb, decrypt_ecb

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

# Part 3 test 4 billion words
one_word = 'word'
four_billion_words = 4000000000 * one_word
key = 'hello, world!'
hash_plain_text = hash(four_billion_words)
cipher_text = encrypt_ecb(four_billion_words, key)
print("decrypt done")
hash_decrypt_text = hash(decrypt_ecb(cipher_text, key))
print(hash_decrypt_text == hash_plain_text)