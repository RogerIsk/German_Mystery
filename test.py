import random
def main():
    print("Welcome to the creepy adventure in Germany!")
    print("You find yourself in an ancient castle, and the door has closed behind you.")
    print("You hear a noise downstairs. What will you do?")
    while True:
        print("\nChoose your action:")
        print("1. Proceed further down the corridor.")
        print("2. Turn back.")
        print("3. Escape through the window.")
        choice = input("Your choice: ")
        if choice == '1':
            continue_journey()
        elif choice == '2':
            go_back()
        elif choice == '3':
            escape_through_window()
        else:
            print("Invalid choice. Please try again.")
def continue_journey():
    print("\nYou decide to proceed further down the corridor.")
    print("But suddenly, in front of you appears a rainbow of gnomes!")
    print("They are laughing and offer you a choice:")
    print("1. Join the merry company.")
    print("2. Pass by them avoiding the rainbow.")
    choice = input("Your choice: ")
    if choice == '1':
        print("\nYou join the gnomes and have the most fun party of your life!")
    elif choice == '2':
        print("\nYou decide not to risk it and pass by the gnomes.")
        print("They let you through, but as you walk away, you hear laughter behind your back.")
def go_back():
    print("\nYou decide to turn back.")
    print("But the door has closed, and you can't open it.")
    print("You start frantically searching for an exit.")
    if random.choice([True, False]):
        print("\nYou find a secret lever and open the door!")
    else:
        print("\nUnfortunately, you find no secret doors, and now it seems you're stuck.")
def escape_through_window():
    print("\nYou decide to try to escape through the window.")
    print("But it's closed with a giant metal grid.")
    print("You search for a way to open the grid.")
    if random.choice([True, False]):
        print("\nYou manage to find a hiding spot with a key, and you unlock the grid!")
    else:
        print("\nUnfortunately, you don't find the key, and now you'll have to look for another way out.")
if __name__ == "__main__":
    main()