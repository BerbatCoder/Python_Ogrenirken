
birler = ['','bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz']
onlar = ['','on','yirmi','otuz','kırk','elli','atmış','yetmiş','seksen','doksan']
yüzler = ['','yüz','ikiyüz','ücyüz','dörtyüz','beşyüz','altıyüz','yediyüz','sekizyüz','dokuzyüz']
binler = ['','bin','ikibin','ücbin','dörtbin','beşbin','altıbin','yedibin','sekizbin','dokuzbin']

sayi = int(input('4 Basamaklı bir sayı giriniz: '))

s = str(sayi)

print(binler[int(s[0])],yüzler[int(s[1])],onlar[int(s[2])],birler[int(s[3])])


