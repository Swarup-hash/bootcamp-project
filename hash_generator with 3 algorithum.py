import hashlib

message = "Swarup".encode()

print()

print("MD5:", hashlib.md5(message).hexdigest())

print()

print("SHA-256:", hashlib.sha256(message).hexdigest())

print()

print("SHA-3-256:", hashlib.sha3_256(message).hexdigest())

print()