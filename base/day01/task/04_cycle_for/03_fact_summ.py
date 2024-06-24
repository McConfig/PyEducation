# Считываем число n
n = int(input())

# Вычисляем сумму факториалов чисел от 1 до n
total_sum = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total_sum += factorial

# Выводим сумму факториалов чисел от 1 до n
print(total_sum)
