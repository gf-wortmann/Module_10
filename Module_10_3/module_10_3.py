# Домашнее задание по теме "Блокировки и обработка ошибок"
# Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.


from random import randint
from time import sleep
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.number_of_transactions = 10
        self.min_value = 50
        self.max_value = 500
        self.lock = Lock()
        if self.lock.locked():
            self.lock.release()
    
    def deposit(self):
        for i in range(self.number_of_transactions):
            sleep(0.01)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            adding = randint(self.min_value, self.max_value)
            self.balance += adding
            print(f'Пополнение: {adding}. Баланс: {self.balance}')
            
    def withdrawal(self):
        for i in range(self.number_of_transactions):
            sleep(0.01)
            if not self.lock.locked():
                withdraw = randint(self.min_value, self.max_value)
                print(f'Запрос на {withdraw}')
                if self.balance >= withdraw:
                    with self.lock:
                        self.balance -= withdraw
                        print(f'Снятие: {withdraw}. Баланс: {self.balance}')
                    
                else:
                    self.lock.acquire()
                    print(f'Запрос отклонён, недостаточно средств')
            else:
                pass


bk = Bank()
deposition = Thread(target=Bank.deposit, args=(bk,))
withdrawal = Thread(target=Bank.withdrawal, args=(bk,))

deposition.start()
withdrawal.start()
deposition.join()
withdrawal.join()

print(f'Итоговый баланс: {bk.balance}')
