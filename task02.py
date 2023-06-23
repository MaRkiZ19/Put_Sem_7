# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

from random import randint
numbers_1 =[]

def numbers(num,n):
    for i in range(n):
        num.append(randint(1, 10))
    print(num)

n=int(input('Введите длину списка: '))
numbers(numbers_1,n)

elements=0
for i in range(1,len(numbers_1)-1):
    if numbers_1[i]>numbers_1[i-1] and numbers_1[i]>numbers_1[i+1]:
        elements+=1

print(elements)
