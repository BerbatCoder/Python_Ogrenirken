'''
for item in range(10,100,10):
    print(item)
print(list(range(10,100,10)))
'''

'''
degisken = 'Hello'
index = 1
for i in degisken:
    print(f'sayı : {index}, obje : {degisken[index]}')
    index += 1 
'''
'''
# Yukardaki kodu daha basit şekilde yapmak için enumerate
degisken = 'hello'
for index,letter in enumerate(degisken):
    print(f'index : {index} , letter : {letter}')
'''
liste = [1,2,3,4,5]
liste2 = ['a','b','c','d','e']
liste3 = [100,200,300,400,500]

for item in zip(liste,liste2,liste3):
    print(item)
for sayi,mayi,farkı in zip(liste,liste2,liste3):
    print(mayi)