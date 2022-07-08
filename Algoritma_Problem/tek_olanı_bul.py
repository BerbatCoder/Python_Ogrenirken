def bul(sayi):
    toplam = []
    for x in range(sayi):
        if x % 2 == 1:
            toplam.append(x)
    #print(toplam)
    print(sum(toplam))
bul(7)