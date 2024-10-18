def add_everything_up(a,b):
    try:
        result = a + b
    except TypeError:
        a = str(a);b = str(b)
        result = a + b
    finally:
        print(result)

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)