# Многопроцессное программирование
from multiprocessing import Pool, cpu_count
from time import time
import os

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            if not file.readline():
                break
            all_data.append(file.readline())


if __name__ == '__main__':
    # Создаем список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 4)]

    # Линейный вызов
    start_time = time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time() - start_time
    print(f"Линейный подход: {linear_duration} секунд")

    # Многопроцессный вызов
    start_time = time()
    with Pool(processes=cpu_count()) as pool:
        pool.map(read_info, filenames)
    multiprocess_duration = time() - start_time
    print(f"Многопроцессный подход: {multiprocess_duration} секунд")

