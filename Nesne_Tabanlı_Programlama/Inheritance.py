class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastName = lname
        print('Person Created')
    def who_ı_am(self):
        print('Ben Onur bey')
    def eat(self):
        print("Ben Yemek Yiyiorum")



class Student(Person): #Personun sahip olduğu özelliklere sahip olur
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname) # Burada initi fonksiyonunu tekrar alıyor
        print(f'adınız : {fname} Soyadınız {lname} = ') 
    
    # Override Yukardaki porsen classındaki fonksiyonu bastırdı.
    def who_ı_am(self):
        print('Ben Küçük Bey')


class Teacher(Person):
    def __init__(self,fname,lname,alan):
        Person.__init__(self,fname,lname)
        print(f"ı  am a {alan} teacher ")
        



t1 = Student('Onur', 'Dogan', )
t1.who_ı_am()
        