from stringcolor import cs
import time

#---------FUNCTIONS-----------------------------------------------------

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))

def room1():
    print("Your enter in room1.")
    print("Text...........")
    option_1 = "..........option 1........."
    option_2 = "..........option 2........."
    option_3 = "..........option 3........."
    printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
    decision = input("CHOOSE: ").lower()
    while decision not in ["1", "2", "3", option_1.lower(), option_2.lower(), option_3.lower()]:
        printc("INVALID INPUT, please choose between:.","red")
        printc("1- "+option_1+"/n"+"2- "+option_2+"/n"+"3- "+option_3, "cyan")
        decision = input("CHOOSE: ").lower()

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




