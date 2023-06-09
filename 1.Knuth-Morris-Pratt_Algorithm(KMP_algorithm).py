# Тема сложная, лучше читать с видео

# Нам надо найти фрагмент строки в другой строке
# Самое первое, что приходит на ум, это проверять фрагмент в начале строки, если не совпадает,
# то передвигать на одну позицию вправо.
# Такой алгоритм называется ПРЯМЫМ ПОИСКОМ и занимает O(n * m), где т-длинна массива, m - длинна фрагмента
# Такой алгоритм относительно долгий

# При Алгоритме КМП O(n + m) мы сдвигаем фрагмент по массиву не полностью, а по максимальному префиксу
# Этапы алгоритма КМП:
# 1. Формирование массива ПИ
# (хранятся максимальная совпадающая длинна суффикса, относительно i-го элемента образа)
# (для сдвига по префиксам)
# (в 0 индексе всегда 0)
# 2. Поиск образа в строке

# Если у нас фрагмент состоит только из 2 символов(например 'ли'),
# то может быть только один префикс 'л' и один суффикс 'и'
# Если у нас фрагмент состоит только из 3 символов(например 'лил'),
# то может быть 2 префикса и три суффикса
# Если у нас фрагмент состоит только из 4 символов(например 'лили'),
# то может быть 3 префикс и 6 суффикса

t = "лилила"

# 1. Формирование массива ПИ
# Формируем массив п
p = [0] * len(t)
# 2 счетчика
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

# Выводим для себя сформированный массив п
print(p)

# 2. Поиск образа в строке
# Наш массив в котором происходит поиск
a = 'лилилось лилилась'
# Длинна подстроки
m = len(t)
# Длинна массива в котором происходит поиск
n = len(a)

# Счетчики
i = 0
j = 0

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Образ найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1
if i == n:
    print("Образ не найден")


