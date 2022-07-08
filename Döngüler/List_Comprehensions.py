'''
numbers []
for x in range(10):
    numbers.append(x)
# Basit
numbers = [x for x in range(10)]
print(numbers)
'''
'''
number =  [x**2 for x in  range(10) if x % 3 ==0]
print(number)

strr = 'hellp'
list = []
for x in strr:
    list.append(x)
print(list)

Mystr= 'Hello'
Mylist = [letter for letter in Mystr]
print(Mylist)

years = [1983, 1999, 2008, 1956, 1986]
ages = [2022-year for year in years]
print(ages)

result = [x if x % 2 == 0 else 'tek' for x in range(1,10)]
print(result)

result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)
'''
result = [(x,y) for x in range(3) for y in range(3)]
print(result)