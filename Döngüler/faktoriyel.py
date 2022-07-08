sayi = int(input('Faktoriyeli Alınacak Sayıyı Giriniz : '))
sonuc = 1
while sayi > 0:
    sonuc *= sayi
    sayi -= 1
print(sonuc)