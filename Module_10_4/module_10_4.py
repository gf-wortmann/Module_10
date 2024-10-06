# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Цель: Применить очереди в работе с потоками, используя класс Queue.

import queue
from time import sleep
from threading import Thread
from random import randint


class Guest(Thread):
    
    def __init__(self, name):
        self.Name = name
        super().__init__()
    
    def run(self):
        sleep(randint(3, 10))


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
    
    def set_guest(self, guest):
        self.guest = guest
    
    def is_free(self):
        return self.guest is None
    
    def release(self):
        self.guest = None


class Cafe:
    def __init__(self, *tables):
        self.tables = []
        for the_table in tables:
            self.tables.append(the_table)
        self.queue = queue.Queue()
    
    def guests_arrival(self, *arrived_guests):
        the_guests = [*arrived_guests]
        for table in self.tables:
            if table.is_free():
                t = table.number
                g = the_guests.pop()
                table.set_guest(g)
                print(f'{g.Name} сел(а) за стол номер {t}')
                g.start()
        
        for guest in the_guests:
            print(f'{guest.Name} в очереди')
            self.queue.put(guest)
    
    def serve_guests(self):
        def all_tables_free():
            res = True
            for t in self.tables:
                if not t.is_free():
                    res = False
            return res
        
        while not all_tables_free():
            for table in self.tables:
                if not table.is_free() and not table.guest.is_alive():
                    print(f'{table.guest.Name} покушал(а) и ушёл(ла)')
                    print(f'Стол №{table.number} свободен')
                    table.guest.join()
                    table.release()
            
            for table in self.tables:
                if table.is_free() and not self.queue.empty():
                    guest = self.queue.get()
                    table.set_guest(guest)
                    guest.start()
                    print(f'{guest.Name} вышел(ла) из очереди и сел(а) за стол номер {table.number}')


guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

tables = [Table(i) for i in range(1, 6)]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guests_arrival(*guests)
cafe.serve_guests()