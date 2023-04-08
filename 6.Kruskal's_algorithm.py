# Алгоритм Краскала служит для поиска минимального острова взвешенного неориентированного графа
# Остров - подграф исходного графа, который состоит из всех вершин графа соединенного ребрами(ребра без циклов)

# 1. Отсортировать ребра по возрастанию
# 2. рассматриваем изолированные вершины графа и соединянием весами (только для изолированных вершин)
# После образования групп вершин соединяем их следующей минимальной вершине

# Список ребер графа (длина, вершина 1, вершина 2)
R = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

# Сортируем ребра
Rs = sorted(R, key=lambda x: x[0])
# Список соединенных вершин
U = set()
# Словарь списка изолированных групп вершин
D = {}
# Список ребер остова
T = []

# Первый этап(соединяем ребра разных групп)
for r in Rs:
    # Проверка для исключения циклов в остове
    if r[1] not in U or r[2] not in U:
        # Если обе вершины не соединены, то
        if r[1] not in U and r[2] not in U:
            # Формируем в словаре ключ с номерами вершин
            D[r[1]] = [r[1], r[2]]
            # И связываем их с одним и тем же списком вершин
            D[r[2]] = D[r[1]]
        # Иначе
        else:
            # Если в словаре нет первой вершины, то
            if not D.get(r[1]):
                # Добавляем в список первую вершину
                D[r[2]].append(r[1])
                # И добавляем ключ с номером первой вершины
                D[r[1]] = D[r[2]]
            else:
                # Иначе, все то же самое делаем со второй вершиной
                D[r[1]].append(r[2])
                D[r[2]] = D[r[1]]

        # Добавляем ребро в остов
        T.append(r)
        # Добавляем вершины в множество U
        U.add(r[1])
        U.add(r[2])

# Второй этап(соединяем вершины разных групп вершин)
# Проходим по ребрам второй раз и объединяем разрозненные группы вершин
for r in Rs:
    # Если вершины принадлежат разным группам, то объединяем
    if r[2] not in D[r[1]]:
        T.append(r)
        # Добавляем ребро в остов
        gr1 = D[r[1]]
        # Объединим списки двух групп вершин
        D[r[1]] += D[r[2]]
        D[r[2]] += gr1

print(T)
