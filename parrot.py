from Tamagotchi import Tamagotchi, Phases

class Parrot(Tamagotchi):
    def __init__(self, name):
        self.counter = 0
        self.phase = Phases(self.counter // 600).name
        self.name = name
        self.age = 0
        self.max_joy = 80
        self.current_joy = 80
        self.max_shape = 50
        self.current_shape = 50
        self.max_health = 100
        self.current_health = 100
        self.weight = 10
        self.max_hunger = 150
        self.current_hunger = 150
        self.max_cleanness = 60
        self.current_cleanness = 60