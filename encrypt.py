from Crypto.Cipher import AES

filename = "file.m4a"

key = b"password"*4
aes = AES.new(key, AES.MODE_CTR)

with open("file.m4a", "rb") as f:
    enc = aes.encrypt(f.read())

with open("encfile.m4a", "wb") as f:
    f.write(aes.nonce)
    f.write(enc)

print(aes.nonce)
