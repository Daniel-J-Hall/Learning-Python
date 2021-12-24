class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key * 100
        self.alphabet = alphabet

    def encode(self, text):
        cypher = []  # List for appending the encoded letters into.
        for x in range(len(text)):
            if text[x] in self.alphabet:  # Check if character is in alphabet var.

                encode = (ord(text[x]) + ord(self.key[x]) - 64) % 26
                #  Algebraic encryption via wikipedia but subtracting the ascii decimals to make it work.

                encode += 97
                #  Afterwards adding back the ascii decimals to convert it back into the right characters.

                cypher.append(chr(encode))

            else:
                cypher.append(text[x])  # Simply append other characters.

        print("".join(cypher))  # Joining and returning cypher.
        return "".join(cypher)

    def decode(self, text):
        decipher = []

        for x in range(len(text)):

            if text[x] in self.alphabet:

                decode = (ord(text[x]) - ord(self.key[x])) % 26
                #  Algebraic decryption via wikipedia.

                decode += 97
                #  Afterwards adding back the ascii decimals to convert it back into the right characters.

                decipher.append(chr(decode))

            else:
                decipher.append(text[x])

        print("".join(decipher))
        return "".join(decipher)


abc = "abcdefghijklmnopqrstuvwxyz"  # Alphabet to check for characters in message.
key = "password"  # Key for cypher / deciphering
c = VigenereCipher(key, abc)

c.encode("it's a cypher!")  # , 'xt'k o fnpzwn!')
c.decode("xt'k o fnpzwn!")  # , 'it's a cypher!')

c.encode('testing zxcvb')  # , 'ieklebx oxunx')
c.decode('ieklebx oxunx')  # , 'testing zxcvb')

c.encode('THISISACYPHER')  # , 'THISISACYPHER')
c.decode('THISISACYPHER')  # , 'THISISACYPHER')
