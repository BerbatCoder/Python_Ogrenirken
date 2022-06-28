"""
x,y,z = 5,10 ,20

x += 5 # x + 5 demek
x -= 5 # x - 5 demek
x *= 5 # x * 5 demek
x /= 5 # x / 5 demek
x %= 5 # x % 5 yani kalanı bul demk
x //= 5 # x // 5 tam bolümü yani intager değeri alır
x **= 5 # x ** 5 üsünü alır
"""
values = 1,2,3,4,5

print(values)
print(type(values))

x, y, *z = values
print(x,y,z)
print(x,y,z[2])