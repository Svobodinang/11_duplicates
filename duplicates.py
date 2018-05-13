import os
import sys


files = []


def find_all_files(filepath):
    os.chdir(filepath)
    for path in os.listdir(filepath):
        if not os.path.isfile(path):
            find_all_files(filepath +'\\'+ path)
        else:
            files.append(path)


def find_dublicates():
    dubl_files = []
    used_file = ''
    for index in range(0, len(files) - 1):
        for index_dubl in range(index + 1, len(files) - 1):
            if files[index] == files[index_dubl] and files[index]!=used_file:
                dubl_files.append(files[index])
                used_file = files[index]
    return dubl_files


def print_dublicates(dubl_files):
    print("Дубликаты: ")
    print(dubl_files)


if __name__ == '__main__':
    filepath = sys.argv[1]
    find_all_files(filepath)
    dubl_files = find_dublicates()
    print_dublicates(dubl_files)
