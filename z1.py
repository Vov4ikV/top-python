

spisok_1 = ['Руслан и Людмила', 'Ревизор', 'Война и мир',  'Муму' ]
spisok_2 =  [1820, 1835, 1867, 1854]

def sort_books():
    for i in range(len(spisok_1)-1):
        for j in range(len(spisok_1)-1 - i):
            if spisok_1[j] < spisok_1[j + 1]:
                temp_1 = spisok_1[j]
                spisok_1[j] = spisok_1[j + 1]
                spisok_1[j + 1] = temp_1
                temp_2 = spisok_2[j]
                spisok_2[j] = spisok_2[j + 1]
                spisok_2[j + 1] = temp_2

# print(spisok_1, spisok_2)
# sort_books()
# print(spisok_1, spisok_2)

def sort_books_age():
    for i in range(len(spisok_2)-1):
        for j in range(len(spisok_2)-1 - i):
            if spisok_2[j] > spisok_2[j + 1]:
                temp_1 = spisok_1[j]
                spisok_1[j] = spisok_1[j + 1]
                spisok_1[j + 1] = temp_1
                temp_2 = spisok_2[j]
                spisok_2[j] = spisok_2[j + 1]
                spisok_2[j + 1] = temp_2
print(spisok_1, spisok_2)
sort_books_age()
print(spisok_1, spisok_2)

def print_books():
    for i in range(len(spisok_1)):
        print(spisok_1[i], spisok_2[i])
print_books()
