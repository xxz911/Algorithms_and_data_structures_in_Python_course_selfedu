# Массив
massiv = [2, 0, -3, 10, 3]
# Число элементов в массиве
len_list = len(massiv)

# Указываем количество итераций(число элементов массива -1,
# так как последний элемент на последней итерации будет уже отсортирован)
for i in range(len_list-1):
    # Проходим по оставшимся неотсортированным парам массива
    for j in range(0, len_list-1-i):
        # Если левый элемент массива меньше правого, меняем их местами
        if massiv[j] > massiv[j+1]:
            massiv[j+1], massiv[j] = massiv[j], massiv[j+1]

print(massiv)