from  math  import log

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

#   N = 2  [ 1*N - 1 + i for i in range(2**(N-1)) ]
#   N = 4  [ 3*N - 1 + i for i in range(2**(N-2)) ]
#   N = 8  [ 3*N - 1 + i for i in range(2**(N-5)) ] 
#   N = 16 [ 1*N - 1 + i for i in range(2**(N-12))]

    # performing N throught N counting
    for N in two_in_power:
        print(N)

        if N == 1:
            print([N - 1, 2*N, 4*N, 6*N, 8*N, 10*N])

        elif N == 2:
            print([ 1*N - 1 + i for i in range(2**(N - log(N, 2))) ])

        elif N == 4:
            print([ 1*N - 1 + i for i in range(2**(N-2)) ])

        elif N == 8:
            print([ 1*N - 1 + i for i in range(2**(N-5)) ] )

        elif N == 16:
            print([ 1*N - 1 + i for i in range(2**(N-12)) ] )

if __name__ == "__main__":
    info = '1101'
    print("Исходное сообщение:", info)

    HammingEncode(info)
