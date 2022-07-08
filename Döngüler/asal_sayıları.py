# asal sayı kontrolü-hesaplama ve fibonacci

'''
Soru: Girilien bir sayının asal olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariçtam böleni olmayan sayılara denir. 1
'''
sayi = int(input('Bir Sayı Griniz : '))

asalmi = True
if sayi == 1:
    print('Sayınız Asal Değildir.')

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break
if asalmi:
    print('Sayı Asaldır')
else:
    print('Sayı Asal Değildir.')