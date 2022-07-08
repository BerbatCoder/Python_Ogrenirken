# Vize notunun %40 ını, Final notunun %60 ını alarak ortalama 
# notu hesaplayan, ortalama 50 den büyükse 'Geçti' küçükse 'kaldı'

def ortalama(vize,final):
   hesapla = vize*0.40 + final*0.60
   if hesapla >= 50:
        print('Geçtiniz')
   else:
        print('Kaldınız')
ortalama(55,99)