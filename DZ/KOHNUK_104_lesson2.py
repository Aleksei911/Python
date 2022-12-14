# задача №1

"""
создаем 2 переменные ann_apple и pol_apple, которые ссылаются (через id) на объекты в памяти компьютера (объект - 2
и объект - 5) равные количеству яблок у Анны и Пола соответственно.
"""
ann_apple, pol_apple = 2, 5
"""
выводим в консоль количество яблок у Анны и Пола (на отдельных строках) использовав одну функцию print()
"""
print("У Пола", pol_apple, "яблок(а). \nУ Анны", ann_apple, "яблок(а).")

# задача №2

"""
1. создаем переменную rib
2. отправляем в консоль запрос на введение инвормации с клавиатуры (длина ребра куба)
3. считываем строку текста (длина ребра куба в виде строки) и помещаем её в память компьютера (выделяется ячейка памяти)
4. приводим считанную строку к целочисленному типу данных (выделяется отдельная ячейка памяти, куда помещается значение
   длинны ребра куба в виде целого числа)
5. переменная rib ссылается (через id) на ячейку памяти, содержащую целочисленное значение длины ребра куба
"""
rib = int(input("Введите длину ребра куба: "))
"""
находим объем и площадь боковой поверхности куба и выводим их в консоль при помощи функции print(), каждое
значение на отдельной строке
"""
print("Объем куба:", rib ** 3, "\nПлощадь боковой поверхности куба:", 6 * rib ** 2)

# задача №3

# создаем переменную step_day которая ссылется на ячейку памяти, хранящую значение объекта 2 (шаг улитки днем)
step_day = 2
# создаем переменную step_night которая ссылется на ячейку памяти, хранящую значение объекта -1 (шаг улитки ночью)
step_night = -1
# создаем переменную length_tree которая ссылется на ячейку памяти, хранящую значение объекта 20 (длина дерева)
length_tree = 20
"""
улитка должна проползти 20 метров за n дней, поднимаясь на 2 метра в день, и опускаясь на 1 метр ночью.
исходя из этого можно составить уравнение length_tree = n * (step_day + step_night)
отсюда n = length_tree / (step_day + step_night)
но когда улитка доберется до отметки 20 метров, опускаться на 1 метр ночью она уже не будет! и этот момент нужно 
в формуле компенсировать! (тоесть отнять 1 этот ночной шаг). тогда получится что
n = length_tree / (step_day + step_night) - 1
"""
# создаем переменную days которая будет ссылаться на ячейку памяти, хранящую значение после
# вычисления выражения length_tree / (step_day + step_night) - 1 (или количество полных дней)
days = int(length_tree / (step_day + step_night) - 1)
print("Улитка заползет на дерево высотой", length_tree, "метров за", days, "дней.")  # выводим результат в консоль

# творческое задание

"""
на вход программе подаётся положительное трёхзначное число. программа должна вывести True, если данное число состоит 
из цифр отличных от нуля, или False в противном случае
"""
num = int(input())  # считываем число с клавиатуры и приводим к целому числу

num1 = num // 100  # находим первую цифру (количество сотен)
num2 = num // 10 % 10  # находим вторую цифру (количество десятков)
num3 = num % 10  # находим первую цифру (количество единиц)

"""
приводим к булеву значению результат произведения цифр нашего числа и выводим на экран. 
если в числе есть 0, то и произведение цифр этого числа будет равно нулю, а 0 = False
если сдеди цифр нуля нет, то значение произведения будет отлично от нуля, а всё что не 0 == True
PS: быстрее чем проверять каждое число по отдельности
"""
print(bool(num1 * num2 * num3))
