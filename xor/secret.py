from pwn import xor

# cipher = plain ^ key
# plain = crypto{...}

hex_val = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

plain = bytes("crypto{", 'utf-8')

bytes_str = bytes.fromhex(hex_val)

key = xor(bytes_str, plain)

print(key)

key = "myXORkey"
plain = xor(bytes_str, bytes(key, 'utf-8'))

print(plain)