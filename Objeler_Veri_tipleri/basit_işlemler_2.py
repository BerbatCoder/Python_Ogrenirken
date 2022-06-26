'''

     Daire Alanı : pi re kare
     Daire Çevresi : 2 pi re

     * Yarı çapı verilen bir dairenin alan çevresini hesaplayınız (r: 3.14)

'''
r = float(input('Yarı Çap : '))
pi = 3.14
alan = pi * (r ** 2)
cevresi = 2 * pi * r
print("Daire alanı {} , Daire Çevresi {}" .format(alan, cevresi))
