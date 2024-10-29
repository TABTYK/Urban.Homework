import threading
import time
import random
from queue import Queue
from threading import Thread

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue() 
        self.tables = tables

    def guest_arrival(self, *guests):
        for g in guests:
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    print(f"{g.name} сел(-а) за стол номер {t.number}")
                    t.guest.start()  # Запускаем поток гостя
                    break
            else:
                # Если все столы заняты, отправляем гостя в очередь
                self.queue.put(g)
                print(f"{g.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(t.guest is not None for t in self.tables):
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f"{t.guest.name} за столом номер {t.number} покушал(-а) и ушёл(ушла)")
                    t.guest = None
                    if not self.queue.empty():
                        # Сажаем следующего гостя из очереди
                        next_guest = self.queue.get()
                        t.guest = next_guest
                        print(f"{next_guest.name} сел(-а) за стол номер {t.number}")
                        t.guest.start()  # Запускаем поток гостя

# Пример выполнения программы
# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()