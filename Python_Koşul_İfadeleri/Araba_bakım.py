import datetime
gun  = input('Aracınız En son bakımdan sonra ne zaman trafiğe Çıktı (Yıl-ay-gün) : ')
gun = gun.split('-')
trafikCık = datetime.datetime(int(gun[0]),int(gun[1]),int(gun[1]))
simdi = datetime.datetime.now()
hesap = simdi - trafikCık
days = hesap.days
if days <= 365:
    print('1.Servis Aralığı')
elif days > 365 and days <=365*2:
    print('2.Servis Aralığı')
elif days > 365*2 and days <= 365*3:
    print('3.Servis Aralığı')
else:
    print('Hatalı Süre')

