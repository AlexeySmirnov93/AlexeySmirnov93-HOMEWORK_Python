# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

friends = {}
lenght = int(input('Введите кол-во друзей: '))
for name in range(lenght):
    name = input('Введите имя друга: ')
    friends[name] = int(input('Введите возраст друга: '))

print(min(friends, key=friends.get))

             
