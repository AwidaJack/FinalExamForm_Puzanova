#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers: list):
    
    numbers = list(set(numbers))
    numbers.remove(max(numbers))
    return max(numbers)
    

print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9
