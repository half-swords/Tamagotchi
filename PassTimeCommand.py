from Tamagotchi import Tamagotchi
from abc import ABC, abstractmethod
from Command import Command

class PassTimeCommand(Command):
    def execute(self, tamagotchi):
        tamagotchi.age_tamagotchi()

    def create_tamagotchi():
        name = input("Enter your Tamagotchi's name: ")
        print("Choose a type: 1. Dog 2. Cat 3. Parrot 4. Panda")
        choice = input("Enter the number of your choice: ")
        types = {
            '1': Dog,
            '2': Cat,
            '3': Parrot,
            '4': Panda
        }
        tamagotchi_class = types.get(choice, Dog)
        return tamagotchi_class(name)
