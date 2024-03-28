from stringcolor import cs
import time

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

intro = ''' The employment agency asks you to submit the same document for the 10th time - so you go to the office in a rage to resolve the matter once and for all.

When you arrive at the office, you find yourself standing in an empty hall with not a soul around and wonder where your point of contact might be. You think about where you are most likely to find someone who can help you with your matter. '''

def main():
    printc(intro, "blue")
    time.sleep(3)
    start()
    
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

# If you bang on the door
def hall():
    print("\nYou bang loudly on the door. You hear some metallic clinking as a grumpy voice shouts from the other side:")
    time.sleep(1)
    printc("\n'What the fuck is going on? Shut the fuck up or I'll make you!'", "red")
    time.sleep(0.5)
    print("\nWhat do you do?")
    while True:
        print("\n1. Bang louder")
        print("2. 'Oh, sorry! I won't do it again'")
        print("3. 'Please, can you help me?? My precious golden ring rolled to a corner and I can't find it. :('")
        choice = input("\nYour choice: ")
        if choice == '1':
            bang_door()
        elif choice == '2':
            start()
        elif choice == '3':
            lost_ring()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)

# If you lure the guard into believing you have a golden ring to seize
def lost_ring():
    print("\nA short silence.")
    time.sleep(1)
    print("You hear a key rotating in the lock. The voice says:")
    printc("\n'Alright, but no funny stuff! I'm armed and I'm a tough one!'", "red")
    time.sleep(0.5)
    print("\nWhat do you do?")
    while True:
        print("\n1. Nothing")
        print("2. Hide behind the door")
        print("2. Hide against the wall on the other side of the door")
        choice = input("\nYour choice: ")

        """
        if choice == '1':
            bang_door()
        elif choice == '2':
            start()
        elif choice == '3':
            lost_ring()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)
            """

if __name__ == "__main__":
    main()