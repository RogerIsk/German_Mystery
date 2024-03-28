from stringcolor import cs
import time
#--------- TEXT -----------------------------------------------------
text_start = """The Agentur für Arbeit asks you to submit the same document for the 10th time - so you go to the office in a rage to resolve the matter once and for all.

When you arrive at the office, you find yourself standing in an empty hall with not a soul around and wonder where your point of contact might be. You think about where you are most likely to find someone who can help you with your matter.
There are 3 options available to you:"""
text_start_options = """1. You take the elevator
2. You take the stairs
3. You are waiting in the hall until you met a member of staff"""
start_option_1 = ['1','you take the elevator','take elevator','elevator']
start_option_2 = ['2','You take the stairs','take stairs','stairs']
start_option_3 = ['3','You are waiting in the hall until you met a member of staff','wait','waiting']

text_elevator = """So you chose the path of lazy people. You gathered your courage and walked over to the elevator call button. You press the button with a shaky hand. The whole building trembled slightly, and through this noise you hear a voice saying: who are you, warrior?
What will you do:"""
text_elevator_options = """1.  wait for the elevator
2.  you will use the stairs"""
elevator_option_1 = ['1','wait for the elevator','wait','elevator']
elevator_option_2 = ['2','you will use the stairs','use stairs','stairs']
elevator_option_3 = []
text_waiting_elevator = """The elevator call button easily and gently yielded to the pressure of your finger. The elevator doors opened and your feet automatically took you there. A very strange feeling. Softly and easily, the elevator took you to another floor. The door opened and you found yourself in the corridor"""

text_stairs = """As you move towards the stairs, you notice a dark shadow standing at the top of the stairs. You can't make out its exact outline, but you can feel it staring at you and it makes you feel uncomfortable!
Do you want to continue up the stairs?"""
text_stairs_options = """1. Yes
2. No"""
stairs_option_1 = ['1','yes','y']
stairs_option_2 = ['2','no','n']
stairs_option_3 = []
text_stairs_yes = """You continue up the stairs, as you get closer and closer to the shadow, you feel your heart beating faster and faster and the presence of this shadow makes you feel very uncomfortable, but in the blink of an eye the shadow disappears before you reach the top of the stairs.
Confused and worried, you ask yourself "Was that just my imagination? What could possibly happen to me here?" """
text_stairs_no = """You turn back into the Main Hall."""

#--------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#text_waiting_staff = """[waiting_staff]"""
#text_waiting_staff_options = """XXX"""
#waiting_staff_option_1 = ['1']
#waiting_staff_option_2 = ['2']
#waiting_staff_option_3 = ['3']

text_floor1 = """You are now standing in a corridor where you can see a door to the left, right and in front of each one, which door do you go in?"""
text_floor1_options = """1. Left
2. Front
3. Terminal"""
floor1_option_1 = ['1','left','l']
floor1_option_2 = ['2', 'front','f']
floor1_option_3 = ['3','terminal','t']
text_floor1_left = """You slowly open the door and hear a soft rustling sound, it sounds like someone is shuffling through papers. Between piles of paper is a very stressed and nervous employee of the Agentur für Arbeit. "Excuse me, please..." you say quietly into the office. The counselor looks at you in horror and under stress he shouts in your direction "All my colleagues are sick, I have to do all the paperwork for them - please go to office 204, above us" and slams the door from the inside."""
text_floor1_front = """A big Potato comes out of the shadows and dragg you into the darkness. You died, what did you expect."""
text_floor1_terminal =""" XXXX """ #--------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#--------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
text_office_204 = """You are in the manager's office. There you find a strange machine. It looks like a machine that turns people into potatoes... that's strange. But maybe that's why no one works at the Agentur für Arbeit and you've only seen one person in the whole building.
Out of nowhere
A katana pierces through you from behind - it's the final boss Potatoman. You've lost your right to benefits. The Robo... I mean the Potatoes won."""
text_office_204_options = """XXX"""
office_204_option_1 = ['1']
office_204_option_2 = ['2']
office_204_option_3 = ['3']

#--------- FUNCTIONS -----------------------------------------------------

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def ask_name():
    print("Welcome to the German mystery")
    name = input("Choose your character's name: ")
    printc("Hi "+name+", let's start.", "blue")
    printc("------------------------", "yellow")

def start(text, text_options, option_1, option_2, option_3):
    print(text)
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        take_elevator(text_elevator, text_elevator_options, elevator_option_1, elevator_option_2, elevator_option_3)
    elif decision in option_2 and decision != '':
        take_stairs(text_stairs, text_stairs_options, stairs_option_1, stairs_option_2, stairs_option_3,text_stairs_yes,text_stairs_no)
    elif decision in option_3 and decision != '':
        gameover_hall()

def take_elevator(text, text_options, option_1, option_2, option_3,text_waiting_elevator):
    print(text)
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        print(text_waiting_elevator)
        go_floor1(text_floor1, text_floor1_options, floor1_option_1, floor1_option_2, floor1_option_3,text_floor1_left,text_floor1_front,text_floor1_terminal)
    elif decision in option_2 and decision != '':
        take_stairs(text_stairs, text_stairs_options, stairs_option_1, stairs_option_2, stairs_option_3,text_stairs_yes,text_stairs_no)
    elif decision in option_3 and decision != '':
        pass

def take_stairs(text, text_options, option_1, option_2, option_3,text_stairs_yes,text_stairs_no):
    print(text)
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        print(text_stairs_yes)
        go_floor1(text_floor1, text_floor1_options, floor1_option_1, floor1_option_2, floor1_option_3,text_floor1_left,text_floor1_front,text_floor1_terminal)
    elif decision in option_2 and decision != '':
        start(text_start, text_start_options, start_option_1, start_option_2, start_option_3)

    elif decision in option_3 and decision != '':
        pass

################################################### DEF IS EMPTY #######################################################################################
def waiting_elevator(text, text_options, option_1, option_2, option_3):
    print(text)
    go_floor1(text_floor1, text_floor1_options, floor1_option_1, floor1_option_2, floor1_option_3,text_floor1_left,text_floor1_front,text_floor1_terminal)
    '''print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif decision in option_2 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif decision in option_3 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
################################################### DEF IS EMPTY #######################################################################################
def waiting_staff(text, text_options, option_1, option_2, option_3):
    print(text)
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif decision in option_2 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif decision in option_3 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def main_hall(text_options, option_1, option_2, option_3):
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        take_elevator(text_elevator, text_elevator_options, elevator_option_1, elevator_option_2, elevator_option_3)
    elif decision in option_2 and decision != '':
        take_stairs(text_stairs, text_stairs_options, stairs_option_1, stairs_option_2, stairs_option_3,text_stairs_yes,text_stairs_no)
    elif decision in option_3 and decision != '':
        waiting_staff(text_waiting_staff, text_waiting_staff_options, waiting_staff_option_1, waiting_staff_option_2, waiting_staff_option_3)


def go_floor1(text, text_options, option_1, option_2, option_3,text_floor1_left,text_floor1_front,text_floor1_terminal):
    print(text)
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        print(text_floor1_left)
        time.sleep(1)
        office_204(text_office_204, text_office_204_options, office_204_option_1, office_204_option_2, office_204_option_3)
    elif decision in option_2 and decision != '':
        print(text_floor1_front)
        # END *******************************************************************************************************************
    elif decision in option_3 and decision != '':
        print(text_floor1_terminal)
        # call def


############### DEF IS EMPTY #######################################################################################
def office_204(text,text_options, option_1, option_2, option_3):
    print(text)
    '''print(text_options)
    
        option = option_1+option_2+option_3
        decision = input("CHOOSE: ").lower()
        while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif decision in option_2 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    elif decision in option_3 and decision != '':
        pass # waiting for a entry ----------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''


# function to use as a exemplo - should be delete after finish the code    
def name_def(text_options, option_1, option_2, option_3):
    print(text)
    print(text_options)
    
    option = option_1+option_2+option_3
    decision = input("CHOOSE: ").lower()
    while decision == '' or decision not in option:
        printc("INVALID INPUT, please choose between:.","red")
        printc(text_options)
        decision = input("CHOOSE: ").lower()
    
    if decision in option_1 and decision != '':
        pass # change to function where you want to go
    elif decision in option_2 and decision != '':
        pass # change to function where you want to go
    elif decision in option_3 and decision != '':
        pass # change to function where you want to go


def gameover_hall():
    print("\n[you are waiting in the hall until you met a member of staff]")
    time.sleep(2)
    print("\n...")
    time.sleep(2)
    print("\nYou've been waiting unnecessarily for 3 hours for something to happen. The employment agency closes for the day.")
    time.sleep(2)
    printc("\nGAME OVER", "red")
    input("\nPress ENTER to exit")
    exit()


#---------END OF FUNCTIONS-----------------------------------------------
ask_name()
start(text_start, text_start_options, start_option_1, start_option_2, start_option_3)


