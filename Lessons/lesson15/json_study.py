import json

# string = '{"id":765,"email":"ivanov@mail.ru","surname":"Иванов","age":45,"admin":false,"friends":[123,456,789]}'
# data = json.loads(string)
# print(data['email'])
# print(data['surname'])
# print(data['admin'])
# print(data['friends'])
#
#
# ########################################################
#
#
# with open('data.json', encoding='UTF-8') as file:
#     data = json.load(file)
# print(data['email'])
# print(data['surname'])
# print(data['admin'])
# print(data['friends'])
#
#
# ########################################################
#
#
# data = {"id": 765,
#         "email": "ivanov@mail.ru",
#         "surname": "Иванов",
#         "age": 45,
#         "admin": False,
#         "friends": [123, 456, 789]}
#
# # преобразуем словарь в json строку
# string = json.dumps(data)
# print(string)
#
# # преобразуем словарь в json строку с отображением русских символов
# string = json.dumps(data, ensure_ascii=False)
# print(string)
#
# ########################################################


data = {"id": 765,
        "email": "ivanov@mail.ru",
        "surname": "Иванов",
        "age": 45,
        "admin": False,
        "friends": [123, 456, 789]}

# преобразуем словарь в json и записываем в файл
with open('data1.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, indent=4)

# преобразуем словарь в json и записываем в файл
with open('data2.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
