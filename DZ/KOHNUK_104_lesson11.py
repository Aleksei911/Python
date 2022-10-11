# задание 6

my_string = 'pythonist'
my_dict = {i: my_string.count(i) for i in my_string}

# DZ

products = {
    'aggs': [1.89, 200],
    'milk': [2.99, 100],
    'cheese': [3.49, 170],
    'icecream': [1.95, 90]
}

print('В данный момент, Ваша корзина пуста! Выберите товар для покупки')
print('Для добавления товара в корзину, выберите название продукта и укажите необходимое вам количество')

basket = {}
user_choice_values = ['y', 'p', 'n']
flag = True
while flag:

    print()
    for key, value in products.items():
        print(f'{key} - {value[0]} руб./шт. - {value[1]} шт. на складе')

    user_key = input('Введите название товара из предложенного списка: ')
    if user_key not in products:
        print('Проверьте корректность введенных данных!')
        continue

    user_count = int(input('Введите необходимое Вам количество товара: '))
    if type(user_count) != int or user_count <= 0 or user_count > products[user_key][1]:
        print('Проверьте корректность введенных данных')
        continue

    if user_key not in basket:
        basket[user_key] = [user_count, products[user_key][0] * user_count]
    else:
        basket[user_key] = [basket[user_key][0] + user_count,
                            basket[user_key][1] + products[user_key][0] * user_count]

    print()
    print('На данный момент у Вас в корзине находится:')
    for basket_key, basket_value in basket.items():
        print(f'{basket_key}, в количестве {basket_value[0]} шт. стоимостью {basket_value[1]} рублей')

    user_choice = input('Хотите ещё что-то добавить в корзину? (y - да, p - к оплате, n - выход): ')
    while user_choice not in user_choice_values:
        print('Проверьте корректность введенных данных')
        user_choice = input('Хотите ещё что-то добавить в корзину? (y - да, p - к оплате, n - выход): ')

    if user_choice == 'y':
        products[user_key][1] -= user_count
    elif user_choice == 'p':
        summa = 0
        for value in basket.values():
            summa += value[1]
        print(f'К оплате {summa} рублей.')
        flag = False
    elif user_choice == 'n':
        break

