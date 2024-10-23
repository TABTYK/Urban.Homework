class StepValueError(ValueError):
    pass

class Iterator():

    def __init__(self,start,stop, step=1):
        try:
            if step==0:
                raise StepValueError

            self.start = start
            self.stop = stop
            self.step = step
            self.pointer = 0

        except StepValueError:
            print('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        if self.step > 0:
            while self.pointer < self.stop:
                self.pointer += self.step
                if self.pointer > self.stop:
                    raise StepValueError()
                return self.pointer
            raise StepValueError()

        else:
            while self.pointer > self.stop:
                self.pointer += self.step
                if self.pointer < self.stop:
                    raise StepValueError()
                return self.pointer
            raise StepValueError()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except AttributeError: # Поставил исключение, потому что проверка шага на 0 происходит до
                       # создания переменной self.start
    print('ШАГ УКАЗАН НЕВЕРНО')
except StepValueError:
    print('\nПеребор завершен')

iter2 = Iterator(start=-5, stop=1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


try:
    for i in iter2:
        print(i, end=' ')
except StepValueError:
    print('\nПеребор завершен')

try:
    for i in iter3:
        print(i, end=' ')
except StepValueError:
    print('\nПеребор завершен')


try:
    for i in iter4:
        print(i, end=' ')
except StepValueError:
    print('\nПеребор завершен')


try:
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print('\nПеребор завершен')

