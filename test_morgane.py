from stringcolor import cs
import time

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def main():
    print("You wake up in a dirty cell.")
    start()


def start():
    print("\nWhat do you do?")
    while True:
        print("\n1. Look around")
        print("2. Try to lockpick the door")
        print("3. Bang on the door")
        choice = input("\nYour choice: ")
        if choice == '1':
            look_cell()
        elif choice == '2':
            lockpick()
        elif choice == '3':
            bang_door()
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)

# If you look around the cell
def look_cell():
    print("\nIt's just a dirty cell with a small window, too small for you to get through.")
    print("Nothing to see here.")

# If you try to lockpick the door   
def lockpick():
    print("\nThe lock is sturdy and you don't have any tool.")
    print("Looks like you won't open it.")

# If you bang on the door
def bang_door():
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