#Identity Operator: is 

x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()

print(x == y)
print(x is y)

# Membership Operator: in

x = ['Banana','apple']
print('Banana' in  x)

namea = 'Çınar'
print('a' in namea)