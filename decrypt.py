from Crypto.Cipher import AES

filename = "file.m4a"

key = b"password"*4

with open("encfile.m4a", "rb") as f:
    aes = AES.new(key, AES.MODE_CTR, nonce=f.read(8))
    dec = aes.decrypt(f.read())

with open("decfile.m4a", "wb") as f:
    f.write(dec)

print(aes.nonce)
