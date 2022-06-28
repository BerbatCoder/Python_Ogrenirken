# sets dizleri

fruits = {'orange','apple','banana'}
# print(fruits[0]) indexlenemez bunların karakter sayıları yoktur.

for x in fruits:
    print(x)

fruits.add('Çilek')
fruits.update(['Mango','grape'])
print(fruits)

myList = [1,2,3,4,4,2,1]
print(set(myList))
fruits.remove('Mango')
fruits.discard('grape')
