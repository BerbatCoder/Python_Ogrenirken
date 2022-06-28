#list = ['Onur' , 'Doğan' , 'Nedir bu çile']
#  *** tuple = ('Bu' , 'liste', 'Güncellenemez')
# Dize ve tuple arasındaki fark güncelleme yani herhangi bir veriyi değiştiremezsin 

# Dictionary listesi  

#sehirler = ['kocaeli', 'istanbul']
#plakalar = [41, 34]

#print(plakalar[sehirler.index('istanbul')])
"""
users = {
    'OnurDoğan':{
        'age':36,
        'roles':['Admin','user'],
        'email':'jame@gmail.com',
        'Address':'Bursa',
        'phone': '21321231'
    },
    'cınarturan':{
        'age':36,
        'roles':['user'],
        'email':'jame@gmail.com',
        'Address':'Bursa',
        'phone':'21321231'
    }
}
print(users['OnurDoğan']['roles'])


"""
ogrenciler = {

}
ad = input('Adınızı Giriniz : ')
num = input('Numaranızı Giriniz : ')
soy = input('Soyadınızı Giriniz : ')
tel = input('Telefonu   Giriniz : ')
"""
ogrenciler[num] = {
    'ad': ad,
    'soyad':soy,
    'tel':tel
}
"""
ogrenciler.update({
    num:{
        'ad':ad,
        'soyad':soy,
        'telefon':tel,
    }
})
print('*'*50)
ogno = input('öğrenci no : ')
ogrenci = ogrenciler[num]
print(f"Aradığınız {ogno} nolu Öğrenci adı :{ogrenci['ad']} , soyadı: {ogrenci['soyad']} , telefon: {ogrenci['telefon']} Budur.")

