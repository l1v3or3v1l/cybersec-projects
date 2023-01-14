import base64 as b64

def encode():
    fname = input("Enter filename to be encoded : ")
    fcontent = open(fname, 'rb').read()
    enc = b64.b64encode(fcontent)
    nfname = open(f'{fname}.b64enc', 'wb')
    nfname.write(enc)

def decode():
    fname = input("Enter filename to be decoded : ")
    fcontent = open(fname, 'rb').read()
    dec = b64.b64decode(fcontent)
    nfname = open(f'{fname}.b64dec', 'wb')
    nfname.write(dec)

def main():
    ch = int(input("1. Encode\n2. Decode\nEnter choice : "))
    if ch == 1:
        encode()
    if ch == 2:
        decode()


if __name__ == "__main__":
    main()