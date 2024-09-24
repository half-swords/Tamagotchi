from Tamagotchi import Tamagotchi

class Parrot(Tamagotchi):
    def __init__(self, name):
        super().__init__(name, hunger=60, joy=80, sickness=0, shape=75, cleanness=85)

    def display_type(self):
        return "Parrot"
