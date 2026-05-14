
from prettytable import PrettyTable


class Person:
    def __init__(self, name,atk,defe,lvl,hp):
        self.name = str(name)
        self.lvl = lvl
        self.atk = atk * (0.4 * lvl)
        self.defe = defe * (0.2 * lvl)
        self.hp = hp * (0.9 * lvl) + ( defe * (0.2 * lvl) )
        self.energ = 10

        self.inv = []

    def prov(self):
        if self.hp <= 0:
            print(f'игрок {self.name} умер \n')

    def attake(self,other):
        if other.hp <= 0:
            print("противник мёртв, нельзя отоковать.\n ")

        else:
            print(f'игрок {self.name} атакует! \n')
            if self.energ >= 2:
                other.hp -= self.atk
                print(f'игрок {self.name} нанёс урон {self.atk} игроку {other.name}.\n')
                if other.hp <= 0:
                    other.prov()
                elif other.hp > 0:
                    print(f'у противника осталось {other.hp} хп.\n')
                self.energ -= 2
            elif self.energ < 2:
                print('нет энергии\n')

    def invent(self):
        table = PrettyTable()
        table.field_names = ["ваш инвентарь :"]

        for i in self.inv:
            table.add_row([i])
        print(table)

    def pickup(self,other):
        self.inv.append(other)




nps = Person('nps_1',100,100,1,100)
nps_1 = Person('nps_2',100,100,1,100)

nps.pickup('лосось')
nps.invent()


