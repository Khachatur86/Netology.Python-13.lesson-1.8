import requests

req = requests.get('https://yahoo.ru')


class Animals():
    """Common class of animals"""

    def __init__(self, name, legs, food):
        self.name = name
        self.legs = legs
        self.food = food

    def sound(self, voice):
        self.voice = voice
        print("I cry", self.voice, ".")

    def display(self):
        print("I am eating a ", self.food, ".")


"""Class of birds"""


class Birds(Animals):
    def height_of_flight(self, height):
        self.height = height
        print("I can fly an", self.height, "metrs above the Earth.")


"""Class of Artodactils"""


class Artiodactyls(Animals):
    def distance_of_running(self, distance):
        self.distance = distance
        print("I can run a:", self.distance, "miles.")


duck = Birds("Donald", 2, "worm")
duck.sound("kryakrya")
duck.display()
duck.height_of_flight(1700)

hen = Birds("Petya", 2, "bread crumbs")
hen.sound("kukareku")
hen.display()
hen.height_of_flight(10)

goose = Birds("Seriy", 2, "bread crumbs")
goose.sound("gagaga")
goose.display()
goose.height_of_flight(15)

cow = Artiodactyls("Buurenka", 4, "grass")
cow.sound("muuu")
cow.display()
cow.distance_of_running(10)

goat = Artiodactyls("Marta", 4, "grass")
goat.sound("beeeee")
goat.display()
goat.distance_of_running(17)

sheep = Artiodactyls("Shon", 4, "grass")
sheep.sound("beebee")
sheep.display()
sheep.distance_of_running(9)

pig = Artiodactyls("Funtic", 4, "acorn")
pig.sound("khrukhru")
pig.display()
pig.distance_of_running(30)
