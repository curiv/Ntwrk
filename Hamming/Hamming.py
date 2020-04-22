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
            msg.append(0)

        # иначе пишем информационный бит
        else:
            msg.append(int(information.pop(0)))

    print('Избыточное сообщение:',msg)

    # Запомним содержимое msg, 
    # Чтобы потом учесть чётность/нечетность "N через N"
    encoded_msg = msg

    # Производим расчёт "N через"
    for N in two_in_power:
#        print("Current power", N)

        # Для N=1 свои правила
        if N == 1:
            bits = [x for x in range(0, bits_in_msg) if x % 2 == 0] 

        else:
           # Генерируем список множителей ( число укладываний интервала в отрезок )
           # Используем только нечетные числа
            multipliers = [ x for x in range(0, bits_in_msg // N  + 1) if x % 2 != 0]

            # Генерируем список битов для суммирования
            bits = [ ( k*N ) - 1 + i for i in range(N) for k in multipliers ]

        summ = 0
        for bit in bits:
            # На последней степени двойки  мы можем выйти за границы длины сообщения
            # Поэтому отлавливаем исключение
            try:
                summ += int(msg[bit])
            except IndexError:
                break

        # Прозводим замёну в завимости от чётности суммы бит "N через N"
        if summ  % 2:
            encoded_msg[N-1] = 1
        else:
            encoded_msg[N-1] = 0

    return encoded_msg

if __name__ == "__main__":
    info = '11011'
    print("Исходное сообщение:", info)

    result = HammingEncode(info)
    print("Закодированное сообщение:", result)
