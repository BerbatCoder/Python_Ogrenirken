def sayhello(name = 'user'):
    return 'İsminiz : ' + name
msg = sayhello()
print(msg)

def total(num1,num2):
    return num1 + num2
result = total(10,10)
print(result)

def yasHesapla(dogumyili):
    return 2022 - dogumyili
poket = yasHesapla(2003)
print(poket)

def emeklilikhesap(dogumyili, isim):
    '''
    DOCSTRİNG : Doğum Yılınıza Göre emekliliğimizi hesapla
    INPUT : Doğum Yılı
    Output : Hesaplanan Yıl Bilgisi
    '''
    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'{isim} Emekliliğinize kalan gün {emeklilik}')
    else:
        print('Emekli Olabilirsiniz')
emeklilikhesap(2000,'Onur')

print(help(emeklilikhesap))