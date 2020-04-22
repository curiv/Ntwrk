# функция кодирования по Хэммингу
# На вход принимает битовую последовательность в виде строки
# на выходе закодированное сообщение
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
    global two_in_power
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

        # Для N=1 свои правила
        if N == 1:
            bits = [x for x in range(0, bits_in_msg) if x % 2 == 0]

        else:
           # Генерируем список множителей ( число укладываний интервала в отрезок )
           # Используем только нечетные числа
            multipliers = [ x for x in range(0, bits_in_msg // N  + 1) if x % 2 != 0]

            # Генерируем список битов для суммирования
            bits = [ ( k*N ) - 1 + i for i in range(N) for k in multipliers ]

            # Очень важно сохранять порядок
            # Это спасёт нас от пропуска младших бит
            bits.sort()

        summ = 0
        for bit in bits:
            # На последней степени двойки  мы можем выйти за границы длины сообщения
            # Поэтому отлавливаем исключение
            try:
                # Суммируем биты по определённым ранее позициям
                summ += msg[bit]
            except IndexError:
                break

        # Прозводим замёну в завимости от чётности суммы бит "N через N"
        if summ  % 2:
            encoded_msg[N-1] = 1
        else:
            encoded_msg[N-1] = 0

    return encoded_msg

# Функция декодирования полученного сообщения 
# На вход принимает сообщение с помехой
# На выходе корректируется ошибка и возвращается исходное сообщение
def HammingDecode(stored, recieved):

    print(stored, " - без ошибки")
    print(recieved, " - с ошибкой")

    error_index = 0
    for bit_number in  range(len(stored)):
        if stored[bit_number] != recieved[bit_number]:
            error_index += bit_number

    if not error_index:
        print("Ошибок при передаче нет!", end="\n\n")
    else:
        print(f"Ошибка в бите {error_index}!\n")
        stored[error_index] = recieved[error_index] ^ 1

    msg = []
    for i in range(len(stored)):
        if i+1 not in two_in_power:
            msg.append(stored[i])
    return msg

if __name__ == "__main__":
    sent  = '10111101'
    sent_encoded  = HammingEncode(sent)
    print("Исходное сообщение:", sent)
    print("Закодированное сообщение:", sent_encoded, end="\n\n")

    recieved = '10111101'
    recieved_encoded = HammingEncode(recieved)
    print("Сообщение с ошибкой:", recieved)
    print("Закодированное сообщение с ошибкой", recieved_encoded, end="\n\n")

    initial_message = HammingDecode(sent_encoded, recieved_encoded)
    print("Исходное сообщение:", ''.join(str(bit) for bit in initial_message))
