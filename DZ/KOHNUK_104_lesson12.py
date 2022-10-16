import string


# задание 4

def seconds_in_time(sec: int) -> None:
    days = sec // 86400
    hours = (sec % 86400) // 3600
    minutes = ((sec % 86400) % 3600) // 60
    seconds = (sec % 86400) % 60
    print(f"{sec} seconds = {days} days {hours} hours {minutes} minutes {seconds} seconds")


seconds_in_time(100000000)


# задание 5

def count_letters(some_string: str) -> dict:
    total = {}
    for letter in some_string.lower():
        if letter in "euioay":
            total.setdefault("vowels", []).append(letter)
        elif letter in "qwrtpsdfghjklzxcvbnm":
            total.setdefault("consonants", []).append(letter)

    return {"vowels": len(total["vowels"]), "consonants": len(total["consonants"])}


print(count_letters(input("Please, enter the Text: ")))


# задание 6

def sum_of_numbers(num: int) -> int:
    return num + int(str(num) * 2) + int(str(num) * 3)


print(sum_of_numbers(int(input("Please, enter your number: "))))


# задание 6-1

def search_y(x: int) -> int:
    if -5 <= x <= 5:
        return x ** 2
    elif x < -5:
        return 2 * abs(x) - 1
    elif x > 5:
        return 2 * x


print(search_y(int(input("Please, enter your number from -10 to 10: "))))


# DZ

def len_words(some_tuple: tuple) -> int:
    len_words_list = [len(elem) for elem in some_tuple if str(elem).isalpha()]
    return sum(len_words_list)


def count_letters_and_digits(some_list: list) -> int:
    counter = 0
    for elem in map(str, some_list):
        for cr in elem:
            if cr not in string.punctuation:
                counter += 1
    return counter


def count_odd_numbers(number: int) -> int:
    odd_numbers = [int(num) for num in str(number) if int(num) % 2 != 0]
    return len(odd_numbers)


def count_letters(some_string: str) -> int:
    letters = [letter for letter in some_string if letter.isalpha()]
    return len(letters)


def type_checker(some_argument):
    if type(some_argument) == tuple:
        return len_words(some_argument)
    elif type(some_argument) == list:
        return count_letters_and_digits(some_argument)
    elif type(some_argument) == int:
        return count_odd_numbers(some_argument)
    elif type(some_argument) == str:
        return count_letters(some_argument)


print(type_checker((1, 1.6, "anything", 15, "seventeen")))
print(type_checker([1, 1.6, "anything", 15, "seventeen"]))
print(type_checker(123456789))
print(type_checker("I had a wonderful time today"))
