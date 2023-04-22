import collections

q = collections.deque()
print('Пустая очередь', q)

# Добавляем элементы в очередь(в конец очереди)
q.append(1)
q.append(2)
q.append(3)
print(q)

# Удалит первый элемент и вернет его значение
q.popleft()
print(q)

# Можем реализовать и Стек используя pop() и удалим последний элемент
q.pop()
print(q)
