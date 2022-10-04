# задание 1

my_list = [i for i in input("Введите строку: ").split()]
my_list.reverse()
print(*my_list)


# задание 2

my_list = [1, 15, 20, 25, 36, 20, 68, 20]
if 20 in my_list:
    my_list[my_list.index(20)] = 200


# задание 3

my_list = [int(input("Введите число: ")) for _ in range(7)]

even = 0
uneven = 0

for i in my_list:
    if i % 2 == 0:
        even += 1
    else:
        uneven += 1

if even > uneven:
    print(sum(my_list))
elif even < uneven:
    print(my_list[0] * my_list[2] * my_list[5])
else:
    print("количество четных и нечетный чисел одинаково")

