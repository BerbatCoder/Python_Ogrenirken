sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?
'''
for al in sayilar:
    if al % 3 == 0:
        print(f'"{al}" Bu sayı 3 ün katıdır')
'''

# 2- Sayilar listesinde sayıların toplamı kaçtır ?
'''
x = []
for al in sayilar:
    x.append(al)
print(sum(x))

toplam = 0 
for sayi in sayilar:
    # toplam = toplam + sayi
    toplam += sayi
    print('toplam' ,toplam) 
'''
# 3- Sayilar listesindeki tek sayıların karesini alınız.
'''
for n in sayilar:
    x = n % 2 == 1
    if x == True:
        karesi = n**2
        print(f'{n} sayısının karesi {karesi} dir')


'''

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
'''
for n in sehirler:
    x = len(n)
    if x == 5:
        print(n)
'''

urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?
'''
toplam = 0 
for urun in urunler:
    toplam += int(urun['price'])
print(toplam)    
'''
# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name']) 