
def Deikstra(matrix):
    inf = 7777
    # Относительно какого узла считаем
    start_node = 0

    # Инициализируем метки бесконечностью
    marks = [9999 for _ in range(len(matrix))]

    # Инициализируем начальный узер нулевой меткой
    W = 0
    marks[start_node] = W

    print(marks)

    # Инициализируем список возможных путей    
    possible_nodes = []

    # Рассматриваем пути из ноды с индексом start_node
    initial_node  = matrix[start_node]

    # Находим минимальную длину пути
    shortest_path = min(initial_node)

    # Находим индексы узлов с одинаковой стоимостью пути
    dummy_node = initial_node
    for  i in range(len(initial_node)):
        try:
            shortest_node_index = dummy_node.index(shortest_path)
            dummy_node[shortest_node_index] = 0
            possible_nodes.append(shortest_node_index)
        except ValueError:
            break

    if len(possible_nodes) > 1:
        print(f"Существует {len(possible_nodes)} узла ({possible_nodes}) с минимальной целой перемещения {shortest_path} ")

    print(matrix[3])
    # Проходим по доступным узлам
    print(matrix)
    for node in possible_nodes:
        print(node)
        if matrix[node - 1].count(inf) == 4:
            print(f"{node} узел - тупик! ")

if __name__ == "__main__":
    inf =  7777 
    matrix = [[inf, 10, 30, 50, 10], [inf, inf, inf, inf], [inf,inf,inf,inf,10], [10, inf, 10, 30, inf]]
    print(matrix)

    Deikstra(matrix)
