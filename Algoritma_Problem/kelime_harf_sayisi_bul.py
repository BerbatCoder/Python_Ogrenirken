deg = input('Cümle Gir: ')
ayrı = deg.split(' ')
print(f"kelime sayısı: {len(ayrı)}")
print(f"harf sayısı: {len(deg)-(len(ayrı)-1)}")
