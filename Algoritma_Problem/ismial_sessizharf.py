def hesap(metin):
    seslihatf = "aeıioöuü"
    sesli_sayac = 0

    for harf in metin:
        if harf in seslihatf:
            sesli_sayac += 1
    print(sesli_sayac)
hesap('kambur')