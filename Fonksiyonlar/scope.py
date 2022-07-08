#global scope
from glob import glob
from hashlib import new


x = 'global x'

def function():
    # local scope
    # x = 'local x'
    print(x)
function()
print(x)

######################3

# global
name = 'Çınar'

def changeName(new_game):
    global name
    name = new_game
    print(name)
changeName('Onur')
print(name)

######################3

name = 'global string'

def greeting():
    # name = 'Çınar'

    def hello():
        print('hello' + name)
    
    hello()
greeting()

######################3

x = 50
def test():
    global x
    print(f'x {x}')

    x = 100
    print(f'cganged x to {x}' )
