import hashlib

text = ' Hello! '

m = hashlib.md5(text.encode('UTF-8'))
print(m.hexdigest())