from PIL import Image
#from operator import xor
from pwn import xor
import numpy as np

# plain1 ^ key = lemur
# plain2 ^ key = flag

lemur = Image.open('lemur.png')
flag = Image.open('flag.png')

lemur_bytes = lemur.tobytes()
flag_bytes = flag.tobytes()

x = xor(lemur_bytes, flag_bytes)

result = Image.frombytes(flag.mode, flag.size, x)
result.save('result.png')