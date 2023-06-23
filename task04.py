# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284



# def frendly(n,m):
#     num_1=list(range(1,n))
#     divider_1=0
#     for i in range(len(num_1)):
#         if n% num_1[i]==0:
#             divider_1+=num_1[i]

#     num_2=list(range(1,m))
#     divider_2=0
#     for j in range(len(num_2)):
#         if m%num_2[j]==0:
#             divider_2+=num_2[j]
#     if divider_1==m and divider_2==n and n!=m:
#         print(n,m)

# k=int(input('Введите k меньше 100000: '))
# if k > 10**5:
#     print('Вы ввели неверное число')
#     exit()
# k_lst=list(range(1,k+1))

# for i in range(len(k_lst)):
#     for j in range(len(k_lst)):
#         frendly(k_lst[i],k_lst[j])

def frendly(n):
    divider=0
    for i in range(1,n):
        if n%i==0:
            divider+=i
    return divider

k=int(input('Введите k меньше 100000: '))
if k > 10**5:
    print('Вы ввели неверное число')
    exit()

dic = {}
for i in range(1,k+1):
    dic[i] = frendly(i)
for j in dic:
    if j == dic.get(dic.get(j)) and j < dic.get(j):
        print(j, dic.get(j))


