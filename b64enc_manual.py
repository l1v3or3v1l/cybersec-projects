string = input()
padding = ''

if (len(string) % 3 > 0):
    padding = '=' * (3 - len(string) % 3)

print(string)

eightbit = ''.join(format(ord(i), '08b') for i in string)
paddingbits = ''.join(format(ord(i), '08b') for i in padding)

eightbit += '0' * len(paddingbits)

sixbit = [eightbit[i:i+6] for i in range(0, len(eightbit), 6)]

b64ascii = [int(i, 2) for i in sixbit]

b64string = ""

for ascii in b64ascii:
    if ascii < 26:
        b64string += chr(65 + ascii)
    elif ascii < 52:
        b64string += chr(97 + ascii - 26)
    elif ascii < 62:
        b64string += chr(48 + ascii - 52)
    elif ascii == 62:
        b64string += '+'
    elif ascii == 63:
        b64string += '/'

encoded = b64string
if len(padding) > 0:
    encoded = b64string[:-len(padding)] + padding

print(encoded)