# Домашнее задание по теме "Создание потоков".
# Цель: понять как работают потоки на практике, решив задачу

from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for word in range(word_count):
            f.write(f'Какое-то слово №{word+1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
            
        
start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time = datetime.now()
time_spent_directly = finish_time - start_time
print(f'Время работы функций: {time_spent_directly}')


start_time = datetime.now()

th_1 = Thread(target=write_words, args=(10, 'example5.txt'))
th_2 = Thread(target=write_words, args=(30, 'example6.txt'))
th_3 = Thread(target=write_words, args=(200, 'example7.txt'))
th_4 = Thread(target=write_words, args=(100, 'example8.txt'))

th_1.start()
th_2.start()
th_3.start()
th_4.start()

th_1.join()
th_2.join()
th_3.join()
th_4.join()

finish_time = datetime.now()
time_spent_with_threads = finish_time - start_time
print(f'Время работы потоков: {time_spent_with_threads}')
print(f'Время работы потоков меньше в {time_spent_directly / time_spent_with_threads:.2f} раза')
