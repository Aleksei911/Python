from random import *


# задание 1

def give_sum(my_list):
    print(sum(my_list))


# задание 2
def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(2020))
