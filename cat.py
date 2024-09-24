from Tamagotchi import Tamagotchi

class Cat(Tamagotchi):
    def __init__(self, name):
        super().__init__(name, hunger=70, joy=100, sickness=0, shape=80, cleanness=90)

    def display_type(self):
        return "Cat"
