
class Horse:

    def __init__(self,x_distance = 0, sound = 'Frr',y_distance = 0):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)
        super().__init__(sound)

    def run(self,dx):
        self.x_distance = self.x_distance + dx
        print(f'Позиция изменилась на {self.x_distance}')

class Eagle:

    def __init__(self,y_distance = 0,sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self,dy):
        self.y_distance = self.y_distance + dy
        print(f'Высота изменилась на {self.y_distance}')

class Pegasus(Horse,Eagle):
    
    def __init__(self,x_distance = 0,y_distance = 0,sound = ''):
        super().__init__(x_distance,y_distance,sound)
        #super().__init__(sound)

    def move(self,dx,dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        x = {'x':self.x_distance,'y':self.y_distance}
        return x

    def voice(self):
        return print(self.sound)

p1 = Pegasus()

print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()