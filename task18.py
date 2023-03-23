# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


n = int(input("Введите количество элементов:  "))
list_1 = [i for i in range(n)]
print(list_1)
x = int(input("Введите число:  "))
min_elem = list_1[0]
min_diff = abs(list_1[0]-x)
for digit in list_1[1:]: 
    diff = abs(digit - x) 
    if diff < min_diff and digit != x:
        min_diff = diff
        min_elem = digit
print(min_elem)


    