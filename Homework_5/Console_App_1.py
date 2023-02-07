# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

str1 = input("Введите текст: ")
str2 = input("Введите буквы: ")
str1 = str1.split()
res = []

for item in str1:
    if not str2 in item:
        res.append(item)

res = ' '.join(res)
print("Слова с нежедательными буквами удалены" )
print (res)