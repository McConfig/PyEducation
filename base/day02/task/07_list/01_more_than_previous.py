# Считываем список чисел
numbers = list(map(int, input().split()))

# Выводим элементы списка, которые больше предыдущего элемента
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        print(numbers[i])
