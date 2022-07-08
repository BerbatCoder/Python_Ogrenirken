def bul(sayi):
    sayac = 0
    for i in range(2,sayi):
        if sayi % i == 0:
            sayac += 1
    if sayac == 0:
        print('sayınız asaldır')
    elif sayac > 0:
        print('sayınız asal değildir.')
bul(int(input('Sayınızı Giriniz: ')))