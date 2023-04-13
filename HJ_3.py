# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input("Введите число: "))
power = 2
list_1 = []
index = 1

while power < n:
    list_1.append(power)
    index+=1
    power = 2**index
    
print(list_1)