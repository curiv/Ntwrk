def CRC(data):

    # initialize reminder
    crc = 0xFFFF

    # go throught the all characters
    for i in range(0, len(data)):
        crc ^= data[i] << 8

        for j in range(0,8):
        #    print(crc, crc & 0x8000)
            if (crc & 0x8000) > 0:
                crc =(crc << 1) ^ 0x1021
            else:
                crc <<=  1

    # used to get last two bytes
    return hex(crc & 0xFFFF)

M = '123456789'

# encode message and translate it to the decimal array
M = bytearray(M.encode())

# get the reminder from CRC
rem = CRC(M)
print("\nReminder:", rem)
