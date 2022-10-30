class Car:
    # статические поля (статические переменные класса)
    default_color = 'Grey'
    default_weight = 5000

    def turn_on(self):
        pass

    def ride(self):
        pass


car_object = Car()


# задание 1

class Example:
    first = 2
    second = 4

    def __init__(self, one, two):
        self.one = one
        self.two = two

    def func_one(self):
        a = 56
        print(a)

    def func_two(self):
        return Example.first + Example.second

    def func_three(self):
        return self.one ** self.two


obj = Example(6, 8)

print(obj.func_two())
print(obj.func_three())
obj.func_one()


# задание 2

class Calculator:

    def __init__(self, first, second):
        self.first = int(input('Введите первое число: '))
        self.second = int(input('Введите второе число: '))

    def get_sum(self):
        return self.first + self.second

    def get_difference(self):
        return self.first - self.second

    def get_multi(self):
        return self.first * self.second

    def get_division(self):
        return self.first / self.second


calc = Calculator(8, 2)
print(calc.get_division())
