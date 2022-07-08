def bul():
    sayac = 0
    toplam = 0
    tek = 0
    cift = 0
    while sayac != 10:
        deg = int(input('Sayı Giriniz: '))
        sayac += 1
        toplam += deg
        if deg % 2 == 1 or toplam == 1:
            tek += 1
        if deg % 2 == 0:
            cift += 1
    print(f"Girdiğiniz Sayıların Toplamı: {toplam}")
    print(f"Girdiğiniz Sayıların tek olanlarının sayısı: {tek}")
    print(f"Girdiğiniz Sayıların çift olanlarının sayısı: {cift}")
bul()
