string = '(2+5)*([10+4]-7)'
stack = []
# Прошла ли проверка
flVerify = True

for lt in string:
    if lt in "([{":
        stack.append(lt)
    elif lt in ")]}":
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        flVerify = False
        break

# Стек по итогу должен быть пустым
if flVerify and len(stack) == 0:
    print("Ok")
else:
    print("Except")
