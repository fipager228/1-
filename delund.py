import random

def deltarom(a,b):
    s = random.randint(a,b)
    return s

def love(op):
    lv = op // 31
    print(f' ваша ЛЮБОВЬ равна {lv} Lv с вашим количеством {op} опыта .')
    return lv

def dark_dollr(zl):
    dd = zl // 1.5
    print(f' ваши {zl} золотых, по курсу тёмного доллара будет равна {dd} .')
    return dd

def gold(dd):
    zl = dd * 1.5
    print(f' ваши {dd} тёмные доллары , по курсу золотых будет равна {zl} .')
    return zl

def point(dd):
    k = deltarom(1,15)
    kyrs = k * 0.5

    pl = dd * kyrs
    print(f' ВООУ ВАШИ {dd} [тёмные] ДОЛЛАРЫ будут [СТОИМОСТЬ] {pl} в ОЧКАХ!! ')
    return pl

def love_in(op):
    lv = op // 31
    return lv

def dark_dollr_in(zl):
    dd = zl // 1.5
    return dd

def gold_in(dd):
    zl = dd * 1.5
    return zl

def point_in(dd):
    k = deltarom(1,15)
    kyrs = k * 0.5

    pl = dd * kyrs
    return pl

def fridm(list_f):
    frdm = 0
    for f in list_f:
        if f == 'Cделкаел':
            frdm = frdm + 25
        if f == 'Касса Дьявола':
            frdm = frdm + 25
        if f == 'Молот из леген':
            frdm = frdm + 25
        if f == 'Осколок тьмы':
            frdm = frdm + 25
        else:
            continue
    print(f" вы СВОБОДНЫ на {frdm} % ")
    return frdm

def fridm_in(list_f):
    frdm = 0
    for f in list_f:
        if f == 'Cделкаел':
            frdm = frdm + 25
        if f == 'Касса Дьявола':
            frdm = frdm + 25
        if f == 'Молот из леген':
            frdm = frdm + 25
        if f == 'Осколок тьмы':
            frdm = frdm + 25
        else:
            continue
    return frdm

