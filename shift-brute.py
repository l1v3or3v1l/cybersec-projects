
def main():
    encodedStr = input()
    for shiftVal in range(1, 26):
        possDecodedStr = ""
        for char in encodedStr:
            if (char.isalpha()):
                shiftedASCII = ord(char) - shiftVal
                if (shiftedASCII < 65):
                    shiftedASCII = 91 - (65 % shiftedASCII)
                if (shiftedASCII > 90 and shiftedASCII < 97):
                    shiftedASCII = 123 - (97 % shiftedASCII)
                possDecodedStr += chr(shiftedASCII)
            else:
                possDecodedStr += char
        print(f"ShiftVal : {shiftVal}, Str : {possDecodedStr}")

if __name__ == '__main__':
    main()