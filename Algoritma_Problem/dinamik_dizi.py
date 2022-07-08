def al():
    dizi = []
    sayac = 0
    istedik = int(input('Kaç Sayı Gireceksiniz: '))
    while len(dizi) != istedik:
        sayac += 1
        deg = int(input(f'{sayac}. Sayınızı Giriniz: '))
        dizi.append(deg)
        toplam = sum(dizi)
    print(f'Girdiğiniz Sayıların Ortalaması: ',toplam // sayac)
al()