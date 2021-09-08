from Crypto.Util.number import long_to_bytes
import telnetlib
import json
import base64

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def rot(s, k=13):
    abc = "abcdefghijklmnopqrstuvwxyz"
    secret = ''.join([abc[(abc.find(c)+k)%26] if c in abc else c for c in s])
    return secret

n = 0
while n < 100:
    received = json_recv()
    print(received)

    if (n == 99):
        break

    if received["type"] == "hex":
        bytes_str = bytes.fromhex(received["encoded"])
        decoded = bytes_str.decode('utf-8')
    elif received["type"] == "rot13":
        decoded = rot(received["encoded"])
    elif received["type"] == "utf-8":
        decoded = "".join([chr(i) for i in received["encoded"]])
    elif received["type"] == "base64":
        bytes_str = base64.b64decode(received["encoded"])
        decoded = bytes_str.decode('utf-8')
    elif received["type"] == "bigint":
        long_str = int(received["encoded"], 16)
        bytes_str = long_to_bytes(long_str)
        decoded = bytes_str.decode('utf-8')
    else:
        print("error")
        break

    print(decoded)
    to_send = {
        "decoded": decoded
    }

    json_send(to_send)