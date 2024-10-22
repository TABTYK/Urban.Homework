def personal_sum(numbers):
    global result
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data +=1
            print('Некоректный тип данных для посчета суммы - ',i)
    return {'result':result,'incorrect_data':incorrect_data}

def calculate_average(numbers):
    delitel = 0
    try:
        Woo = personal_sum(numbers)
        for k in numbers:
            if isinstance(k,int):
                pass
            else:
                delitel +=1
        try:
            return Woo.get('result') / (len(numbers) - delitel)
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('Работаем только с коллекциями')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
