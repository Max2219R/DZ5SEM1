# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def recsum(a, b):
    if b == 0:
        return a
    return 1 + recsum(a, b - 1)

print(recsum(2, 2))