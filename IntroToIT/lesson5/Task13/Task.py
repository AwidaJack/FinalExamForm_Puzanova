#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def wrong_is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return True
    return False

print (wrong_is_sorted([1, 2, 3, 4]))