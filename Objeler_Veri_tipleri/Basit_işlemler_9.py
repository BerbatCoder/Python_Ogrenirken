dize = ['Bmw','Mercedes','Opel','Mazda']
#print(dize.len())
#print(dize[0],dize[-1])
#dize[2]="Toyota"
#print(dize)
result = 'Mercedes' in dize
dize[-2:] = "Toyata","Renault"
result = dize + ['Auidi','Nissan']
del dize[-1]
result = dize
result = dize[::-1]
print(result)

studA = ['Yiğit Bilgi 2010',70,60,90]
studB = ['Sena Turan 1999',80,80,70]
studC = ['Ahmet Turan 1998',[80,70,90]]
result = studC[1][1]
user = studA+studB+studC
print(user, result)