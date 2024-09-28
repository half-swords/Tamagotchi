from cat import Cat
from dog import Dog
from parrot import Parrot
from panda import Panda

class CreateTamagotchi():
    def Create_Pet(self):
        name = input("Enter your Tamagotchi's name: ")
        while True:
            print("Types: 1.Dog 2.Cat 3.Parrot 4.Panda")
            choice = input("Enter the number of your choice: ")
            types = {
                '1': Dog,
                '2': Cat,
                '3': Parrot,
                '4': Panda
            }
            if choice in types:
                return types[choice](name)
                break
            else:
                print("Invalid choice, try again")


