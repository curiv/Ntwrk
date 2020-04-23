from sympy import Symbol, div
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

CRC8_poly = "111010101" 
CRC8_poly = list(CRC8_poly)
#message = input("Insert a message to find a CRC summ:\n>")
message = "12"
binary_message = list(text_to_bits(message))

# Skip first zeroes
for index,bit in enumerate(binary_message):
    if bit == '1':
        binary_message = binary_message[index:]
        break

print(f"Binary message {binary_message}" )
print(f"CRC8_poly {CRC8_poly}")

for i in range(8):
    xored = int(binary_message[i]) ^ int(CRC8_poly[i])
    print(binary_message[i], CRC8_poly[i], xored)
    binary_message[i] = str(xored)

print(binary_message)


for index,bit in enumerate(binary_message):
    if bit == '1':
        binary_message = binary_message[index:]
        print(index)
        break
print(f"Binary message {binary_message}" )
print(f"CRC8_poly {CRC8_poly}")

for i in range(8):
    xored = int(binary_message[i]) ^ int(CRC8_poly[i])
    print(binary_message[i], CRC8_poly[i], xored)
    binary_message[i] = str(xored)

print(binary_message)

