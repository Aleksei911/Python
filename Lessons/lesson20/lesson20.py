types_list = [
    1,  # integer
    'строка',  # string
    [1, 2, 3],  # list
    {1, 2, 3},  # set
    1.1,  # float
    True,  # bool
    (1, 2, 3),  # tuple
    frozenset({1, 2, 3}),  # frozenset
    {'key': 'value'},  # dict
    range(1, 10)  # range
]

for _ in types_list:
    print(f"Тип данных: {type(_)}, "
          f"наличие iter: {'__iter__' in _.__dir__()}, "
          f"наличие getitem: {'__getitem__' in _.__dir__()}")
