import time
from EatSnackCommand import EatSnackCommand
from SleepCommand import SleepCommand
from TakeMedicineCommand import TakeMedicineCommand
from TakeShowerCommand import TakeShowerCommand
from PassTimeCommand import PassTimeCommand
from PlayCommand import PlayCommand
from CreateTamagotchi import CreateTamagotchi
from Tamagotchi import Tamagotchi
from dog import Dog

def main():
    tamagotchi_creator = CreateTamagotchi()
    tamagotchi = tamagotchi_creator.Create_Pet()
    tamagotchi.display_status()
    commands = {
        '1': EatSnackCommand(),
        '2': SleepCommand(),
        '3': TakeShowerCommand(),
        '4': TakeMedicineCommand(),
        '5': PlayCommand(),
    }

    actions = 0
    while tamagotchi.is_alive():
        action = input("Choose an action: 1.Eat Snack 2.Sleep 3.Take Shower 4.Take Medicine 5.Play 6.Quit: ")

        if action in commands:
            commands[action].execute(tamagotchi)
            tamagotchi.display_status()
            actions+=1
        elif action == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
        if actions % 2 == 0:
            PassTimeCommand().execute(tamagotchi)
        time.sleep(1)

    print(f"{tamagotchi.name} has passed away. Game over!")

if __name__ == '__main__':
    main()