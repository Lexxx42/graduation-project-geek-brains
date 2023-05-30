# Соединить две строки разнимы методами

a = 'hello '

b = 'world!'

print(a + b)

print(f'{a}{b}')

print(''.join((a, b)))

print(s := (a + b))

c = ''
print(c.__add__(a).__add__(b))


a += b
print(a)
