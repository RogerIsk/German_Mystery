from stringcolor import cs
import time

# printing with color easily
def printc(string, color="white"):
    # string first, then color optional - default white
    print(cs(string,color))


intro = """
YOU ARE waiting for your JC-Agent inside a dark, cold, hopeless room of the Jobcenter HQ in Berlin.

As usual in sweat and fear waiting for the agent to come back with also usual bad news - you notice screams in the hallways.
Is this the day? Are the people finally standing up against the horrible Jobcenter? 
You dont know for sure - as the only thing you hear are screams - followed by deafening silence.

WHAT DO YOU DO?
"""
intro_decisions = "(enter hallway/ call agent/ wait like a good german citizen)"

#map - 1st floor (hallway, guards office, elevator) 
#      2nd floor (hallway, agents office, elevator, bathroom, waiting room)

######## PROGRAM START #########
printc(intro, "blue")
time.sleep(3)
printc(intro_decisions, "cyan")
time.sleep(0.5)
decision = input("CHOOSE: ") 
if decision.lower() == "enter hallway":
    printc("You entered the hallway. but to your surprise - it seems life went on normally and people are just working and doing normal things.","green")
    time.sleep(1)
    printc("You asked a random person 'Yo what were those screams?? is everyone ok?' he answered unimpressed 'ah yes someone protested against how we do things, so we... took care of him.'","green")
    time.sleep(3)
    printc("WHAT DO YOU DO?", "blue")
    printc("go find your agent/ start a fight too","cyan")
    decision = input("CHOOSE: ")
    if decision.lower() == "go find your agent":
        print()
        #finding your agent and then stuff happens
    elif decision.lower() == "start a fight too":
        print()
        # starting a fight in the jc
    else:
        printc("INVALID INPUT","red")
elif decision.lower() == "call agent":
    printc("You called your agent and waited for him to answer - but nothing.","green")
    time.sleep(1)
    printc("After long waiting you stopped trying and accept you can't reach that guy...","green")
    time.sleep(3)
    printc("WHAT DO YOU DO?", "cyan")
    # decisions (
elif "wait" in decision.lower():
    printc("After a long and polite waiting time - you feel how the injustice of this whole situation begins to corrupt you.","green")
    time.sleep(1)
    printc("Every damn time youre here they let you wait, and wait, and wait for what? For like enough cash to not die in the street? MAybe? You've had enough.","orange")
    time.sleep(1)
    printc("Your soul fills with dark anger and violence - fueled by this you storm out of that damn room and search for the first person to unload your anger upon. Ready to say: 'This is unacceptable'","red")
    time.sleep(3)
    printc("WHAT DO YOU DO?", "cyan")
    # decisions (
else:
    printc("INVALID INPUT.","red")