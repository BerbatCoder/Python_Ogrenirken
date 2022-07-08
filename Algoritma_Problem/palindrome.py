# Girilin sayıların testen yazıldığında aynı değeri vermesi 
# 34543 tesrten yazıldığında aynı derğeri verir bunun gibi
# 1000 ve 100000 arasındaki palindrome sayıları buldur


def ayar():
    for i in range(1000,100000):
        s = str(i)
        t = s[::-1]
        if s == t:
            print(s)
ayar()