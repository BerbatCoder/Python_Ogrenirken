def buk(isten):
    a,b,c = 1,1,0
    while c < isten:
        print(b)
        c = a + b
        a = b
        b = c
buk(5000)
