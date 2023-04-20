# Функция слияния двух отсортированных списков
def merge_list(massiv1, massiv2):
    # Массив для результата
    res = []

    # Кол-во элементов для каждого массива
    len_1 = len(massiv1)
    len_2 = len(massiv2)

    # Указатели для массивов
    i = 0
    j = 0

    # Пока не пройдем по одному из списков
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

    return res


# Функция деления списка и слияния списков в общий отсортированный список
def split_and_merge_list(massiv):
    # Получаем примерную середину списка
    N1 = len(massiv) // 2
    # Делим список на два примерно на равные части
    list1 = massiv[:N1]
    list2 = massiv[N1:]

    # Если длинна 1-го списка больше одного, то делим дальше
    if len(list1) > 1:
        list1 = split_and_merge_list(list1)

    # Если длинна 2-го списка больше одного, то делим дальше
    if len(list2) > 1:
        list2 = split_and_merge_list(list2)

    # Объединяем два отсортированных списка в один
    return merge_list(list1, list2)


# Неотсортированный массив
massiv = [9, 5, -3, 4, 7, 8, -8]

massiv = split_and_merge_list(massiv)

print(massiv)
