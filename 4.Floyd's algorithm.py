# Алгоритм Флойда предназначен для поиска кратчайшего пути во взвешенном графе
# (работает с положительными и отрицательными графами и находит сразу кратчайшие расстояния между всеми графами)

import math


def get_path(P, u, v):
    # Записываем конечную вершину в путь
    path = [u]
    # Пока не пришли в нужную вершину
    while u != v:
        # Получаем промежуточную вершину
        u = P[u][v]
        # Добавляем промежуточную вершину в путь
        path.append(u)

    return path


# Создаем матрицу смежности
V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
]
# Число вершин в графе
N = len(V)

# Начальный список предыдущих вершин для поиска кратчайших маршрутов
P = [[v for v in range(N)] for u in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            # Если длинна маршрута через дополнительную вершину меньше чем маршрут из матрицы смежности
            if V[i][j] > d:
                # То мы заменяем его новым значением
                V[i][j] = d
                # Записываем через какую вершину(промежуточную) нужно пройти от i до j
                P[i][j] = k

# нумерация вершин начинается с нуля
# Из какой точки выйти
start = 0
# В какую точку прийти
end = 7
print(get_path(P, end, start))
