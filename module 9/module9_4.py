from os import startfile
from random import choice, random

first = 'Мама мыла раму'
second = 'Рамена мало было'

one_of_this = list(map(lambda x,y:x==y, first,second))
print(one_of_this)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name,'a', encoding='UTF-8') as file:
            for info in data_set:

                file.write(f'{str(info)}\n')
            #file.write(data_set)
            return startfile(file_name)
    return write_everything

result = get_advanced_writer('example.txt')
result('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall():
    def __init__(self,*words):
        self.words = words

    def __call__(self, *args, **kwargs):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
