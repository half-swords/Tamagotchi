from Tamagotchi import Tamagotchi, Phases

class Cat(Tamagotchi):

    def __init__(self, name):
        self.counter = 0
        self.phase = Phases(self.counter // 240).name
        self.name = name
        self.age = 0
        self.max_joy = 70
        self.current_joy = 70
        self.max_shape = 70
        self.current_shape = 70
        self.max_health = 100
        self.current_health = 100
        self.weight = 15
        self.max_hunger = 150
        self.current_hunger = 150
        self.max_cleanness = 50
        self.current_cleanness = 50