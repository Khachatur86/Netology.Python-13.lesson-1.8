import requests

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
        print("I am eating a ", self.food, ".")  # Разобрался :) Я бы хотел, чтобы не указывая в скобках переменную food
        #  оно работало правильно: оно бы брало food из __init__, возможно ли такое?


"""Class of birds"""


class Birds(Animals):
    def height_of_flight(self, height):
        self.height = height
        print("I can fly an", self.height, "metrs above the Earth.")


"""Class of Artodactils"""


class Artiodactyls(Animals):


    def __init__(self, name, legs, food, distance=0):
        super(Artiodactyls, self).__init__(name, legs, food)
        self.distance = distance

    def distance_of_running(self):
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

cow = Artiodactyls("Buurenka", 4, "grass", 20)
cow.sound("muuu")
cow.display()
cow.distance_of_running()

goat = Artiodactyls("Marta", 4, "grass", 30)
goat.sound("beeeee")
goat.display()
goat.distance_of_running()

sheep = Artiodactyls("Shon", 4, "grass", 40)
sheep.sound("beebee")
sheep.display()
sheep.distance_of_running()

pig = Artiodactyls("Funtic", 4, "acorn", 50)
pig.sound("khrukhru")
pig.display()
pig.distance_of_running()


