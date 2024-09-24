    def main():
        tamagotchi = create_tamagotchi()

        commands = {
            '1': EatSnackCommand(),
            '2': SleepCommand(),
            '3': TakeShowerCommand(),
            '4': TakeMedicineCommand(),
            '5': PassTimeCommand(),
        }

        while tamagotchi.is_alive():
            tamagotchi.display_status()
            action = input("Choose an action: 1. Eat Snack 2. Sleep 3. Take Shower 4. Take Medicine 5. Pass Time 6. Quit: ")

            if action in commands:
                commands[action].execute(tamagotchi)
            elif action == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

            time.sleep(1)

        print(f"{tamagotchi.name} has passed away. Game over!")


    if __name__ == "__main__":
        main()