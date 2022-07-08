SadıkHesap = {
    'ad' : 'Sadık Turan',
    'hesapNo' : '131245678',
    'bakiye' : 3000,
    'ekhesap' : 2000
}
def paraCek(hesap,para):
    isim = input('İsminizi Giriniz: ')
    hesapNo = input('Hesap no Giriniz: ')
    if isim == hesap['ad'] and hesapNo == hesap['hesapNo']:
        print('Giriş Yapıldı.')

        if para > hesap['bakiye'] + hesap['ekhesap']:
            print('Bakiye Yetersiz')
        elif para <= hesap['bakiye']:
            hesap['bakiye'] = hesap['bakiye'] - para
            print('para çekme işlemi yapılmıştır')
            print('Güncel Bakiyeniz: ' ,hesap['bakiye'])
            print('Güncel ek Hesabınız: ' ,hesap['ekhesap'])
        elif para > hesap['bakiye']:
            kontrol = input('Bakiyenizde Yeterli miktar yoktur ek hesap kullanılsın mı (e/h): ' )
            if kontrol == 'e':
                miktar = hesap['ekhesap'] + hesap['bakiye'] - para
                hesap['bakiye'] = 0
                print(f"Para Çekilmiştir ek hesapta kalan: {miktar}, bakiyede kalan: {hesap['bakiye']}")
            else:
                print('Çıkış Yapıldı.')
    else:
        print('Giriş Başarısız.')
paraCek(SadıkHesap,1000)
                

