from stringcolor import cs
import time

#---------FUNCTIONS-----------------------------------------------------

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def start():
    print("""The Agentur für Arbeit asks you to submit the same document for the 10th time - so you go to the office in a rage to resolve the matter once and for all.

When you arrive at the office, you find yourself standing in an empty hall with not a soul around and wonder where your point of contact might be. You think about where you are most likely to find someone who can help you with your matter.""")
    print("""There are 3 options available to you:""")
    option_1 = "You take the elevator"
    option_2 = "You take the stairs"
    option_3 = "You are waiting in the hall until you met a member of staff"
    #printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        #print('''  ''')
        take_elevator()
    elif decision in ["2",option_2]:
        #print('')
        take_stairs()
    elif decision in ["3",option_3]:
        #print('')
        waiting_staff()

def take_elevator():
    print("""So you chose the path of lazy people. You gathered your courage and walked over to the elevator call button. You press the button with a shaky hand. The whole building trembled slightly, and through this noise you hear a voice saying: who are you, warrior?""")
    print("""What will you do:""")
    option_1 = "Wait for the elevator"
    option_2 = "You will use the stairs"
    #option_3 = "..........option 3........."
    # posible optointo type
    option_1_p = "wait"
    option_2_p = "stairs"
    
    printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower(), option_1_p, option_2_p]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1], option_1_p:
        print('''  ''')
        waiting_elevator()
    elif decision in ["2",option_2, option_2_p]:
        print('')
        take_stairs()

############### DEF IS EMPTY #######################################################################################
def waiting_elevator():
    print("""  """)
    print("""  """)
    option_1 = "......option 1 ......"
    option_2 = ".....option 2......."
    #option_3 = "..........option 3........."
    printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        print('''  ''')
        return ""
    elif decision in ["2",option_2]:
        print('')
        return ""
    elif decision in ["3",option_3]:
        print('')
        return ""

def take_stairs():
    print("""As you move towards the stairs, you notice a dark shadow standing at the top of the stairs. You can't make out its exact outline, but you can feel it staring at you and it makes you feel uncomfortable!""")
    print("Do you want to continue up the stairs?")
    option_1 = "Yes"
    option_2 = "No"
    #option_3 = "..........option 3........."
    #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower(), "y","n"]:
        printc("INVALID INPUT, please choose between:.","red")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1","yes","y"]:
        print('''You continue up the stairs, as you get closer and closer to the shadow, you feel your heart beating faster and faster and the presence of this shadow makes you feel very uncomfortable, but in the blink of an eye the shadow disappears before you reach the top of the stairs.
Confused and worried, you ask yourself "Was that just my imagination? What could possibly happen to me here?" ''')
        1.floor()
    elif decision in ["2","no","n"]:
        print('You turn back into the Main Hall.')
        main_hall()

############### DEF IS EMPTY #######################################################################################
def waiting_staff():
    print("""  """)
    print("""  """)
    option_1 = "......option 1 ......"
    option_2 = ".....option 2......."
    #option_3 = "..........option 3........."
    printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        print('''  ''')
        return ""
    elif decision in ["2",option_2]:
        print('')
        return ""
    elif decision in ["3",option_3]:
        print('')
        return ""

############### DEF IS EMPTY #######################################################################################
def main_hall():
    print("""You are back in the main hall.""")
    print("""There are 3 options available to you:""")
    option_1 = "You take the elevator"
    option_2 = "You take the stairs"
    option_3 = "You are waiting in the hall until you met a member of staff"
    #printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        #print('''  ''')
        take_elevator()
    elif decision in ["2",option_2]:
        #print('')
        take_stairs()
    elif decision in ["3",option_3]:
        #print('')
        waiting_staff()
def 1.floor():
    print("""You are now standing in a corridor where you can see a door to the left, right and in front of each one, which door do you go in?  """)
    option_1 = "Left"
    option_2 = "Front"
    option_3 = "Terminal"
    #printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        #printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        print('''You slowly open the door and hear a soft rustling sound, it sounds like someone is shuffling through papers. Between piles of paper is a very stressed and nervous employee of the Agentur für Arbeit. "Excuse me, please..." you say quietly into the office. The counselor looks at you in horror and under stress he shouts in your direction "All my colleagues are sick, I have to do all the paperwork for them - please go to office 204, above us" and slams the door from the inside.  ''')
        office_204()
    elif decision in ["2",option_2]:
        print('A big Potato comes out of the shadows and dragg you into the darkness. You died, what did you expect.')
        # END *******************************************************************************************************************
    elif decision in ["3",option_3]:
        print('.............')
        # call def

############### DEF IS EMPTY #######################################################################################
def office_204():
    print("""  """)
    print("""  """)
    option_1 = "......option 1 ......"
    option_2 = ".....option 2......."
    #option_3 = "..........option 3........."
    printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        print('''  ''')
        return ""
    elif decision in ["2",option_2]:
        print('')
        return ""
    elif decision in ["3",option_3]:
        print('')
        return ""
    
def name():
    print("""  """)
    print("""  """)
    option_1 = "......option 1 ......"
    option_2 = ".....option 2......."
    #option_3 = "..........option 3........."
    printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
    #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2, "cyan")
        #printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()
    
    if decision in ["1",option_1]:
        print('''  ''')
        return ""
    elif decision in ["2",option_2]:
        print('')
        return ""
    elif decision in ["3",option_3]:
        print('')
        return ""



#---------END OF FUNCTIONS-----------------------------------------------

print("Welcome to the German mystery")
name = input("Choose your character's name: ")
printc("Hi "+name+", let's start.", "blue")
printc("------------------------", "yellow")

start()


