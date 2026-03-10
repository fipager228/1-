import numpy as np


temp1 = []
vlv1 = []
vtr1 = []
obl1 = []
bvn1 = []


class Weather:
    def __init__(self, temp, vlv, obl, vtr, bvn):
        self.temp = temp
        temp1.append(self.temp)
        self.vlv = vlv
        vlv1.append(self.vlv)
        self.obl = obl
        obl1.append(self.obl)
        self.vtr = vtr
        vtr1.append(self.vtr)
        self.bvn = bvn
        bvn1.append(self.bvn)

day1 = Weather(2, 78, 30, 4, 756)
day2 = Weather(3, 56, 75, 6, 760)
day3 = Weather(7, 66, 63, 3, 761)
day4 = Weather(4, 76, 52, 3, 763)

sfin = np.array([temp1, obl1, vlv1, vtr1, bvn1])

maxss = list(sfin.max(axis=1))
minss = list(sfin.min(axis=1))
meanss = list(sfin.mean(axis=1))

print()
print(" Максимальные величины ")
# Порядок индексов: 0 (Темп), 4 (Давл), 2 (Влаж), 3 (Ветер), 1 (Обл)
print(f"Температура: {int(maxss[0])}°C\nАтмосферное давление: {int(maxss[4])} \nВлажность: {int(maxss[2])}%\nВетер: {int(maxss[3])} м/с\nОблачность: {int(maxss[1])}%")

print()
print(" Минимальные величины ")
print(f"Температура: {int(minss[0])}°C\nАтмосферное давление: {int(minss[4])} \nВлажность: {int(minss[2])}%\nВетер: {int(minss[3])} м/с\nОблачность: {int(minss[1])}%")

print()
print(" Средние величины ")
print(f"Температура: {float(meanss[0])}°C\nАтмосферное давление: {float(meanss[4])} \nВлажность: {float(meanss[2])}%\nВетер: {float(meanss[3])} м/с\nОблачность: {float(meanss[1])}%")

