from ast import arg


def changeName(n):
    n = 'ada'
name = 'Yiğit'
changeName(name)
print(name)

def change(n):
    n[0] = 'İstanbul'
sehirler = ['Ankara','İzmir']
n = sehirler[:] #slicing
n[0] = 'İStanbul'
change(sehirler)

def add(a,b):
    return sum((a,b))
print(add(10,20))

def ett(*param):
    return sum(param)
print(ett(15,20,50))

def displayerUser(**args):
    for key, value in args.items():
        print('{} is {}'.format(key,value))
displayerUser (user = 'Çınar', age= 2, city='Bursa')
displayerUser (user = 'Onur', age = 12,city = 'İstanbul', phone = '45454545')
