# Считываем строку
s = input()

# Ищем индекс первого и последнего символа 'h'
first_index = s.find('h')
last_index = s.rfind('h')

# Заменяем все появления буквы 'h' на букву 'H', кроме первого и последнего вхождения
s = s[:first_index] + 'H' + s[first_index+1:last_index] + 'H' + s[last_index+1:]

# Выводим получившуюся строку
print(s)




