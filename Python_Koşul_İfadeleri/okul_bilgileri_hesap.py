isim = input('İsminizi giriniz : ')
sin1 = int(input('1. Yazılı Sınavının Değerleri : '))
sin2 = int(input('2. Yazılı Sınavının Değerleri : '))
soz = int(input('Sözlü notunutuzu giriniz : '))

ortalama = (sin1 + sin2 + soz) // 3

print('*'*50)
print(f'{isim} adlı öğrenci aldığı puan : {ortalama}')

if (ortalama < 24) and (ortalama >=0):
    print('Karne Notu : Sıfır') 
if ortalama < 44 and (ortalama >=25):
    print('Karne Notu : Bir')
if ortalama < 54 and (ortalama >=45):
    print('Karne Notu : İki')
if ortalama < 69 and (ortalama >=55):
    print('Karne Notu : Üç')
if ortalama < 84 and (ortalama >=70):
    print('Karne Notu : Dört')
if ortalama < 100 and (ortalama >=85):
    print('Karne Notu : Beş')
