from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from AES import writeEncryption
from AESD import readDecryption

choice = input("Would you like to encrypt data? y/n?")

if choice == "y":
    writeEncryption()
elif choice == "n":
    readDecryption()
else:
    print("Invalid Input")