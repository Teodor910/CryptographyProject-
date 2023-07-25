from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def writeEncryption():

    key = b"sixteenbytescode"
    userText = input("Enter the text you want to encrypt: ")
    plainText = f"{userText}".encode()

    cipher = AES.new(key, AES.MODE_CBC)

    cipherText = cipher.encrypt(pad(plainText, AES.block_size))

    with open("c_File", "wb") as c_File:
        c_File.write(cipher.iv)
        c_File.write(cipherText)

def main():
    writeEncryption()

if __name__ == "__main__":
    main()

