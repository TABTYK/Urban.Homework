class House():
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor+1):
                print(i)

H1 = House('ЖК Горский', 18)
H1.go_to(6)
H2 = House('ЖК 52', 52)
H2.go_to(-3)