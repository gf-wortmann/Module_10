# Домашнее задание по теме "Потоки на классах"
# Цель: научиться создавать классы наследованные от класса Thread.

from time import sleep
from threading import Thread


class Knight(Thread):
    max_enemies_number = 100
    
    def __init__(self, knight_name, force):
        self.knight_name = knight_name
        self.force = force
        self.enemies = Knight.max_enemies_number
        self.days_of_battle = 0
        super().__init__()
    
    def run(self):
        print(f'{self.knight_name}, на нас напали!')
        while self.enemies:
            self.enemies -= self.force
            self.days_of_battle += 1
            print(f'{self.knight_name} сражается {self.days_of_battle} дней(дня)..., осталось {self.enemies} врагов...')
            sleep(1)
        print(f'{self.knight_name} одержал победу спустя {self.days_of_battle} дней(дня)!')


knight_1 = Knight('Sir Lancelot', 10)
knight_2 = Knight('Sir Galahad', 20)
knight_1.start()
knight_2.start()
knight_1.join()
knight_2.join()
print('Все битвы закончились!')
