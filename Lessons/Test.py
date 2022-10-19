from functools import reduce


def evaluate(coefficients, x):
    total1 = [x ** i for i in range(len(coefficients))[::-1]]
    total2 = list(map(lambda a, b: a * b, coefficients, total1))
    print(reduce(lambda a, b: a + b, total2))


evaluate([int(i) for i in input().split()], int(input()))
