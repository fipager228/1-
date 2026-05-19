from collections import Counter
import time
import random
from prettytable import PrettyTable


print('Это симулятор кассира ! \n')

print('правила : \nвы должны обслуживать клиентов и ровно отдавать сдачу, если вы дадите больше положенной суммы, то вычтем из вашей зарплаты!')
zp = 1500
print(f'ваша зарплата : {zp}')
time.sleep(4)

list_cassa = [1,1,1,1,5,5,5,5,1,1,1,10,10,10,10,10,10,10,10,10,10,10,10,10,10,50,50,50,50,100,100,100,10,200,200,500,1000,10,1,1,1,1,200,200,100,100,50,50,50,500,1000,1000,1,1,1,1,1,1,2,2,3,3,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1]

def vide_cassa():
    list_cassa02 = Counter(list_cassa)
    table_cassa = PrettyTable()
    table_cassa.field_names = ['Номинал (руб)', 'Количество']

    for i in sorted(list_cassa02.keys()):
        table_cassa.add_row([i,list_cassa02[i]])

    print(table_cassa)

list_polca = ['хлеб','молоко','соль','сахар','сыр','лимонад','лапша быстрого приготовления','колбаса','молоток']
list_polca_cena = [45,50,30,35,66,120,40,60,150]


def polci():

    table_polca = PrettyTable()
    table_polca.field_names = ['продукты на полке','цена']
    for i in range(8):
        table_polca.add_row([list_polca[i],list_polca_cena[i]])

    print(table_polca)

def client():
    global zp
    c = random.randint(1,5)
    list_client = []
    list_client_cena = []

    for i in range(c):
        a = random.randint(0,8)
        list_client_cena.append(list_polca_cena[a])
        list_client.append(list_polca[a])


    for i in range(c):
        print(f'{i+1} продукт в корзине : {list_client[i]}. \nего цена : {list_client_cena[i]}.')
        time.sleep(0.5)
    x = sum(list_client_cena)
    print()
    xx = random.randint(x,x*3)
    time.sleep(0.9)
    print(f'клиент должен {x}, он отдал вам {xx}. отдайте ему здачу!({xx-x})')

    vide_cassa()
    s = 0
    while True:
        try:
            v = int(input('на "-1" вы увидете кассу, а на "-2" заканчиваете если готово!\nчто выбрать ? - '))
        except ValueError:
            print("введите число!")
            continue
        time.sleep(0.3)
        if v == -1:
            vide_cassa()
        elif v == -2:
            if s == xx - x:
                print("\ncдача выдана ровно! клиент доволен.")
                break
            elif s > xx - x:
                s_ = s - (xx - x)
                zp -= s_  #
                print(f'\nвы дали лишнего на {s_} . штраф вычтен!')
                print(f'ваша зарплата : {zp}')
                break
            elif s < xx - x:
                print(f"\nне достаточно! не хватает ещё {xx - x - s} . Продолжайте или нажмите -2.")
                continue
        elif v in list_cassa:
            list_cassa.remove(v)
            s = s + v
            print(f'выдали {v}. всего сдано: {s}. осталось: {(xx - x) - s}.')

        else:
            print('нет такого номинала в кассе!')

polci()
time.sleep(6)

k = random.randint(1,4)
print('\n')
print(f'сегодня будет {k} клиент(ов)')
print('')
for i in range(k):
    client()
