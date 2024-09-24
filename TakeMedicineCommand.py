from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class TakeMedicineCommand(Command):
    def execute(self, tamagotchi):
        if tamagotchi.sickness > 0:
            tamagotchi.sickness -= 20
            print(f"{tamagotchi.name} took medicine and feels better!")
        else:
            print(f"{tamagotchi.name} is not sick!")