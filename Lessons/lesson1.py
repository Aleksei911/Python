a = 5                   # переменная типа int
pi = 3.14               # переменная типа float
s = "Helo, world!"      # переменная типа string
t = True                # переменная типа bool

print(a)
print(pi)
print(s)
print(t)
print("передал текст")


num1, num2, str1, fl1 = int(input("Введите целое число: ")), int(input("Введите целое число: ")), \
                        input("Введите целое строку: "), float(input("Введите вещественное число: "))
print(num1, num2, str1, fl1)

a, b, c, d = 1, 1.5, True, "kjsghkjs"
print(str(a), str(b), str(c), str(d))

name = input("Введите Имя: ")
lastname = input("Введите Фамилию: ")
patronymic = input("Введите Отчество: ")
age = input("Введите Возраст: ")
city = input("Введите Город проживания: ")
print(lastname, name, patronymic)
print(age)
print(city)
