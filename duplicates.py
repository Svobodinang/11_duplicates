import os
import sys
import collections


def find_all_files(filepath):
    tree = os.walk(filepath)
    files = []
    for argumen in tree:
        for file_name in argumen[2]:
            files.append(file_name)
    return files


def find_dublicates(files):
    dublicates = []
    count_mas = collections.Counter()
    for file_name in files:
        count_mas[file_name] += 1
    for file_name in files:
        if (count_mas[file_name] > 1) and (file_name not in dublicates):
            dublicates.append(file_name)
    return dublicates


def print_dublicates(dublicates):
    print('Дубликаты: ')
    print(dublicates)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Вы не ввели путь к папке')
    filepath = sys.argv[1]
    files = find_all_files(filepath)
    dublicates = find_dublicates(files)
    print_dublicates(dublicates)
