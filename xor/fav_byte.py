from pwn import xor

hex_val = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

bytes_str = bytes.fromhex(hex_val)

print(bytes_str)

for i in range(2**7):
    val = xor(bytes_str, i)
    if "crypto" in val.decode('utf-8'):
        print(val)