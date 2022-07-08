import random

satir = int(input('Satır Sayısı: '))
sutun = int(input('Sutun Sayısı: '))

m = [[0 for x in range(sutun)] for y in range(satir)]
mt = [[0 for x in range(satir)] for y in range(sutun)]

for i in range(satir):
    for j in range(sutun):
        m[i][j] = random.randint(0,9)
        mt[j][i] = m[i][j]


print(m)
print(mt)