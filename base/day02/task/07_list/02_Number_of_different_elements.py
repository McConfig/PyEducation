# Считываем список чисел
numbers = list(map(int, input().split()))

# Определяем количество различных элементов
unique_count = len(set(numbers))

# Выводим количество различных элементов
print(unique_count)
