# задание 1

text = input("Введите строку: ")
cr = input("Введите букву: ")
new_text = ""

for c in text:
    if c != cr:
        new_text += c

print(new_text)

# задание 2

start = int(input("Введите начало последовательности: "))
end_ = int(input("Введите конец последовательности: "))
step = int(input("Введите шаг последовательности: "))

for i in range(start, end_, step):
    print(i, end=" ")

# задание 3

for i in range(54, 9184):
    if i % 5 == 0:
        print(i)

# задание 4

food = ["борщ", "сало", "кекс", "горох"]
not_eat = "горох"
for elem in food:
    if elem == not_eat:
        print(f"Я не ем {not_eat}")
        break

# задание 5

numbers = list(range(1, 50))
summa = 0
multi = 1
for num in numbers:
    summa += num
    multi *= num
print(summa)
print(multi)
