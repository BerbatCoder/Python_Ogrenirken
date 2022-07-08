# Map , Filter ve Reduce 
# Map dizi elamanlarının tamamına uygulanacak işlemlerde kullanılır.

liste = [2,5,6,7,9]
yeni_liste = list(map(lambda x:x**2,liste))
print(yeni_liste)

def ikiKat(x):
    return x*2

def yari(x):
    return x/2

fonk = [ikiKat, yari]

for i in range(5):
    deger = list(map(lambda x:x(i),fonk))
    print(deger)

# Filter dizi elamanlarının seçiknesinde kullanılır 

liste = [1,5,6,9,16,27,45,46]
uce_bolunenler = list(map(lambda x:x%3==0,liste))
print(uce_bolunenler)

#reduce dizi elamlarının toplanmasını, çapılması gibi işlemlerde kullanılır
from functools import reduce
toplam = reduce(lambda x,y:x+y,liste)
print(toplam)