vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final = float(input('Final : '))
ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
result = ortalama>= 50 and final>= 50 or final >= 70
print(result,ortalama) 