from multiprocessing.sharedctypes import Value


numbers = [1,2,3,4,5]

for num in numbers:
    print(num)

names = ['Çınar' , 'Onur', 'Sadık']

for name in names:
    print(f'My name is {name}')

tuple = [(1,2),(3,4),(5,6)]
for n,c in tuple:
    print(n)

d = {'k1':1, 'k2':2, 'k3':3}
for k,value in d.items():
    print(k,value)