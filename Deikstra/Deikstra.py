def Dijkstra(N, start, matrix, inf):
    valid = [True]*N
    weight = [inf]*N

    # Зануляем расстояние до самого себя
    weight[start] = 0
    # Проходимся по всем узлам
    for _ in range(N):
        min_weight = inf + 1
        # -1 - послений элемент
        ID_min_weight = -1

        for j in range(N):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                ID_min_weight = j

        for z in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                # Увеличиваем длину пути
                weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]

        valid[ID_min_weight] = False

    return weight
     
if __name__ == "__main__":
    # Задаёмся условной бесконечностью
    inf = 777

    # Формируем матрицу весов
    matrix = [
                [inf , 10, 3, inf],
                [10, inf, 4, inf],
                [3, 4, inf, 11],
                [inf, inf, 11, inf],
            ]
    lenght = len(matrix)

    print("Кратчайшее расстояние:\nx0, x1, 2, x3")
    print(Dijkstra(lenght, 3, matrix, inf))
