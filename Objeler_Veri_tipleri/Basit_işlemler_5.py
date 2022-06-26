website = "http://www.sadikturan.com"
course = "Python kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
print(len(course)) #65
print(website[7:10])
print(website[-3:])
print(course[:15]," , " ,course [-15:])
print(course [::]) # print(course [-65:]) aynı işlevde
print(course [::-1]) #Tüm dizeyi testen okutur 
print(course [24:20:-1]) # baştan 24. karakterden baştan 20.karaktere kadar tesine yazdır.

name , surname , age, job = 'Onur','Doğan','19','Yazılımcı'
print(f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}')

# Hello world ifadesindeki w harfini W olarak değiştiriniz

x = 'Hello world'
x = x[0:6] + 'W' + x[-4:] # 6 Karaktere kadar gel Yanında W koy orld u da yanına koy
print(x)


y= 'abc '
print(y * 3)
