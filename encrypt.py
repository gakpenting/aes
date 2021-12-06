from aes import AES
import sys

key = '000102030405060708090a0b0c0d0e02'

# Hex string to encrypt!
data = sys.argv[1]
# Set AES mode of operation (ECB, w/ hex input)
aes = AES(mode='ecb', input_type='text')
# Encrypt data with your key
cyphertext = aes.encryption(data, key)
# Decrypt data with the same key
print(cyphertext)