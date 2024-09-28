import random
import time
from abc import ABC, abstractmethod
from enum import Enum

class Phase(Enum):
    BABY = "baby"
    CHILD = "child"
    TEENAGER = "teenager"
    ADULT = "adult"
    SENIOR = "senior"
    DEAD = "dead"

class Tamagotchi(ABC):
    def __init__(self, name, hunger, joy, sickness, shape, cleanness):
        self.name = name
        self.age = 0
        self.hunger = hunger
        self.joy = joy
        self.sickness = sickness
        self.shape = shape
        self.cleanness = cleanness
        self.phase = Phase.BABY

    @abstractmethod
    def display_type(self):
        pass

    def update_phase(self):
        if self.age < 1:
            self.phase = Phase.BABY
        elif self.age < 3:
            self.phase = Phase.CHILD
        elif self.age < 5:
            self.phase = Phase.TEENAGER
        elif self.age < 10:
            self.phase = Phase.ADULT
        elif self.age < 15:
            self.phase = Phase.SENIOR
        else:
            self.phase = Phase.DEAD

    def age_tamagotchi(self):
        self.age += 1
        self.hunger -= random.randint(8, 20)
        self.joy -= random.randint(8, 20)
        self.shape -= random.randint(8, 15)
        self.cleanness -= random.randint(10, 20)
        if self.hunger < 0 or self.joy < 0 or self.shape < 0 or self.cleanness < 0:
            self.sickness += random.randint(5, 15)
        self.update_phase()

    def is_alive(self):
        return self.phase != Phase.DEAD and self.sickness < 40

    def display_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Type: {self.display_type()}")
        print(f"Age: {self.age} (Phase: {self.phase.value})")
        print(f"Hunger: {self.hunger}")
        print(f"Joy: {self.joy}")
        print(f"Sickness: {self.sickness}")
        print(f"Shape: {self.shape}")
        print(f"Cleanness: {self.cleanness}")
        print("------------------------------")