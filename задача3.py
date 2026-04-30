import math


z = input('ведите числа - ')

list2= z.split()
list1 = list(z)
print(list1)
list_s = []
a = 999
x=0

for i in list1:
    if a == 999:
        if i.isdigit():
            a = i
    elif i.isdigit():
        print(i)
        x = int(i) * int(a)
        list_s.append(x)
        print (x,'xxx')
        a = 888
    elif a == 888:
        a = 999
    else:
        continue

print(list_s)

sch = 1
for j in range(len(list_s)):


    if list_s[j] == list_s[j+1]:
        sch =+1
    else:
        print(sch)
        sch = 0




