# Вывести все уникальные значения из списка

a = [1, 1, 1, 2, 3, 1, 2, 3, 4, 5, 6, 0]

print(list(set(a)))

unique = list(dict.fromkeys(a))

print(unique)
