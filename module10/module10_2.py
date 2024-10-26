import threading
from threading import Thread
import time

class Knight(Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            enemies -= self.power
            days += 1
            time.sleep(1)
            print(f'{self.name} сражается {days} дня,осталось {enemies} воинов.\n')
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")
#knights =[]
first_knight = Knight('Sir Lancelot', 20) #knights.append(first_knight)
second_knight = Knight("Sir Galahad", 10) #knights.append(second_knight)
third_knight = Knight('Sir Persival', 25) #knights.append(third_knight)


first_knight.start()
second_knight.start()
third_knight.start()

first_knight.join()
second_knight.join()
third_knight.join()