# easycrypt
A tiny little python class for encrypting and decrypting a string


## USAGE 
```python
import EasyCrypt

keystring = "SixteenByteKey!!"
inpstring = "Some super secret string, that I don't want you to see."

# This is the initialisation vector/nonce. I generated it with the below code. As you 
#  will need it to decrypt later on, you might want to store it and not just generate it each time
#  I just generated it like this and printed this one out to store it.
#  
#  import os
#  from binascii import hexlify, unhexlify
#  ivstring = hexlify(os.urandom(16)).decode()

ivstring = "aba0a3bde34a03487eda3ec96d5736a8"

crypted = EasyCrypt.encrypt_string(keystring, inpstring, ivstring)
print(crypted)

decrypted = EasyCrypt.decrypt_string(keystring, crypted, ivstring)
print(decrypted)
```