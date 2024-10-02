import math

def isPrime(n):
    if n % 2 or n % 3 or n % 5 or n % 7 or n % 9:
        return True

class Figure():

    filled = bool()

    def __init__(self, __sides = [1], __color = [int(), int(), int()]):
        self.__sides = __sides
        self.__color = __color

    def get_color(self):
        return print(self._Figure__color)

    def __is_valid_color(self,r = int(),g = int(),b = int()):
        l1 = list()
        for i in [r,g,b]:
            if isPrime(i) and i <=255 and i >=0:
                l1.append(i)
            else:
                print('Вы неправильно ввели данные к RGB')
        #print(l1)
        if len(l1) == 3:
            self._Figure__color = l1
            return l1

    def __is_valid_sides(self,not_args):
        if self.sides_count == len(not_args) or self.sides_count == 12 and len(not_args) == 1:
            for i in not_args:
                if i >=0:
                    pass
                else:
                    print('Размер стороны не может быть отрицательным')
                    return False
            return True
        else:
            print('Количество переданных сторон не совпадает с текущим их количеством.',len(self.__sides))
            return False

    def get_sides(self):
        return print(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            print(f'Стороны объекта были изменены на {new_sides}')
            self.__sides = new_sides
        else:
            print('Mistake')

    def set_color(self,r = int(0),g = int(0),b = int(0)):
        print(f'Цвет объекта был изменён на {self.__is_valid_color(r,g,b)}')


class Circle(Figure):

    sides_count = 1

    def __init__(self,__sides = [1], __color = [0,0,0],__radius = None):
        self.__radius = __sides[0] / 6.28
        super().__init__(__sides,__color)

    def get_square(self):
        self.__radius = self._Figure__sides[0] / 6.28
        return print(self.__radius * self.__radius * 3.14)

class Triangle(Figure):

    sides_count = 3

    def __init__(self,__sides = [1,1,1],__color = [0,0,0]):
        super().__init__(__sides,__color)

    def get_square(self):
        p = 0.5 * self.__len__()
        S = math.sqrt((p*(p-self._Figure__sides[0])*(p-self._Figure__sides[1])*(p-self._Figure__sides[2])))
        return print(S)

class Cube(Figure):

    sides_count = 12

    def __init__(self,__sides = [1],__color = [0,0,0]):
        super().__init__(__sides,__color)

    def get_volume(self):
        return print((self._Figure__sides[0] * self._Figure__sides[0]) * self._Figure__sides[0])


#circle1 = Circle([10],(200, 200, 100))
#circle1.get_color()
#circle1.get_sides()
#circle1.get_square()

triangle1 = Triangle([10,12,15], (100,0,100))
triangle1.get_square()
#triangle1.set_sides(14,12,13)

cube1 = Cube([15],(255,255,255))
#cube1.get_volume()
#cube1.set_color(123,52,322)
#cube1.get_color()
cube1.set_sides(5)
cube1.get_volume()