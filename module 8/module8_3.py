class Car():
    def __is_valid_vin(self,vin_number):
        if isinstance(vin_number,int):
            if vin_number in range(1000000,9999999):
                return True
            else:
                try:
                    raise IncorrectVinNumber('Неверный диапазон для vin номера')
                except IncorrectVinNumber as exc:
                    print(exc.message)
        else:
            try:
                raise IncorrectVinNumber('Некорректный тип vin номер')
            except IncorrectVinNumber as exc:
                print(exc.message)

    def __is_valid_numbers(self,numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                try:
                    raise IncorrectCarNumbers('Неверная длина номера')
                except IncorrectCarNumbers as exc:
                    print(exc.message)
        else:
            try:
                raise IncorrectCarNumbers('Некорректный тип numbers')
            except IncorrectVinNumber as exc:
                print(exc.message)

    def __init__(self,model = str(),__vin = int(), __numbers = str()):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        if self.__is_valid_vin(__vin) and self.__is_valid_numbers(__numbers):
            print(f'{self.model} успешно создан')

class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 2020202, 'нет номера')
