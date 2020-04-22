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

        # иначе пишем информационный бит
        else:
            msg.append(information.pop(0))

    print('Избыточное сообщение:',msg)

    print("Powers", two_in_power)
    # performing N throught N counting
    for N in two_in_power:
        print(N)

       # Generate a list of possible multipliers 
       # We can only use even numbers

        # N = 1 acts by it's own
        if N == 1:
            bits = [x for x in range(1, bits_in_msg) if x % 2 == 0] 
            print("Bits", bits)
            continue

        print(bits_in_msg // N )
        multipliers = [ x for x in range(0, bits_in_msg // N  + 1) if x % 2 != 0]
        print("Multipliers", multipliers)

        # generate a list of "NtN" numbers for each N
        bits = [ ( k*N ) - 1 + i for i in range(N) for k in multipliers ]
        bits.sort()
        print("Bits", bits)

if __name__ == "__main__":
    info = '1110000000'
    print("Исходное сообщение:", info)

    HammingEncode(info)
