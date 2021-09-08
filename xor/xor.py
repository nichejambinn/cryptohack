s = "label"
arr = [ord(c) ^ 13 for c in s]
s = "".join([chr(i) for i in arr])

print(s)