# Считываем список чисел
numbers = list(map(int, input().split()))

# Находим индексы минимального и максимального элементов
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Меняем местами минимальный и максимальный элемент
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Выводим измененный список
print(numbers)
