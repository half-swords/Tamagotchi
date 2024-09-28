from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class PassTimeCommand(Command):
    def execute(self, tamagotchi):
        tamagotchi.age_tamagotchi()