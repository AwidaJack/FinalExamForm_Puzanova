#INTRO TO IT 2nd COURSE
#Задача 10: Вычисление факториала
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)