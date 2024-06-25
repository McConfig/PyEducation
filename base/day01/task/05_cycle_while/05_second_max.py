# Считываем последовательность чисел
numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

# Сортируем последовательность в порядке убывания
numbers.sort()
numbers.reverse()
# Выводим второй по величине элемент
print(numbers[1])

