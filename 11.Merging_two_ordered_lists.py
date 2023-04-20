# Два упорядоченных массива, которые необходимо объединить в один
massiv1 = [1, 4, 10, 11]
massiv2 = [2, 3, 3, 4, 8]

# Массив для результата
res = []

# Кол-во элементов для каждого массива
len_1 = len(massiv1)
len_2 = len(massiv2)

# Указатели для массивов
i = 0
j = 0

# Пока пройдем по одному из списков
while i < len_1 and j < len_2:
    # Если элемент 1 массива меньше второго
    if massiv1[i] <= massiv2[j]:
        # Добавляем его в наш итоговый массив
        res.append(massiv1[i])
        # Смещаем указатель для первого массива
        i += 1

    # Иначе, делаем то же самое с вторым массивом и его счетчиком
    else:
        res.append(massiv2[j])
        j += 1

# Объединяем оставшиеся элементы одного из массивов
res += massiv1[i:] + massiv2[j:]

print(res)
