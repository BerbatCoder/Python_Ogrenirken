# ikinci dereceden ax^2 + bx + c = 0 denkleminin diskriminant çözümünü yapınız.
# Kullanıcıdan a,b ve c değerlerini alarak deltayı hesaplayınız.
# Bu program tamamlanmadı 



from cmath import sqrt
# Delta 


def dikrim(a,b,c):
    delta = b**2-4*a*c
    if delta>0:
        x = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a
        print(f'Girdiğiniz sayıların diskrimantı {x} , {x2}')
dikrim(int(input('A Sayısını giriniz : ')) , int(input('B Sayısını giriniz : ')), int(input('C Sayısını giriniz : ')))
