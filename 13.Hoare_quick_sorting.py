import random

massiv = [-4, 2, 7, 0, 1, 10, 3]


# Быстрая сортировка Хоара через рекурсию
def quick_sort(massiv):
    # Если длинна массива больше 1, то можем разбить его на подмассивы
    if len(massiv) > 1:
        # Случайное пороговое значение (для разделения на малые и большие)
        x = massiv[random.randint(0, len(massiv)-1)]
        # Подмассив меньших значений
        low = [u for u in massiv if u < x]
        # Подмассив равных значений
        eq = [u for u in massiv if u == x]
        # Подмассив больших значений
        hi = [u for u in massiv if u > x]
        # Соединяем отсортированные подмассивы
        massiv = quick_sort(low) + eq + quick_sort(hi)

    return massiv


print(quick_sort(massiv))

