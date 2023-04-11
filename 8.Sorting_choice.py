# Массив
massiv = [-3, 5, 0, -8, 1, 10]
# Число элементов в массиве
len_massiv = len(massiv)


for left_pointer in range(len_massiv-1):
    # Минимальное значение
    small = massiv[left_pointer]
    # Индекс минимального значения
    index_small = left_pointer

    # Поиск минимального значения
    for right_pointer in range(left_pointer+1, len_massiv):
        # Если по правому счетчику значение меньше, чем по левому
        if small > massiv[right_pointer]:
            # Меняем минимальное значение
            small = massiv[right_pointer]
            # Меняем индекс минимального значения
            index_small = right_pointer

    # Обмен значениями
    if index_small != left_pointer:
        temp_variable = massiv[left_pointer]
        massiv[left_pointer] = massiv[index_small]
        massiv[index_small] = temp_variable

print(massiv)
