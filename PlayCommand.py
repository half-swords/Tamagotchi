from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class PlayCommand(Command):
    def execute(self, tamagotchi):
        tamagotchi.joy += 10
        tamagotchi.shape += 10
        tamagotchi.cleanness -= 15
        print(f"{tamagotchi.name} played a game.")