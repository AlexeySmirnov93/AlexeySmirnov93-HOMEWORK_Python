# Пользователь вводит число K - количество фруктов. 
# Затем он вводит K фруктов в формате: название фрукта и его количество. 
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение. 

listFruit = {}
amount = int(input("Введите количество позициий: "))
for key in range(amount):
    key = input("Введите назавание: ")
    listFruit[key] = int(input("Введите количество: "))
print(listFruit)
