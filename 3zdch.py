x = input('введите число по парам - ')

list1 = list(x)
list_s = []

a = 999
z = 0

for i in (list1):
    if a == 999:
        if i.isdigit():
            a = int(i)
    elif i.isdigit():
        z = a * int(i)
        list_s.append(z)
        a = 888
    elif a == 888:
        a = 999
    else:
        continue

list_s.append(0)
sch1 = 1
list_ss = []

for i in range(len(list_s)):
    if list_s[i] == 0:
        break
    else:
        if list_s[i]==list_s[i+1]:
            sch1 += 1
        elif list_s[i]!=list_s[i+1]:
            if sch1 == 0:
                continue
            else:
                list_ss.append(sch1)
                sch1 = 1

print(f'итог: {max(list_ss)}')







