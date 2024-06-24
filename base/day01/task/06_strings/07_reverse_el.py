# Считываем строку
s = input()

# Ищем индекс первого и последнего символа 'h'
first_index = s.find('h')
last_index = s.rfind('h')

mirror=s[::-1]
# Развернем последовательность символов между первым и последним появлением буквы 'h'
s = s[:first_index+1]+mirror[len(s)-last_index:len(s)-first_index]+s[last_index+1:]

# Выводим получившуюся строку
print(s)





