# Считываем последовательность чисел
numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

# Вычисляем среднее значение последовательности
average = sum(numbers) / len(numbers)

# Выводим среднее значение
print(average)
