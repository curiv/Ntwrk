from sympy import Symbol, div

CRC8_poly = "111010101" 

message = input("Insert a message to find a CRC summ:\n>")

# convert all characters to the binary form
binary_message = ''
for char in message:
    decimal = ord(char)

    # get rid of '0b' at the beginning
    binary = str(bin(decimal)[2:])

    # fill unimportant bit at the beginning
    if len(binary) == 7:
        binary = '0' + binary

    print(f"{char} - {decimal} - {binary}")

    binary_message += binary

print("Binary message:", binary_message)
print("CRC8 poly:", CRC8_poly)

for i in range(len(binary_message) - len(CRC8_poly) + 1):
    octet = binary_message[i:i+len(CRC8_poly)]
    print(octet)

