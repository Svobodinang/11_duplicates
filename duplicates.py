import os
import sys
import collections


def find_all_files_in_filepath(dirpath):
    tree = os.walk(dirpath)
    paths_to_files = collections.defaultdict(list)
    for dir_path, _, file_names in tree:
        for file_name in file_names:
            paths_to_files[file_name].append(dir_path)
    return paths_to_files


def find_duplicates(paths_to_files):
    duplicates = collections.defaultdict(list)
    for file_name in paths_to_files:
        if len(paths_to_files[file_name]) > 1:
            duplicates[file_name].append(paths_to_files[file_name])
    return duplicates


def print_dublicates(duplicates):
    print('Дубликаты: ')
    for name in duplicates:
        print(name, 'Пути: ', duplicates[name])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('Вы не ввели путь к папке')
    dirpath = sys.argv[1]
    if not os.path.isdir(dirpath):
        exit('Данный путь не ведет к каталогу')
    file_name_path = find_all_files_in_filepath(dirpath)
    duplicates = find_duplicates(file_name_path)
    print_dublicates(duplicates)
