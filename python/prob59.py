#!/usr/bin/env python3.3

import string

alphabet = string.ascii_lowercase

with open('cipher1.txt', 'r') as en_file:
    s = en_file.read()
    s = s.strip('\n')
    msg = [int(n) for n in s.split(sep=',')]

with open('decrypted1.txt', 'w') as de_file:
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

                    de_file.write(''.join(str(char) for char in decoded))
                    de_file.write(' '.join(["\nencryption key:", a, b, c, "\n"]))
