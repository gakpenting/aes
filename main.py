from aes import AES
# key 128 itu 32
key = '000102030405060708090a0b0c0d0e02'
print(len(key))
# Hex string to encrypt!
data = 'panda'
# Set AES mode of operation (ECB, w/ hex input)
aes = AES(mode='ecb', input_type='text')
# Encrypt data with your key
cyphertext = aes.encryption(data, key)
# Decrypt data with the same key
plaintext = aes.decryption(cyphertext, key)

print(plaintext)