# Функция перевода текста в бинарный вид
# На входе текст
# На выходе его бинарный код
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

# Функция на пустой нулевой остаток
# На входе список
# На выходе True или False
def have_zero_reminder(bits):
    for bit in bits:
        if  bit == '1':
            return False
    return True

# Функция CRC
# На вход принимает пораждающий полином и сообщение
# На выходе остаток
def CRC(CRC_poly, message, padding):

    # Переводим данные в удобный вид
    CRC_poly = list(CRC_poly)

    # Инициализируем добавку в виде нулей в конец сообщения

    binary_message = text_to_bits(message) + padding
    #binary_message = "1101011011" + padding
    binary_message = list(binary_message)

    # Сдвигаемся, пока есть куда
    while len(binary_message) > len(CRC_poly):

        # Проверка на равенство всех элементов списка нулю
        # Это возможно только при нулевом остатке
        if have_zero_reminder(binary_message):
            print(f"Zero reminder!\nCRC {padding} seems correct!\nExpected message: {message}")
            return ''

        print("Next iteration")

        # Пропускаем незначачащие нули
        for index,bit in enumerate(binary_message):
            if bit == '1':
                binary_message = binary_message[index:]
                break

        print(f"Binary message {binary_message}" )
        print(f"CRC_poly {CRC_poly}")

        # Дополнительная проверка длины после удаления нулей
        if len(binary_message) < len(CRC_poly):
            print("Binary is to small already!")
            return binary_message


        # Ксорим с перезаписью
        for i in range(len(CRC_poly)):
            xored = int(binary_message[i]) ^ int(CRC_poly[i])

            print(binary_message[i],"^", CRC_poly[i],"=",xored)
            binary_message[i] = str(xored)

        print(f"Binary {binary_message}\n")

    return binary_message

if __name__ == "__main__":
    CRC_poly = "10011"
    message  = input("Insert a message to find a CRC summ:\n>")
    padding  = "0"*(len(CRC_poly)-1)

    crc      = CRC(CRC_poly, message, padding)
    crc      = ''.join(str(char) for char in crc)
    print(f"\nCRC for that message: {crc}\n")

    input("Found a CRC. Would you like to check it?")
    check  = CRC(CRC_poly, message, crc)
    print(check)

