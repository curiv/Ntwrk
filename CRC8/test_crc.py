def CRC(M):
    # encode message and translate it to the decimal array
    data = bytearray(M.encode())

    # initialize reminder
    crc = 0xFFFF

    # set a poly
    poly = 0x1021

    print("Initial CRC:", hex(crc))
    print("Poly:", hex(poly))
    print("Message:", M)
    print("Data: ", end='')

    # iterate throught the all characters
    for i in range(0, len(data)):
        print(data[i], end=' ')
        crc ^= data[i] << 8

        for j in range(0,8):
            if (crc & 0x8000) > 0:
                crc = (crc << 1) ^ poly
            else:
                crc = crc << 1

    # used to get last two bytes
    return hex(crc & 0xFFFF )

M = '123456789'

rem = CRC(M)
print("\nReminder:", rem)
