class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu')
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('Film Silindi.')

m = Movie('Film Adı', 'Yönetmen Adı', 120)

print(type(m))
print(str(m))
print(len(m))

# Python daki özel methotları bulmak için internetten yardım alabilirsin.
