# задание 1

name = input("Введите ваше имя: ")
print("Привет,", name)
print(name * 3)


# задание 2

num = input("Введите 3-х значное число: ")
print(f"Сумма цифр числа {num} равна:", int(num[0]) + int(num[1]) + int(num[2]))


# задание 3

s = input("Введите строку: ")
print(s[::3])
print(s[0] + s[-1])
print(s.upper())
print(s[::-1])
print(s.isdigit())


# задание 4

string_ = "".join(input("Введите строку: ").split())
print(string_ == string_[::-1])
