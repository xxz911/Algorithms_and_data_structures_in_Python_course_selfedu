# Тема сложная, лучше читать с видео
# Алгоритм Форда-Фалкерсона позволяет определить максимальную пропускную способность потоков в направленном графе

# Правило: если в рассматриваемом ненасыщенном маршруте встречается противоположная по направлению дуга,
# то величину ее потока уменьшаем. Для остальных дуг - значение увеличиваем

# Шаг 1. Выбираем вершину-исток(начальная точка) как текущую (k = 1)
# Шаг 2. Формируем множество вершин, с которыми имеются положительные остаточные веса дуг.
# Если множество пустое, то переходим к 4 шагу
# Шаг 3. Во множестве S находим вершину, к которой идет дуга с наибольшим остаточным весом.
# Формируем для нее метку в формате, где - значение остаточного потока к этой вершине от рассматриваемой K-й вершины.
# Выбираем найденную вершину как текущую
# Если она не является стоком, то переходим к шагу 2.
# Если она является конечной (стоком), то переходим к шагу 5
# Шаг 4(откат назад). Если k=1, то исток не связан со стоком и движение потока невозможно (переход на шаг 6).
# Если K > 1, то переходим к предыдущему узлу i формируемого маршрута и удалям узел i, из смежных узлов с узлом k.
# Приравниваем k = i и переходим к шагу 2
# Шаг 5. Для найденного маршрута выполняем пересчет остаточных величин потоков.
# Убираем все метки у вершин, кроме истока возвращаемся к шагу 1.
# Шаг 6. Вычисляем значение максимального потока как сумму загрузки дуг, исходящих из потока


import math


def get_max_vertex(k, V, S):
    # наименьшее допустимое значение
    m = 0
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue

        # Движение по стрелке
        if w[2] == 1:
            if m < w[0]:
                m = w[0]
                v = i
        # Движение против стрелки
        else:
            if m < w[1]:
                m = w[1]
                v = i

    return v


def get_max_flow(T):
    w = [x[0] for x in T]
    return min(*w)


def updateV(V, T, f):
    for t in T:
        # Это исток
        if t[1] == -1:
            continue

        # Направление движения
        sgn = V[t[2]][t[1]][2]

        # Меняем веса в таблице для (i,j) и (j,i)
        V[t[1]][t[2]][0] -= f * sgn
        V[t[1]][t[2]][1] += f * sgn

        V[t[2]][t[1]][0] -= f * sgn
        V[t[2]][t[1]][1] += f * sgn


# Конфигурация графа
V = [[[0,0,1], [20,0,1], [30,0,1], [10,0,1], [0,0,1]],
     [[20,0,-1], [0,0,1], [40,0,1], [0,0,1], [30,0,1]],
     [[30,0,-1], [40,0,-1], [0,0,1], [10,0,1], [20,0,1]],
     [[10,0,-1], [0,0,1], [10,0,-1], [0,0,1], [20,0,1]],
     [[0,0,1], [30,0,-1], [20,0,-1], [20,0,-1], [0,0,1]],
]
# Число вершин в графе
N = len(V)
# Вершина истока (нумерация с нуля)
init = 0
# Вершина стока
end = 4
# Первая метка маршрута (a, from, vertex)
Tinit = (math.inf, -1, init)
# Максимальные потоки найденных маршрутов
f = []

# Счётчик есть ли вершины относительно истока
j = init
while j != -1:
    # Стартовая вершина (нумерация с нуля)
    k = init
    # Метки маршрута
    T = [Tinit]
    # Множество просмотренных вершин
    S = {init}

    # Пока не дошли до стока
    while k != end:
        # Выбираем вершину с наибольшей пропускной способностью
        j = get_max_vertex(k, V, S)
        # Если следующих вершин нет
        if j == -1:
            # И мы на истоке, то
            if k == init:
                # Завершаем поиск маршрутов
                break
            # Иначе, переходим к предыдущей вершине
            else:
                k = T.pop()[2]
                continue

        # Определяем текущий поток
        c = V[k][j][0] if V[k][j][2] == 1 else V[k][j][1]
        # Добавляем метку маршрута
        T.append((c, j, k))
        # Запоминаем вершину как просмотренную
        S.add(j)

        # Если дошли до стока
        if j == end:
            # Находим максимальную пропускную способность маршрута
            f.append(get_max_flow(T))
            # Обновляем веса дуг
            updateV(V, T, f[-1])
            break

        k = j

F = sum(f)
print(f"Максимальный поток равен: {F}")