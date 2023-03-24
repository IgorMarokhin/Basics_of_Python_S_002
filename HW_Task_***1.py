'''
*** (1) У вас есть массив чисел, составьте из них максимальное число.
Например:
[61, 228, 9] -> 961228
'''
# Вариант 1.
import random

a = []
for x in range(random.randint(3, 6)):
    a.append(random.randint(1, 250))
print(a)

s = sorted(map(str, a), reverse=True)
print(s)
n = ''
for i in s:
    n = n + i
print('Максимальное число из списка: ' + n)

# Вариант 2.
join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse=True)))

if __name__ == '__main__':
    print(f'Максимальное число из списка: {join_to_biggest([501, 2, 1, 80, 9])}')