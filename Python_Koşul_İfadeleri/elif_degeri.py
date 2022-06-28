"""
x = int(input('x: '))
y = int(input('y: '))

if x > y:
    print('x y den büyük')
elif x == y:
    print('x y eşit')
else:
    print('y x den büyük')
"""

num = int(input('Bir sayı giriniz : '))
if num > 0:
    print(f'Girdiğiniz sayı {num} Pozitiftir')
elif num < 0:
    print(f'Girdiğiniz sayı {num} Negatiftir')
else:
    print(f'Girdiğiniz sayı {num} Sıfıra Eşittir')