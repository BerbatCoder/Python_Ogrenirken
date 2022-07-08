# Gönderilen bir kelimeyi belirtilen kez ekranda gösterilen fonksiyonu yazın.
'''
def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)
'''
# Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
'''
def cıktı(kelime,sayi):
    print(kelime * sayi)
cıktı('Onur',5)
'''
# Gönderilen 2 sayıyı arasındaki tüm asal sayıları bulun
'''
def asalSayilarBul(sayi1, sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input('Sayı 1: '))
sayi2 = int((input('Sayı 2: ')))

asalSayilarBul(sayi1 ,sayi2)
'''
# Kednisine gönderilen bir sayının tam bölenleri bir liste şeklinde döndürün

def bolencık(sayi):
    tamBolen = []
    for x in range(2, sayi):
        if sayi % x == 0:
            tamBolen.append(x)
            
    return tamBolen
            
print(bolencık(15))





