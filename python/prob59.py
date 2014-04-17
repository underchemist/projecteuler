#!/usr/bin/env python3.3

import string

alphabet = string.ascii_lowercase

with open('cipher1.txt', 'r') as en_file:
    s = en_file.read()
    s = s.strip('\n')
    msg = [int(n) for n in s.split(sep=',')]

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            key1 = ord(a)
            key2 = ord(b)
            key3 = ord(c)

            decoded = []
            for i in range(0, len(msg) - 3, 3):
                decoded.append(chr(msg[i] ^ key1))
                decoded.append(chr(msg[i + 1] ^ key2))
                decoded.append(chr(msg[i + 2] ^ key3))

            if decoded.count(' ') > 60:
                decoded_str = ''.join(char for char in decoded)
                if decoded_str.count('the') > 5:
                    print(decoded_str)
                    print('encryption key:', a, b, c)
                    print('sum of decoded characters:', sum([ord(char) for char in decoded]))
