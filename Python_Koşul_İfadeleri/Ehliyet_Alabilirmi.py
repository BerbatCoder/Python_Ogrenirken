isim = input('İsminizi Yazınız : ')
yas = int(input('Yasınızı Yazınız : '))
if yas >= 18:
    print('Yaşınız Uygundur "Eğitim Bilgisi İlkokul - Lise - Üniversite"')
    egitim = input('Egitim Bilginizi Yazınız : ')
    if egitim == 'Lise' or egitim == 'lise' or egitim == 'Üniversite' or egitim == 'üniversite' :
        print('Eğitim Bilginizde Uygundur')
        print('*'*50)
        print(f'{isim} Kişisi Ehliyet Alabilme Durumu : Alabilirsiniz')
    elif egitim == 'İlkokul':
        print('Ehliyet Alabilme Durumunuz : Alamaz en az Lise')
    else:
        print('Yanlış Karakter')
elif yas < 18:
    print('Yaşınız Küçük olduğundan Alabilme durumu : Alamaz')
else:
    print('Yanlış Karakter')
