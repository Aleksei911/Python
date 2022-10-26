import json

# задача 1
groceries = []
while True:
    name = input('Введите название продукта: ')
    if name == 'стоп':
        break
    price = input('Введите стоимость покупки: ')
    if price == 'стоп':
        break
    groceries.append({
        'название': name,
        'стоимость': price
    })

with open('task1.json', 'w', encoding='UTF-8') as file:
    json.dump(groceries, file, ensure_ascii=False)


# задача 2

total = 0
with open('task1.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)
    for elem in data:
        total += int(elem['стоимость'])
print(total)
