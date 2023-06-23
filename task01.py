# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


from random import randint
numbers_1 =[]
numbers_2=[]

def numbers(num,n):
    for i in range(n):
        num.append(randint(1, 10))
    print(num)

n=int(input('Введите длину первого списка: '))
m=int(input('Введите длину второго списка: '))
numbers(numbers_1,n)
numbers(numbers_2,m)

# fin_num=[]
# for i in numbers_1:
#     if i not in numbers_2:
#         fin_num.append(i)
# print(fin_num)

print(fin_num := [i for i in numbers_1 if i not in numbers_2])


