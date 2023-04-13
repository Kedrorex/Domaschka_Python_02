# Задача 12: Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.



s = int(input("Введите сумму: "))
p = int(input("Введите произведение: "))
x = y = 0

for i in range(0, s//2):
    if i * (s-i) == p:
        x = i
        y = s-i
        print("x = ", x, "y = ", y)
        break
else:
    print("Искомые счисла не существуют")