import time
import random

#Starting all the code
def startgame():
    start = ""
    while start != "y":
        start = input("Do you want to start the game? (y/n):")

    return start

startgame()

#background info
print("game starting...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(1)
print("Welcome to the kingdom of Kandarin, a kingdom full of a")
time.sleep(3)
print("variety of cities, each contributing some sort of value")
time.sleep(3)
print("to King Thoros. Kandarin is the youngest kingdom and largest")
time.sleep(3)
print("kingdom in Gielinor. Kandarin is bordered with Asgarnia, a")
time.sleep(3)
print("kingdom consisting of the cities of Falador, home to the white")
time.sleep(3)
print("knights, Port Sarim, a popular place for fisherman, and Burthorpe,")
time.sleep(3)
print("a place where only the strongest warriors can train.")
time.sleep(3)
print ("To the north is the Fremmenik Province, full of Norsemen who are")
time.sleep(3)
print ("all trained to be the strongest warriors. All humans of Gielinor")
time.sleep(3)
print ("originate from them so they are the ancestors of this world")
time.sleep(3)
print("You are a loyal subject of King Thanos and must help him")
time.sleep(3)
print("save the city of Ardougne. To start the quest talk to Thoros")
time.sleep(1)

#start of adventure
def start():
    begin = 'n'
    while begin != 'y':
        begin = input ("Do you wish to step up as an adventurer and serve your kingdom?[y/n]:")
        if begin != 'y':
            print ("Exiting game...")
            time.sleep(2)
            print("Just kidding. You better start this quest!")

start()

print("You look for King Thoros")
#Looking for Thoros
def thoros():
    enter = 'n'
    while enter != 'y':
        enter = input ("You find King Thoros. Do you wish to talk to him?[y/n]:")
        if enter != 'y':
            print ("To start the quest you have to talk to Thoros")
thoros()

#More background information
print ("Hello there adventurer. You came at the perfect time")
time.sleep(3)
print ("I need your help. The city of Ardougne was once a perfectly,")
time.sleep(3)
print ("peacueful place however when the Zamoraks attacked")
time.sleep(3)
print ("the citizens had no chance and our army was quickly")
time.sleep(3)
print ("defeated. The Zamoraks were laying waste on the city")
time.sleep(3)
print ("when Saradomin, the magical wizard came and banished")
time.sleep(3)
print ("the Zamoraks into a crystal. They were forever sealed")
time.sleep(3)
print ("into the crystal however yesterday I noticed it went")
time.sleep(3)
print ("missing which means that someone stole it and is trying")
time.sleep(3)
print ("to release the Zamoraks to release havok on this city")
time.sleep(3)
print ("once again.")

#this is where you start your quest
def quest():
    quest = 'n'
    while quest != 'y':
        quest = input("Can you help me find the crystal?[y/n]:")
        if quest != "y":
            print ("You must help him, otherwise your city will be doomed.")
quest()

print ("Wonderful. Thank you so much for helping. Now be off")
print ("and please bring back some good news.")
time.sleep(3)

print ("You go out to town to get some clues as to where to start")
print ("As you are walking past the fruit stand, you overhear people talking of a mysterious crystal")
time.sleep(3)

def approach():
    approach = 'n'
    while approach != 'y':
        approach = input("Do you eavesdrop?[y/n]?")
        if approach != 'y':
            print("You continue your walk")
            print("You decided that the best idea is to start at the cavern of secrets")
            break
approach()

print("You start your start over to the cavern of secrets, just north on the outskirts of Ardougne.")

#you reached the cave
def cave():
    enter = 'n'
    while enter != 'y':
        enter = input("You reach the cave. Do you wish to enter?[y/n]:")
        if enter != "y":
            print ("You must continue your journey by entering the cavern")

cave()
#You walk into the cave
print ("You enter the cavern slowly")
print ("You quickly lose sight of the sun")


time.sleep(3)
#the stick on the floor is used later in the game to hit higher dmg
print ("You enter the dark cavern. It is dark and you can only make out a small stick on the floor.")
ch1 = str(input("Do you take it? [y/n]: ")).lower()

# Stick taken
if ch1 in ['y', 'yes']:
    print("You have taken the stick!")
    time.sleep(2)
    stick = 1

# Stick not taken
else:
    print("You did not take the stick")
    stick = 0

print ("As you proceed further into the cave, you see a small glowing object")
ch2 = str(input("Do you approach the object? [y/n]")).lower()

# Approach spider
while True:
    if ch2 in ['y', 'yes']:
        print ("You approach the object...")
        time.sleep(2)
        print ("As you draw closer, you begin to make out the object as an eye!")
        time.sleep(1)
        print ("The eye belongs to a giant spider!")
        ch3 = str(input("Do you try to fight it? [y/n]")).lower()

        # Fight spider
        if ch3 in ['y', 'yes']:

            # With stick
            if stick == 1:
                print ("You only have a stick to fight with!")
                print ("You quickly jab the spider in it's eye and gain an advantage")
                time.sleep(2)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                  Fighting...                   ")
                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(3, 10))
                edmg1 = int(random.randint(1, 5))
                print ("you hit a", fdmg1)
                print ("the spider hits a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                    print ("The spider has dealt more damage than you!")
                    complete = 0


                elif fdmg1 < 5:
                    print ("You didn't do enough damage to kill the spider, but you manage to escape")
                    complete = 1


                else:
                    print ("You killed the spider!")
                    complete = 1


            # Without stick
            else:
                print ("You don't have anything to fight with!")
                time.sleep(2)
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                  Fighting...                   ")
                print ("   YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER    ")
                print ("IF THE SPIDER HITS HIGHER THAN YOU, YOU WILL DIE")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                time.sleep(2)
                fdmg1 = int(random.randint(1, 8))
                edmg1 = int(random.randint(1, 5))
                print ("you hit a", fdmg1)
                print ("the spider hits a", edmg1)
                time.sleep(2)

                if edmg1 > fdmg1:
                    print ("The spider has dealt more damage than you!")
                    complete = 0


                elif fdmg1 < 5:
                    print ("You didn't do enough damage to kill the spider, but you manage to escape")
                    complete = 1


                else:
                    print ("You killed the spider!")
                    complete = 1


        #Don't fight the spider
        if ch3 in ['n', 'no']:
            print ("You choose not to fight the spider.")
            time.sleep(1)
            print ("As you turn away, it ambushes you and impales you with it's fangs!!!")
            complete == 0



# game loop
        if complete == 1:

            alive = input('As you defeat the spider, you notice a sparkle and you find the magical jewel! You save the city of Ardougne. Would you like to play again? [y/n]: ').lower()
            if alive in ['n', 'no']:
                break


        if complete == 0:
            alive = input('O dear, you have died! Would you like to try again? [y/n]: ')
            if alive in ['n','no']:
                break


