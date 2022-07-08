import math
import random
def bul(kacsayi):
    dizi = []
    while kacsayi != len(dizi):
        at = random.randint(1,100)
        dizi.append(at)
    sayac = 0
    for x in dizi:
        fark = x - sum(dizi)
        fark = fark ** 2
        sayac += fark
    ssapma = math.sqrt(sayac/kacsayi)
    
    print(f'Sayıları{dizi}')
    print(f'Standart Sapma {ssapma}')
    print('Dizideki sayıların toplamı',sum(dizi))
    print('Dizideki sayıların ortalaması',sum(dizi) // len(dizi))
bul(90)

