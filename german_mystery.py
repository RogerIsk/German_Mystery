from stringcolor import cs
import time

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

# Introduction text
intro = '''The employment agency asks you to submit the same document for the 10th time - so you go to the office in a rage to resolve the matter once and for all.

When you arrive at the office, you find yourself standing in an empty hall with not a soul around and wonder where your point of contact might be. You think about where you are most likely to find someone who can help you with your matter. '''
# short break after intro
def main():
    printc(intro, "blue")
    time.sleep(3)
    start()

# Start of the actual game
def start():
    print("\nWhat do you do?")
    while True:
        print("\n1. you take the elevator")
        print("2. you take the stairs")
        print("3. you are waiting in the hall until you met a member of staff")
        choice = input("\nYour choice: ")
        if choice == '1':
            elevator()
        elif choice == '2':
            stairs()
        elif choice == '3':
            hall()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)

# If you take the elevator
def elevator():
    print("\nSo you chose the path of lazy people. You gathered your courage and walked over to the elevator call button.")
    print("You press the button with a shaky hand.")
    print("The whole building trembled slightly, and through this noise you hear a voice saying:")
    printc("Who are you, warrior?", "red")
    time.sleep(0.5)
    printc("\nWhat will you do:", "yellow")

# If you take the stairs
def stairs():
    print("\nAs you move towards the stairs, you notice a dark shadow standing at the top of the stairs.")
    print("You can't make out its exact outline, but you can feel it staring at you and it makes you feel uncomfortable!")
    time.sleep(0.5)
    print("\nDo you want to continue up the stairs?")
    while True:
        print("\n1. you take the elevator")
        print("2. you take the stairs")
        print("3. you are waiting in the hall until you met a member of staff")
        choice = input("\nYour choice: ")
        if choice == '1':
            stairs_up()
        elif choice == '2':
            print("You turn back into the Main Hall.")
            start()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)

#game over if you wait too long
def gameover_hall():
    print("\nYou turn back into the Main Hall.")
    time.sleep(2)
    print("\n[you are waiting in the hall until you met a member of staff]")
    time.sleep(5)
    print("\nYou've been waiting unnecessarily for 3 hours for something to happen. The employment agency closes for the day.")
    printc("GAME OVER", "red")

if __name__ == "__main__":
    main()