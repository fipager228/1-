
import random

list_I = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
]
list_A = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
]

s = 0

def pole(list):
    for i in range(5):
        for j in range(5):
            print(list[i][j], end='  ')
        print()


def stav(list):

    y = random.randint(1, 2)
    x = random.randint(1, 2)

    list[y][x] = 'X'

    list[y - 1][x] = '='
    list[y + 1][x] = '='
    list[y][x - 1] = '='
    list[y][x + 1] = '='


def metk(list1, list2):
    global s
    while True:
        try:

            y = int(input("впишите 1 кардинату (1-5) - "))-1
            x = int(input("впишите 2 кардинату (1-5) - "))-1
            if list1[y][x] == '=':
                list2[y][x] = '#'
                print('теплее!')
                break
            elif list1[y][x] == '-':
                list2[y][x] = '*'
                print('холодно..')
                break
            elif list1[y][x] == 'X':
                list2[y][x] = 'X'
                print('Вы нашли клад!')
                s+=1
                break
        except ValueError, IndexError:
            print('извини, но нет')
            continue




print('ИГРА НАЙТИ КЛАД!')
print("* - Холодно\n# - Теплее\nX - КЛАД!")
stav(list_A)
while True:
    pole(list_I)
    metk(list_A, list_I)
    if s == 1:
        break
    else:
        continue
pole(list_A)