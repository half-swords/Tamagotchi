from Tamagotchi import Tamagotchi

class Panda(Tamagotchi):
    def __init__(self, name):
        super().__init__(name, hunger=90, joy=70, sickness=0, shape=80, cleanness=75)

    def display_type(self):
        return "Panda"