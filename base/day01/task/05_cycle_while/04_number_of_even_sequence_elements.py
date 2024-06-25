# Считываем последовательность чисел
numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

# Определяем количество четных элементов
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1

# Выводим количество четных элементов
print(even_count)







