class person:
    # class attributes
    address = 'no information'
    # constructor (Yapıcı Metod)
    def __init__(self, name, years):
        # object attribute
        self.name = name
        self.years = years
        
    # methods
    def intro(self):
        print('hello there ' + self.name)
    
    def calculateAge(self):
        return 2022 - self.years


p1 = person('ali', 1998, )
p2 = person('mehmet', 1995)
print(p1.name, p1.address)
print(p2.intro())
print(f'ismim {p1.name} ve yaşım {p1.calculateAge()}')