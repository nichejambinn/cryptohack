import Crypto.Util.number as pyc

long_val = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_str = pyc.long_to_bytes(long_val)

print(bytes_str)