def bul(n,m):
    rem = 0
    for i in range(n,m):
        if i%7==0:
            rem += i
    print('Yediye tam bölünenlerin toplamı=', rem)
bul(1,8)