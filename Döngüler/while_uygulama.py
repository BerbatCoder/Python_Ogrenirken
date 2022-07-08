sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
'''
while True:
    print(sayilar)
    break
'''
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
'''
bas = int(input('Başlangıç Değerini Giriniz: '))
bit = int(input('Bitiş Derğerini Griniz: '))
if bas <= bit:
    while True:
        bas += 1
        if bas % 2 == 1:
            print(bas)
        elif bas > bit:
            break

'''



# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
'''
toplam = 100
while toplam > 0:
    toplam -= 1
    print(toplam)

x = int(input('İlk Sayıyı Giriniz : '))
x1 = int(input('ikinci Sayıyı Giriniz : '))
x2 = int(input('üçüncü Sayıyı Giriniz : '))
x3 = int(input('dördüncü Sayıyı Giriniz : '))
x4= int(input('beşinci Sayıyı Giriniz : '))
'''
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.
'''
al = []
kontrol = 0
while kontrol < 5:
    kontrol += 1
    x = int(input('Bir Sayı Giriniz : '))
    al.append(x)
print(al)
'''
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.


urunler = []

adet = int(input('Kaç ürün eklemek istiyorsunuz: '))
i = 0

while (i < adet):
    i += 1
    name = input(f'{i}. Ürün adını Giriniz: ')
    price = input(f'{i}. Ürün Fiyatını giriniz: ')
    urunler.append({
        'name' : name,
        'price' : price
    })
    
for urun in urunler:
    print(f"Ürün adı : {urun['name']}, Fiyatı: {urun['price']}")
