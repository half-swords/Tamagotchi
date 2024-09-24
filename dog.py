from Tamagotchi import Tamagotchi

class Dog(Tamagotchi):
    def __init__(self, name):
        super().__init__(name, hunger=80, joy=90, sickness=0, shape=85, cleanness=70)

    def display_type(self):
        return "Dog"
