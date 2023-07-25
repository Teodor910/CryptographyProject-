from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"sixteenbytescode"

plainText = b"mypassword"

cipher = AES.new(key, AES.MODE_CBC)

cipherText = cipher.encrypt(pad(plainText, AES.block_size))

with open("c_File", "wb") as c_File:
    c_File.write(cipherText)

