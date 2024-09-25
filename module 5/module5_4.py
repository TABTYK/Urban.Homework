from module5_3 import House

class House(House):
    houses_history = []
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return cls.__instance

    def __del__(self):
        print(f"{self.name} снесен но он останется в истории.")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
House.__del__(h2)
House.__del__(h3)

print(House.houses_history)