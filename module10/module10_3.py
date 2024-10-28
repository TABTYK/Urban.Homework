import time
from random import randint
import threading


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for k in range(100):
            rand = randint(50,500)
            self.balance += rand
            if self.lock.locked() == True and self.balance >= 500:
                self.lock.release()
            print(f"Пополнение: {rand}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self): #Если снятие отклонилось, то запрос на снятие сам по себе не возообновляется
        for i in range(100):
            rand = randint(50,500)
            print(f"Запрос на {rand}")
            if rand <= self.balance:
                self.balance -= rand
                print(f"Снятие: {rand}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.002)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')