'''
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть
'''
import random

n = int(input("Введите количество монет: "))

def avers_revers(n):
    money = []
    for _ in range(n):
        m = (random.randint(0, 1))
        money.append(m)
    print(money)
    count1 = 0
    for i in money:
        if money[i] == 0:
            count1 += 1
    count2 = 0
    for i in money:
        if money[i] == 1:
            count2 += 1
    if count1 < count2:
        print(count1)
    else:
        print(count2)

avers_revers(n)