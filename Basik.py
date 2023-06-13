'''"""Вывессти числа от 0 до 10"""
for i in range(0, 11):
    print(i)
"""Вывести числа от 0 до И, где И это случайное число, введеное с клавиатуры"""
x = int(input('x = '))
for i in range(0, x):
    print(i)
"""Вывести нечетные числа в диапазоне от 0 до И"""
x = int(input('x = '))
for i in range(0, x):
    if i % 2 != 0:
        print(i)
"""Вывести четные числа из диапозона от 0 до И"""
x = int(input('x = '))
for i in range(0, x):
    if i % 2 == 0:
        print(i)
"""Вывести числа, делящиеся на три без остатка, в диапозоне от 0 до И"""
x = int(input('x = '))
for i in range(0, x):
    if i % 3 == 0:
        print(i)'''
"""Вывести числа, делящиеся на три или на семь без осткатка от 0 до И"""
'''x = int(input('x = '))
for i in range(0, x):
    if (i % 3 == 0) or (i % 7 == 0):
        print(i)
'''"""Найти сумму всех чисел от 1 до И"""'''
x = int(input('x = '))
summ = 0
for i in range(1, x):
    summ += i
    print(summ)'''
'''"""Найти сумму четных чисел вдиапозане от 0 до И"""
x = int(input('x = '))
summa = 0
for i in range(0, x):
    if i % 2 == 0:
        summa += i
        print(summa)
'''
'''"""Даны два числа а и b а < b. Найти сумму всех целых чисел от а до b включительно """
a = int(input('a = '))
b = int(input('b = '))
summa = 0
for i in range(a, b+1):
    summa += i
    print(summa)'''
'''"""Найти сумму чисел от 1 до И, делящихся на 3 """
x = int(input('x = '))
summa = 0
for i in range(1, x):
    if i % 3 == 0:
        summa += i
        print(summa)'''
''' Какая-то параша с дробями кефтеме того сиську царапал 
x = int(input('x = '))
s = float(0)
a = float
for i in range(1, x + 1):
    a = 1 / i
    s += a
    i += 1
    print(s)
        '''
'''n = int(input())
s = 1
p = 1
for i in range(n+1):
    p = 2 * p
    s = s + p
    print(s)'''

"""a = int(input('a = '))
x = int(input('x = '))
b = int(input('b = '))
if a + x == b or x + b == a or b + a == x:
    print("Yes")"""
'''a = []
for i in range(54, 9184):
    if i % 5 == 0:
        a.append(i)
        print(a)'''
"""proiz = 1
for i in range(0, 30):
    if i % 2 != 0:
        proiz *= i
print(proiz)
"""
'''a = int(input('a = '))
x = int(input('x = '))
b = int(input('b = '))
print((a > 0) + (x > 0) + (b > 0))
'''




####  Цикл While
""" дано положительное число И. Вывести все числа от 0 до И с помощью цикла while."""
'''x = int(input('x = '))
i = 0
while i < x:
  i += 1
  print(i)
'''
""" Дано положительное число И. Вывести все числа от И до 0 с помощью цикла while"""
'''x = int(input('x = '))
i = 0
while i < x:
    x -= 1
    print(x)'''
""" Даны два положительных числа ф и а (ф < a). Вывести все числа от ф до а """
'''x = 1
a = 5
while x < a:
    x += 1
    print(x)'''
"""Даны два положительных числа ф и а (ф < a). На отрезке длины ф размещено максимальное кол-во отрезков  а. 
 Найти длину не занятой части отрезка"""
'''x = 4
a = 6
while a > x:
    f = a % x
    print(f)
    break'''
'''x = 4
a = 6
while a > x:
    f = a // x
    print(f)
    break'''
'''x = int(input('x = '))
i = 0
summa = 0
while i < x:
    i += 1
    if i % 2 == 0:
        summa += i
        print(summa)'''

'''x = int(input('x = '))
i = 0
summa = 0
while i < x:
    i += 1
    if i % 2 != 0:
        summa += i
        print(summa)'''

'''x = int(input('x = '))
i = 1
fact = 1
while i < x:
    i += 1
    fact *= i
    print(fact)'''


"""x = int(input('x = 9'))
a = 1
while True:
    if x % a**3 == 0:
        print('yes')
    elif x % a**3 != 0:
        print('no')
        break"""



