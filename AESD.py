from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def readDecryption():

    key = b'sixteenbytescode'

    with open("c_File", "rb") as c_File:
        iv = c_File.read(16)
        ciphertext = c_File.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    plainText = unpad(cipher.decrypt(ciphertext), AES.block_size)

    print(plainText)

def main():
    readDecryption()

if __name__ == "__main__":
    main()
