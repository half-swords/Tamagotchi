from Tamagotchi import Tamagotchi, Phases

class Dog(Tamagotchi):

    def __init__(self, name):
        self.counter = 0
        self.phase = Phases(self.counter // 180).name
        self.name = name
        self.age = 0
        self.max_joy = 100
        self.current_joy = 100
        self.max_shape = 100
        self.current_shape = 100
        self.max_health = 100
        self.current_health = 100
        self.weight = 20
        self.max_hunger = 100
        self.current_hunger = 100
        self.max_cleanness = 100
        self.current_cleanness = 100
