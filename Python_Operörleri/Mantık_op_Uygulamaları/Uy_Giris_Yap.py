email = 'eposta@gmail.com'
sifre = '1234'
e_mail = input('E posta Adınızı Giriniz : ')
p_ssw = input('Şifrenizi Giriniz : ')
dogrula = (e_mail == email) and (p_ssw == sifre)
print('*'*50)
print(f'Giriş Yapıldı  : {dogrula}')