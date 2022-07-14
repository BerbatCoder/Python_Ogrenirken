class Circle:
    pi = 3.14
    # Class object attribute
    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    #methods

    def cevrehesap(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
c1 = Circle() # yarıcap = 1
c2 = Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevrehesap()}')
print(f'c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevrehesap()}')
