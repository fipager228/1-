import random

s = input("Введите строку (минимум 4 слова): ")
s1 = s.split()

if len(s1) < 4 :
    print("Ошибка! \nНужно минимум 4 слова.")
else:
    ra = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    sf = []

    for i in s1:
        if i.isdigit():
            num = int(i)
            if num >= 1 and num <= 5:
                n = ""
                for k in range(num):
                    r = random.randint(0, len(ra)-1 )
                    n = n + ra[r]
                sf.append(n)
            else:
                sf.append(i)
        else:
            sf.append(len(i))

    c = len(sf)
    zi = 1
    while zi * zi < c:
        zi=zi+1

    m = []
    idx = 0
    for r in range(zi):
        row = []
        for c in range(zi):
            if idx < len(sf):
                row.append(sf[idx])
                idx=idx+1
            else:
                row.append(0)
        m.append(row)

    for i in m:
        print(i)