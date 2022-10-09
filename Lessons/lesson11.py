dict1 = {}
dict2 = dict([(1, "a"), (2, "b")])
dict3 = dict.fromkeys([3, 4], 300)
dict4 = dict(a=2, b=3)

Salary = {'Director': '120800.0',
          'Secretary': '101150.25',
          'Locksmith': '188200.00'}

print(Salary)

key = "Secretary"
if key in Salary:
    del Salary["Secretary"]
    print(Salary)

key2 = 5
if key2 in Salary:
    del Salary[key2]

# задание 1

person = {"name": "Vasya",
          "age": 999,
          "city": "LA"}
print(f"age = {person['age']}")

# задание 2

cars = {"BMW": ["a", "b", "c"],
        "Tesla": ["d", "e", "f"]}

print(cars['BMW'][0], cars['BMW'][-1])
print(cars['Tesla'][0], cars['Tesla'][-1])

# задание 3

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "c": 400}

print(d1['b'] == d2['b'])

# задание 4

Salary = {'Director': 120800,
          'Secretary': 101150,
          'Locksmith': 188200}

multi = 1

for value in Salary.values():
    multi *= value

print(multi)

# задание 5

list1 = [1, 2, 3, 4, 5]
list2 = ["one", "two", "three", "four", "five"]

my_dict = dict(zip(list1, list2))

