from stringcolor import cs
import time

#---------FUNCTIONS-----------------------------------------------------

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

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
        return "1. floor"
    elif decision in ["2","no","n"]:
        print('You turn back into the Main Hall.')
        return "main hall"

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
        return "office_204"
    elif decision in ["2",option_2]:
        print('A big Potato comes out of the shadows and dragg you into the darkness. You died, what did you expect.')
        #return ""
    elif decision in ["3",option_3]:
        print('.............')
        return ""

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

intro = """
YOU ARE waiting for your JC-Agent inside a dark, cold, hopeless room of the Jobcenter HQ in Berlin.

As usual in sweat and fear waiting for the agent to come back with also usual bad news - you notice screams in the hallways.
Is this the day? Are the people finally standing up against the horrible Jobcenter? 
You dont know for sure - as the only thing you hear are screams - followed by deafening silence.

WHAT DO YOU DO?
"""
intro_decisions = """1- Enter hallway
2- Call agent
3- Wait like a good german citizen"""

######## PROGRAM START #########
printc(intro, "blue")
time.sleep(1)
#printc(intro_decisions, "cyan")
#time.sleep(0.5)
#decision = input("CHOOSE: ").lower()
#while decision not in ["1", "2", "3", "enter hallway", "call agent", "wait like a good german citizen"]:
#    printc("INVALID INPUT, please choose between:.","red")
#    printc(intro_decisions, "cyan")
#    decision = input("CHOOSE: ").lower()

option_1 = "Enter hallway"
option_2 = "Call agent"
option_3 = "Wait like a good german citizen"
printc("1- "+option_1+"\n"+"2- "+option_2+"\n"+"3- "+option_3, "cyan")
decision = input("CHOOSE: ").lower()
while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
    printc("INVALID INPUT, please choose between:.","red")
    printc("1- "+option_1+"\n"+"2- "+option_2+"\n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()




