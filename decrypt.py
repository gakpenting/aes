from aes import AES
import sys
# key 128 itu 32
key = '000102030405060708090a0b0c0d0e02'

# Hex string to encrypt!
cyphertext = sys.argv[1]
# Set AES mode of operation (ECB, w/ hex input)
aes = AES(mode='ecb', input_type='text')
# Encrypt data with your key
plaintext = aes.decryption(cyphertext, key)
# Decrypt data with the same key
print(plaintext)