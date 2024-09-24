from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class SleepCommand(Command):
    def execute(self, tamagotchi):
        tamagotchi.joy += 10
        tamagotchi.cleanness -= 5
        print(f"{tamagotchi.name} took a nap.")
