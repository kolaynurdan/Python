class Movie():
    def __init__(self, title, director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie obeject was created.')

    def __str__(self):
        return f"{self.title} by {self.director}"

m = Movie('Movie: ', 'Director: ', 'Duration: ')

print(str(m))