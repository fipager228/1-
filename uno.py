import random

color = [1,2,3,4,5,6,7,8,9,0,'+2','БЛОК','СвапКолор']
icon = ['Красный','Синий','Жёлтый','Зелёный','Чёрная']

stol = []

class Uno:
    def __init__(self, name):
        self.name = str(name)
        self.invt = []

    def strt(self):
        while True:
            a = random.choice(color)
            if a == 'СвапКолор':
                b = 'Чёрная'
            else:
                while True:
                    b = random.choice(icon)
                    if b == 'Чёрная':
                        continue
                    else:
                        break
            card = [a, b]
            self.invt.append(card)
            if len(self.invt) == 6:
                break
            else:
                continue
    def plus1(self):
        while True:
            a = random.choice(color)
            if a == 'СвапКолор':
                b = 'Чёрная'
            else:
                while True:
                    b = random.choice(icon)
                    if b == 'Чёрная':
                        continue
                    else:
                        break
            card = [a, b]
            self.invt.append(card)
            break

    def kart(self):
        print('Твои карты: ')
        for i in range(len(self.invt)):
            print()
            print(i+1,':')
            for j in range(2):
                print(self.invt[i][j], end=' ')

    def bam(self):
        if len(stol) == 0:
            while True:
                a = random.choice(color)
                if a == 'СвапКолор' or a == '+2' or a == 'БЛОК':
                    continue
                else:
                    while True:
                        b = random.choice(icon)
                        if b == 'Чёрная':
                            continue
                        else:
                            break
                card = [a, b]
                stol.append(card)
                print(f"Первая карта на столе: {stol[-1]}")
                break

        while True:
            print(f"На столе: {stol[-1]}")
            self.kart()
            print()

            kart_pl = input("Выбери номер карты (или 'взять'): ")

            if kart_pl == 'взять':
                self.plus1()
                print("Вы взяли карту.")
                break

            try:
                index = int(kart_pl) - 1
                if index < 0 or index >= len(self.invt):
                    print("Неверный номер карты.")
                    continue
            except ValueError:
                print("Введите число или 'взять'.")
                continue

            my_card = self.invt[index]
            top_card = stol[-1]

            can_play = False

            if my_card[0] == 'СвапКолор':
                can_play = True
            elif my_card[1] == top_card[1]:
                can_play = True
            elif my_card[0] == top_card[0]:
                can_play = True

            if can_play:
                stol.append(my_card)
                self.invt.pop(index)
                print("Ход принят!")

                if my_card[0] == 'СвапКолор':

                    while True:
                        print("Доступные цвета: 1) Красный, 2) Синий, 3) Жёлтый, 4) Зелёный ")
                        choice = input("Выберите цвет (1-4): ")

                        if choice == '1':
                            new_color = 'Красный'
                            break
                        elif choice == '2':
                            new_color = 'Синий'
                            break
                        elif choice == '3':
                            new_color = 'Жёлтый'
                            break
                        elif choice == '4':
                            new_color = 'Зелёный'
                            break
                        else:
                            print("Введите число от 1 до 4!")

                    stol[-1][1] = new_color
                    print(f"Цвет изменён на {new_color}")

                if my_card[0] == '+2':
                    print("Вы положили +2! Следующий игрок берёт 2 карты.")

                if my_card[0] == 'БЛОК':
                    print("Вы положили БЛОК! Следующий игрок пропускает ход.")

                if len(self.invt) == 0:
                    print("УНО! Вы победили!")

                break
            else:
                print("Эта карта не подходит!")




p1 = Uno("Игрок 1")


p1.strt()
p1.kart()

while True:
    p1.bam()

    p1.bam()
