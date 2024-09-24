from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class EatSnackCommand(Command):
    def execute(self, tamagotchi):
        if tamagotchi.hunger < 100:
            tamagotchi.hunger += 10
            tamagotchi.joy += 5
            print(f"{tamagotchi.name} ate a snack.")
        else:
            print(f"{tamagotchi.name} is not hungry!")