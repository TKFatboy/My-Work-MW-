class Movie():

    def __init__(self, title, genre, director, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.actors = []
        self.actors.append(actors)

    def show(self):
        print(self.title)
        print(self.genre)
        print(self.director)
        print(self.actors)

class Actor():

    def __init__(self, name, filmography, movies):
        self.name = name
        self.filmography = filmography
        self.movies = []
        self.movies.append(movies)

    def show(self):
        print(self.name)
        print(self.filmography)
        print(self.movies)

print("Movie List")
movie1 = Movie("Spider-Man Homecoming", "Superhero", "Jon Watts", "Tom Holland")
movie2 = Movie("Sherlock Holmes", "Action", "Guy Ritchie", "Robert Downey Jr.")
movie3 = Movie("Pirates of the Caribbean: The Curse of the Black Pearl", "Adventure", "Gore Verbinski", "Johnny Depp")
movie1.show()
movie2.show()
movie3.show()

print("Actor List")
actor1 = Actor("Margot Robbie", "Barbie", "Suicide Squad")
actor2 = Actor("Cillian Murphy", "Oppenheimer", "Peaky Blinders")
actor3 = Actor("Will Smith", "Bad Boys", "MIB")
actor1.show()
actor2.show()
actor3.show()