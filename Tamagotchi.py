from abc import ABC, abstractmethod
from enum import Enum

class Phases(Enum):
    BABY = 0
    CHILD = 1
    TEENAGER = 2
    ADULT = 3
    SENIOR = 4
    SPECIAL = 5

class Tamagotchi(ABC):
   
    @abstractmethod
    def __init__(self, name):
        pass

