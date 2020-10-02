import rsa
pub,priv = rsa.newkeys(512)
talk = "Hello"
info = rsa.encrypt(talk,pub)

real = rsa.decrypt(info,priv)
real = real.decode("utf-8")
print(real)