# Блокировки и обработка ошибок
import threading
from random import randint
from time import sleep

print_lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            rnd = randint(50, 500)
            self.balance += rnd
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            with print_lock:
                print(f'Пополнение: {rnd}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            rnd = randint(50, 500)
            with print_lock:
                print(f'Запрос на {rnd}')
            if rnd <= self.balance:
                self.balance -= rnd
                with print_lock:
                    print(f'Снятие: {rnd}. Баланс: {self.balance}')
            else:
                with print_lock:
                    print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')