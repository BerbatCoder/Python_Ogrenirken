numbers = [1 , 5 ,10 ,20 ,50]
letters = ['a', 'g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[::2]

numbers[2] = 2

numbers.append(49) # Listenin sonuna ekle
numbers.insert(3,45) # 3. Karakterden sonra 45 ekle
numbers.pop(-1) #Sondaki yada verilen elemanı sil 
numbers.remove(20) # Veriyi bul ve sil 
numbers.sort() # sayısal olarak sırala
letters.sort() # Alfabetik olarak sırala
numbers.reverse() # Listeyi tersine çevirir
numbers.count(10) # numbersın içinde 10 Kaç tane var 
letters.clear() # Temizleme Metodu 
print(letters)