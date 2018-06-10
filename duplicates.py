import os
import sys
import collections


def find_all_files_in_filepath(filepath):
    tree = os.walk(filepath)
    paths_to_files = collections.defaultdict(list)
    for dir_path, _, file_names in tree:
        for file_name in file_names:
            paths_to_files[file_name].append(dir_path)
    return paths_to_files


def find_dublicates(paths_to_files):
    dublicates = collections.defaultdict(list)
    path = 1
    name = 0
    for name in paths_to_files:
        if len(paths_to_files[name]) > 1:
            dublicates[name].append(paths_to_files[name])
    return dublicates


def print_dublicates(dublicates):
    print('Дубликаты: ')
    for name in dublicates:
        print(name, 'Пути: ', dublicates[name])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Вы не ввели путь к папке')
    filepath = sys.argv[1]
    if os.path.isdir(filepath) is False:
        exit('Данный путь не ведет к каталогу')
    file_name_path = find_all_files_in_filepath(filepath)
    dublicates = find_dublicates(file_name_path)
    print_dublicates(dublicates)
