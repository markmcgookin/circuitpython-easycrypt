import aesio
from binascii import hexlify, unhexlify

name = "EasyCrypt"
mode = aesio.MODE_CTR

def encrypt_string(keystring, inpstring, ivstring):

    # Convert our string key to a byte array
    key = bytearray(keystring)

    # Convert the iv (Initialisation Vector/Nonce) to a byte arry
    iv = bytearray(unhexlify(ivstring))

    # Convert our string that we want to encrypt to a byte array
    inp = bytearray(inpstring)
     
    # Create a byte array to store the output in
    outp = bytearray(len(inp))

    # Create our cypher
    cipher = aesio.AES(key, mode, iv)

    # Encrypt the input into the output
    cipher.encrypt_into(inp, outp)

    # Convert that into the hex representation of the bytes, then decode that to 
    # a string for us to return (easy to save in a database/file etc)
    trans = hexlify(outp).decode()

    return trans

def decrypt_string(keystring, inpstring, ivstring):
    # Convert our string key to a byte array
    key = bytearray(keystring)

    # Convert the iv (Initialisation Vector/Nonce) to a byte arry
    iv = bytearray(unhexlify(ivstring))

    # Unhex the input string, then convert it into a byte array
    inp = bytes(unhexlify(inpstring))

    # Create a byte array to store the output in
    outp = bytearray(len(inp))
    
    # Create our cypher
    cipher = aesio.AES(key, mode, iv)
    
    # Decrypt the data into the output array
    cipher.decrypt_into(inp, outp)
    
    # Conver the unencrypted bytes into a string to return
    trans = outp.decode()

    return trans