first = int(input('Введите первые числа:'))
second = int(input('Введите вторые числа:'))
third  = int(input('Введите третьи числа:'))

if first == second == third:
    print(3)
elif first == second or first == third or second == first:
    print(2)
else:
    print(0)