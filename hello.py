from random import randint

spisok = []
def lst():
    for i in range(1, 101):
        spisok.append(randint(1, 100))
    print(spisok)

lst()

def tpl(spisok_1):
    min = 101
    max = 0
    for i in range(0, 100):
        if min >= spisok_1[i]:
            min = spisok_1[i]
        if max <= spisok_1[i]:
            max = spisok_1[i]
    return (min, max)

print(tpl(spisok))

# Вариант №2

spisok = []

for i in range(1, 101):
    spisok.append(randint(1, 100))
print(spisok)

def tpl(spisok_1):
    min = 101
    max = 0
    for i in range(0, 100):
        if min >= spisok_1[i]:
            min = spisok_1[i]
        if max <= spisok_1[i]:
            max = spisok_1[i]
    return (min, max)

print(tpl(spisok))

word = input('Введите строку: ')

spisok = []
while (word != ''):
    spisok.append(word)
    for i in range(0, len(spisok)-1):
        if word == spisok[i]:
           spisok.pop()
    word = input('Введите строку: ')
print(spisok)