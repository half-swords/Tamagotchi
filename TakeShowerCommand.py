from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class TakeShowerCommand(Command):
    def execute(self, tamagotchi):
        tamagotchi.cleanness += 20
        tamagotchi.joy -= 5
        print(f"{tamagotchi.name} took a shower.")