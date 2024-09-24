from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, tamagotchi):
        pass
