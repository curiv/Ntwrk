
def HammingEncode(information):
    # information - должно быть в бинарном виде

    # Количество информационных битов
    information = list(information)
    m = len(information)

    # Расчёт битов избыточности
    k = 0
    while 2**k < m + k + 1:
        k += 1
    print('Количество битов избыточности:', k)

    # создаём список необходимых степеней двойки
    two_in_power = [ 2**i for i in range(k) ]

    bits_in_msg = m + k
    print('Суммарное количество  бит в избыточном сообщении:',bits_in_msg)

    # инициализируем выходную строку
    msg = []

    # двигаемся по элементам строки
    for i in range(bits_in_msg):

        # Если позиция бита является степенью двойки, то записываем бит чётности
        if i+1 in two_in_power:
            msg.append('0')
        else:
            # иначе пишем информационный бит
            msg.append(information.pop(0))

    print('Избыточное сообщение:',msg)
    
    # performing N throught N counting

    N = 2
    pos = N - 1
    while True:
        try:
            msg[pos]
            print(pos)
            pos += 2*N
        except IndexError:
            break

    #for pos in (0,2,4,6):
        #counter += int(msg[pos])
    #print("Not Even" if counter % 2 else "Even")

if __name__ == "__main__":
    info = '1101'
    print("Исходное сообщение:", info)

    HammingEncode(info)
