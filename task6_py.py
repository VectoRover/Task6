import os
path_to_file = "F:/prog/input.txt"
file = open(path_to_file, "r")

try:
    if os.stat(path_to_file).st_size > 0:
        print("file opened successfully")
    if os.stat(path_to_file).st_size == 0:
        print("Error: empty file")
        exit(-3)
except OSError:
    print("cannot open file")


def scan(file):
    string = file.read()
    temp = ""
    i = 0
    flag = 0
    count = 0
    temp1 = 0
    temp2 = 0
    if len(string) == 0:
        print("Error: empty file")
        exit(-3)
    for index in range(len(string)):
        if (string[index] != " ") or (string[index] != "\n"):
            temp += string[index]
        if (string[index] == " ") or (string[index] == "\n") or (index == (len(string) - 1)):
            try:
                temp2 = int(temp)
                if (i == 0):
                    i += 1
                    temp1 = temp2
                if (temp2 <= temp1) and (i != 0) and (flag == 1):
                    flag = 0
                if (temp2 > temp1) and (i != 0) and (flag == 0):
                    flag = 1
                    count += 1
                temp1 = temp2
            except ValueError:
                pass
            temp = ""
    return count

def Autotest():
    path_to_file = "F:/prog/autotest.txt"
    file = open(path_to_file, "r")
    answer = scan(file)
    if answer == 2:
        print("Автотест сдан")
    else:
        print("Автотест проавлен")

Autotest()
print("Количество промежутков возрастания =", scan(file))





