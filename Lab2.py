#Котуранова Мария Сергеевна R3135 408879

import csv
from random import randint
import xml.dom.minidom as minidom

# Задание 1
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    cnt = 0
    for row in freader:
        if len(list(row)[1]) > 30:
            cnt += 1
    print(cnt)

print("Задание 2")
print('Введите автора')
search = input().lower()
flag = 0
result = set()
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    for row in freader:
        if list(row)[4].lower() == search or list(row)[3].lower() == search:
            price = float(list(row)[7])  # берем из даты только цену
            if price>=200:  # условие варианта 9
                flag = 1
                result.add(row[1])
    if flag == 0:
        print('Ничего не найдено')
    else:
        for book in result:
            print(book)


# Задание 3
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    flength = 0
    for row in freader:
        flength += 1  # считаем кол-во строчек
with open("books.csv") as r_file:
    freader = csv.reader(r_file, delimiter=";")
    random_list = [randint(1, flength) for i in range(20)]  # случайные 20 значений
    random_list.sort()
with open("books.csv") as r_file:
    in_use = list(csv.reader(r_file, delimiter=";"))
    with open('result.txt', 'w') as file:
        for i in random_list:
            file.write(str(i) + ' ' + in_use[i][3] + '. ' + in_use[i][1] + ' - ' + in_use[i][6] + '\n')
    file.close()

# Задание 4
num_code = []
char_code = []
with open('currency.xml', 'r') as file:
    for line in file:
        data=line.split()
        if len(data)>=2:
            num_code.append(int(data[0]))
            char_code.append(int(data[1]))
print("NumCode:", num_code)
print("CharCode:", char_code)
