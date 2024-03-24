from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sys
import binascii

# Declare plain and cipher text
plaintext = b"This is a top secret."
ciphertext = binascii.unhexlify(b"8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9")

# Check file input
if len(sys.argv) != 2:
    print("Error no file input")
    exit(1)

lines = None

# Open dictionary file and parse lines
with open(sys.argv[1], 'r') as file:
    lines = [line.rstrip() for line in file]


# Set up possible keys to use in brute force
possibleKeys = []
for word in lines:
    if len(word) < 16:
        byteString = word.encode('utf-8')

        # Calculate padding length of key
        paddingLength = 16 - len(byteString)

        paddedByteString = byteString + bytes([0x20] * paddingLength)

        # Append to possible keys
        possibleKeys.append(paddedByteString)     

# Encrypt with each possible key
for key in possibleKeys:
    
    # Create cipher for AES-CBC with zeros as iv and use the possible key
    cipher = AES.new(key, AES.MODE_CBC, iv=bytes([0]*16))
    ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    
    # Compare the encrypted ct_bytes with the possible key to see
    # if it is equal to the known ciphertext
    if ct_bytes == ciphertext:
        print(f"CT_BYTES {ct_bytes}    known cipher {ciphertext}")
        print(f"Success, key is {key}")
        exit(0)
