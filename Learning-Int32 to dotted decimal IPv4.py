#  Convert integer to 32 bit binary
#  '{:032b}'.format(n)

#  Decimal is base 10 = 0123456789
#  Binary is base 2 = 1s and 0s
#  Hex is base 15 = 0 to 9, A to F
print(int("255", 10))  # Decimal
print(int("101", 2))   # Binary
print(int("1A", 15))   # Hexadecimal


#  Converting int32s to binary exercise
def int32v1_to_ip(int32):
    z = []
    x = '{:032b}'.format(int32)

    for i in range(0, 32, 8):
        z.append(str(int(x[i:i + 8], 2)))

    print(".".join(z))


#  Comprehension of above code
def int32v2_to_ip(int32):
    return ".".join(str(int('{:032b}'.format(int32)[i:i + 8], 2)) for i in range(0, 32, 8))


int32v1_to_ip(2154959208)  # , "128.114.17.104")
int32v1_to_ip(0)  # , "0.0.0.0")
int32v1_to_ip(2149583361)  # , "128.32.10.1")

int32v2_to_ip(2154959208)  # , "128.114.17.104")
int32v2_to_ip(0)  # , "0.0.0.0")
int32v2_to_ip(2149583361)  # , "128.32.10.1")
