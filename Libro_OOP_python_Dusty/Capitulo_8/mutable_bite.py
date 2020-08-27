b = bytearray(b"abcdefgh")
b[4:6] = b"\x15\xa3"
print(b)

b = bytearray(b'abcdef')
b[3] = ord(b'g')
b[4] = 68
print(b)