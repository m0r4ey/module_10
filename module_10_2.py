# Потоки на классах
from time import sleep
import threading

print_lock = threading.Lock()
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            with print_lock:
                print(f'{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.')
            sleep(1)
            if enemies == 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
