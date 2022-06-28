"""
if 3>2:
    print('Hoşgeldün')
else:
    print('Çalışmadı la ')

users = input('User Griniz : ')
password = int(input('Password : '))

if (users == 'Sadik'):
    print("Kullanıici adını doğru girdiniz")
    if(password == 1234):
        print('Hoşgeldiniz')
    else:
        print('Şifre Yanlış')
else:
    print('kullanıcı ya da parola yanlış')
"""
username = input ('Kullanıcı Adını Gir : ')
if username == 'sadikturan':
    print('*'* 50)
    print('Kullanıcı Adı Doğru')
    print('*'* 50)
    password = input ('Şifreni Gir : ')
    if password == '1234':
        print(f'Şifre De Doğru Hoşgeldin "{username}"')
    else:
        print('Şifre Yanlış girildi.')
else:
    print('Kullanıcı yada şifre yanlış ')