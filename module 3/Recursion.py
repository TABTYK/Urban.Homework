def get_multiplied_digits(number):
    str_number = f'{number}'
    first = int(str_number[0])
    if number >= 10:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
print(get_multiplied_digits(121212))