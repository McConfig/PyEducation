# Считываем строку
s = input()

# Ищем индекс первой и последней буквы f
first_index = s.find('f')
last_index = s.rfind('f')

# Выводим индексы
if first_index != -1:
    if first_index == last_index:
        print(first_index)
    else:
        if first_index != -1:
            print(first_index)
        if last_index != -1:
            print(last_index)





