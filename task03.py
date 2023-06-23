# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

from random import randint
numbers_1 =[]
def numbers(num,n):
    for i in range(n):
        num.append(randint(1, 10))
    print(num)
numbers(numbers_1, 10)

n=0
for i in set(numbers_1):
    n+=numbers_1.count(i)//2
    
print(n)