# Задание "Слишком древний шифр":

# Ввод числа n
n = int(input('Введите число: '))
result = ""
used_numbers = set()

# Основной цикл для перебора всех пар чисел от 1 до 20
for i in range(1, 21):
    if i not in used_numbers:
        for j in range(i + 1, 21):
            if j not in used_numbers and n % (i + j) == 0:
                result += str(i) + str(j)
                used_numbers.add(i)
                used_numbers.add(j)
                break  # Прерывание внутреннего цикла, так как пара для i найдена

if result == "":
    print("Пароль не найден!")
else:
    print(result)