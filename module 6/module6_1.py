class Animal():
    alive = True
    fed = False

    def __init__(self,name):
        self.name = name

    def eat(self,food = None):
        if food is None:
            print(f'{self.name} ничего не съел :(')
        elif food.edible is True:
            print(f'{self.name} съел {food.name} и насытился ^_^')
            self.fed = True
        elif food.edible is False:
            print(f'{self.name} съел {food.name} и отравился.')
            self.alive = False

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant():
    edible = False

    def __init__(self,name):
        self.name = name


class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)