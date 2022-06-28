"""
bir = input("1.Sayı Giriniz: ")
iki = input("2.Sayı Giriniz: ")
toplam = bir > iki
print ("'True : 1. Sayı Büyüktür' , 'False : 2.Sayı Büyüktür.'  Değer : ", toplam)


toplam = ((60 + 40) // 2) >= 50 
print(toplam)

bir = int(input("1.Sayı Giriniz: "))
tekmicift = (bir % 2) == 0
print(tekmicift)
"""
bir = int(input("1.Sayı Giriniz: "))
pozifit = bir > 0 
print(f'sayının pozitid olma durumu {pozifit}')

e_mail = input("E mail giriniz  : ")
parola = input('Parola Giriniz  : ')
dogrumu = ('mailonurdogan@mail.com' == e_mail) & ('abc123' == parola)