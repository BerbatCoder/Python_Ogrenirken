'''
# def square(num): return num ** 2
square = lambda num: num ** 2
numbers = [1,2,3,9]
result = list(map(square , numbers))

#for item in map(square, numbers):
 #   print(item)
print(result)
'''
ikikat = lambda x : x * 2
print(ikikat(5))

liste = [1, 2, 3, 4, 5, 6]
yeni_liste = list(filter(lambda x : (x%2==1), liste))
print(yeni_liste)

yeni_liste2 = list(map(lambda x:(x+5),liste))
print(yeni_liste2)