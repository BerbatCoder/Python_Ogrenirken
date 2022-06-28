"""
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

bilgi = int(input('Sayınızı Giriniz : '))
if (100 >= bilgi) and (0 <= bilgi):
    print('Sayınız 0 - 100 Arasındadır. ')
elif 100 < bilgi :
    print('100 sayısından büyük bir değer girdiniz.')
elif 0 > bilgi :
    print('Negatif Bir Değer Girdiniz')
else:
    ('Yanlış bir değer girdiniz') 

"""
"""
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

gir = int(input('Kontrol edilecek sayıyı yazınız: '))
toplam = (gir % 2) == 0
if toplam == True:
    print('Sayınız Çift Bir sayıdır') 
if toplam != True:
    print('Sayınız Tek  Bir sayıdır')

"""
"""
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

e_mail = 'onurdogan@gmail.com'
sifre  = '1234'

isteposta = input('E posta adresinizi Giriniz : ')
istesifre = input('Şifrenizi Giriniz : ')
Kontrol = (e_mail == isteposta) and (sifre == istesifre)
if Kontrol == True:
    print('Giriş yaptınız Hayırlı Olsun')
elif Kontrol != True:
    print('Şifre veya E posta hatalı')
"""


'''
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

x = input('1.Sayınızı Giriniz : ')
y = input('2.Sayınızı Giriniz : ')
z = input('3.Sayınızı Giriniz : ')
nedir = x > y 
if nedir == True:
    nedir = 'Büyüktür'
else:
    nedir = 'Küçüktür'
nedir2 = x > z
if nedir2 == True:
    nedir2 = 'Büyüktür'
else:
    nedir2 = 'Küçüktür'
nedir3 = y > x
if nedir3 == True:
    nedir3 = 'Büyüktür'
else:
    nedir3 = 'Küçüktür'
nedir4 = y > z
if nedir4 == True:
    nedir4 = 'Büyüktür'
else:
    nedir4 = 'Küçüktür'
nedir5 = z > x
if nedir5 == True:
    nedir5 = 'Büyüktür'
else:
    nedir5 = 'Küçüktür'
nedir6 = z > y
if nedir6 == True:
    nedir6 = 'Büyüktür'
else:
    nedir6 = 'Küçüktür'

print(f'1.Sayı : 2.sayıdan {nedir} 3.sayıdan {nedir2}')
print(f'2.Sayı : 1.sayıdan {nedir3} 3.sayıdan {nedir4}')
print(f'3.Sayı : 1.sayıdan {nedir5} 2.sayıdan {nedir6}')

'''

'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.

'''
'''
vize_1 = int(input('Vize Bir Notunuzu Giriniz : '))
vize_2 = int(input('Vize 2 Notunuzu Giriniz : '))
final  = int(input('Final Notunuzu Giriniz : '))

Kontrol = (vize_1+vize_2 / 2 ) * 0.6 + (final * 0.4)
if Kontrol >= 50 and final >= 50:
    print(f'Geçtiniz Notunuz {Kontrol}')
elif Kontrol < 50 and final >= 70: 
    print(f'Final Notu İle Geçtiniz {Kontrol}')
elif Kontrol < 50:
    print(f'Kaldınız Notunuz {Kontrol}')
elif final < 50:
    print('Final Notu Elliden Küçük : Kaldınız') 
else :
    ('Hatalı Giriş yaptınız. ')

'''
'''

6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4    => Zayıf 
   18.5-24.9 => Normal  
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman (Obez)
'''
kilo = float(input('Kilonuzu Giriniz : '))
boy = float(input('Boy Bilginizi Giriniz : '))
kontrol = (kilo / (boy ** 2)) 
if kontrol >= 0 and kontrol <= 18.4:
    print(f'Kilo İndexi zayıf {kontrol}')
elif kontrol >= 18.5 and kontrol <= 24.9:
    print(f'Kilo İndexi Normal {kontrol}')
elif kontrol >= 25.0 and kontrol <= 29.9:
    print(f'Kilo İndexi Fazla Kilolu {kontrol}')
elif kontrol >= 30.0 and kontrol <= 34.9:
    print(f'Kilo İndexi Obez {kontrol}')    