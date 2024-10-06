# Домашнее задание по теме "Многопроцессное программирование"
# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.

import multiprocessing
from pathlib import Path
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for s in file:
            all_data.append(s)


# start_all = datetime.datetime.now()
# for f in Path('.').glob('*.txt'):
#     start = datetime.datetime.now()
#     read_info(f)
#     finish = datetime.datetime.now()
#     print(f'время чтения файля {f} {finish - start}')
# finish_all = datetime.datetime.now()
# print(f'время чтения всех файлов: {finish_all - start_all}')
#
# # вывод в консоль:
# # время чтения файля file 1.txt 0:00:01.167000
# # время чтения файля file 2.txt 0:00:01.057011
# # время чтения файля file 3.txt 0:00:01.055000
# # время чтения файля file 4.txt 0:00:00.098000
# # время чтения всех файлов: 0:00:03.377011


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, [f.name for f in Path('.').glob('*.txt')])
    finish = datetime.datetime.now()
    print(f'время чтения всех файлов: {finish - start}')

# вывод в консоль:
# время чтения всех файлов: 0:00:01.410000
