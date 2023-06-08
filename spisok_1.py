
spisok_1 = [12, 14, 119, 329, 1611, 1442, 939, 234]
spisok_2 = [14, 24, 116, 259, 1616, 1442, 992, 324]
spisok_3 = [18, 134, 13, 296, 1618, 1424, 994, 344]
spisok_4 = [16, 141, 14, 294, 1613, 1423, 999, 344]
def sort_list(sort_dir):
    if sort_dir == 1:
        for i in range(len(spisok_5)-1):
            for j in range(len(spisok_5)-1 - i):
                if spisok_5[j] < spisok_5[j + 1]:
                    temp_1 = spisok_5[j]
                    spisok_5[j] = spisok_5[j + 1]
                    spisok_5[j + 1] = temp_1
    else:
        for i in range(len(spisok_5) - 1):
            for j in range(len(spisok_5) - 1 - i):
                if spisok_5[j] > spisok_5[j + 1]:
                    temp_1 = spisok_5[j]
                    spisok_5[j] = spisok_5[j + 1]
                    spisok_5[j + 1] = temp_1

spisok_5 = spisok_1 + spisok_2 + spisok_3 + spisok_4
print(spisok_5)
input_check = 'null'
while(input_check != 'exit'):
    user = input('Введите \n1 - для сортировки по убыванию \n2 - для сортировки '
                 'по возрастанию \n3 - для выхода из программы \nВведите значение: ')
    match user:
        case '1':
            sort_list(1)
            print(spisok_5)
        case '2':
            sort_list(2)
            print(spisok_5)
        case '3':
            print('Пока')
            input_check = 'exit'
        case _:
            print('Вы ввели неправильное значение!!!')
