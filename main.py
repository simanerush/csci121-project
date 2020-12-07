
from room import Room
from player import Player
from item import Item, Healing
from creature import Creature
from spell import Spell
from container import Container
import os
import updater
import random

player = Player()

def createWorld():
    a = Room("You are in a dark, mysterious place. There are trees around you, and it is a late evening.", None)
    b = Room("You see an old scroll lying under a tree.", None)
    c = Room("You smell a strange odor and hear loud footsteps somewhere around.", "troll")
    d = Room("You see some big white feathers lying around. You can hear a wing noise far away.", "hippogriff")
    e = Room("You see a lot of intertwined trees and roots. You look closer and see spider webs all around.", "acromantula")
    f = Room("You see a school bag, left here by some student.", None)
    g = Room("Seems like nothing is here... Just plain forest.", "thestral")
    h = Room("You hear loud barking and gnashing of teeth.", "dog")
    k = Room("You are standing in front of a hill. You can hear human voices from the top of the hill, but they are far away.", "centaur")
    m = Room("You can see a mysterious glowing from the trees. It smells good here.", "unicorn")
    rooms = [a, b, c, d, e, f, g, h, k, m]
    random.shuffle(rooms)
    roomsWithDeluminators = random.sample(rooms, 2)
    for room in roomsWithDeluminators:
        Item('Deluminator', 'Bring this to Dumbledore', 1).putInRoom(room)

    Room.connectRooms(rooms[0], "east", rooms[1], "west")
    Room.connectRooms(rooms[0], "north", rooms[2], "south")
    Room.connectRooms(rooms[1], "south", rooms[3], "north")
    Room.connectRooms(rooms[4], "east", rooms[3], "west")
    Room.connectRooms(rooms[4], "north", rooms[0], "south")
    Room.connectRooms(rooms[2], "north", rooms[5], "south")
    Room.connectRooms(rooms[4], "west", rooms[6], "east")
    Room.connectRooms(rooms[6], "north", rooms[7], "south")
    Room.connectRooms(rooms[0], "west", rooms[7], "east")
    Room.connectRooms(rooms[1], "east", rooms[8], "west")
    Room.connectRooms(rooms[3], "east", rooms[9], "west")
    Room.connectRooms(rooms[8], "north", rooms[9], "south")

    #default rooms
    # Room.connectRooms(a, "east", b, "west")
    # Room.connectRooms(a, "north", c, "south")
    # Room.connectRooms(b, "south", d, "north")
    # Room.connectRooms(e, "east", d, "west")
    # Room.connectRooms(e, "north", a, "south")
    # Room.connectRooms(c, "north", f, "south")
    # Room.connectRooms(e, "west", g, "east")
    # Room.connectRooms(g, "north", h, "south")
    # Room.connectRooms(a, "west", h, "east")
    # Room.connectRooms(b, "east", k, "west")
    # Room.connectRooms(d, "east", m, "west")
    # Room.connectRooms(k, "north", m, "south")

    player.location = a
    s1 = Spell('Expelliarmus', 'Helpful but not very powerful spell', 10)
    s1.putInRoom(b)
    bag = Container("Old bag", [])
    obj1 = Spell('Sectumsempra', 'Against enemies...', 30)
    obj2 = Healing('Healing Potion', 'Restores health', 2, 20)
    obj1.putInCont(bag)
    obj2.putInCont(bag)
    bag.putInRoom(f)
    player.items = []
    player.spells = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    printWay(recentWay)
    print("Your health: " + str(player.health))
    print()
    print(player.location.desc)
    print()
    if player.location.hasCreatures():
        print("The following creatures are nearby:")
        for cr in player.location.creatures:
            print(cr.name + " (health: " + str(cr.health) + ")")
        print()
    if player.location.hasItems():
        print("The following things are lying in the grass:")
        for i in player.location.items:
            print(i.name)
        print()
    if player.location.hasSpells():
        print("The following spell instructions are around you:")
        for s in player.location.spells:
            print(s.name)
        print()
    if player.location.hasContainers():
        print("You can see the following bags:")
        for cont in player.location.containers:
            print(cont.name)
        print()
    if player.location.hasDeluminator():
        print("There is a deluminator near you! Use 'pickup deluminator' to pick it up")
        print()
    print("You can go in the following directions: (Use go <direction> to go there)")
    for e in player.location.exitNames():
        print(e)
    print()

def printWay(recentWay):
    clear()
    global s
    if recentWay != None:
        global c
        c += 1
        s = s[:-1]
        s += (recentWay + '->' + '?')
        if c == 10:
            s = (recentWay + '->' + '?')

    print("Your way:")
    print(s)
    print()


def showHelp():
    clear()
    print("info -- allows you too once again see the welcoming screen.")
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drops the item that's currently in your inventory")
    print("wait <number> -- allows you to wait for a number of turns if you don't see any creatures.")
    print("me -- allows you to see your status")
    print("inspect <item> -- allows you to find out more about an item (it can be in a location or your inventory)")
    print("use <item> -- allows you to interract with items in your inventory")
    print("attack <creature name> -- allows you to attack the creature with spells you've learnt")
    print("learn <spell> -- allows you to learn the spell")
    print("open <bag> -- allows you to open the bag you might encounter")
    print("talk <creature name> -- allows you to talk with the creature (if it is friendly)")
    print("ask -- allows you to ask Ronald Weasley for help")
    print("exit -- quit the game")
    print()
    input("Press enter to continue...")



createWorld()
playing = True
s = ''
c = 0
recentWay = None
startedGame = False
canBeAttacked = True
timeSinceAskedRon = 0

while playing and player.alive:
    if not startedGame:
        startedGame = True
        clear()
        print()
        print('================= Forbidden Forest Mysteries =================')
        print()
        print("H a g r i d: ")
        print("It's you again! One more detention? What?\nYou've accused this Slytherin guy again? I'm sorry.\nLet's go to the Forbidden Forest then. Do you remember?\nYou need to be very careful, you have the whole night to stay here.\nThere are many cratures who live in this place, some of them are kind\nand some are evil.\nReminder: they might attack you, and I don't want to bring\nyou to hospital tomorrow.\nAlso, because of yesterday's accident, you might not remember spells.\nBut I think that there might be some students' instructions left in the forest.\nRonald, I'll give you some Healing Potions... Just in case...\nOh, I almost forgot! Dumbledore wants you to bring 5 deluminators.")
        print()
        print()
        print("H i n t: ")
        print("You and Ronald are to spend a detention in a Forbidden Forest.\nType 'help' to see what you can do. Good luck!")
        print()
        input("Press enter when you ready to start...")
    printSituation()
    commandSuccess = False
    timePasses = False
    if len(player.spells) >= 3 and player.deluminatorsCount >= 5:
        clear()
        playing = False
        print()
        print("Congrats! Your detention is over, and now you can head back to school.")
        print()
        print()
        print()
        input("Press enter to quit the game...")
        break
    elif player.health <= 0:
        clear()
        playing = False
        print()
        print("You are seriously injured. You've lost the game")
        print()
        print()
        print()
        input("Press enter to quit the game...")
        break

    while not commandSuccess:
        if canBeAttacked and random.random() < .3 and player.location.hasCreatures() and player.location.creature_type != "unicorn" and player.location.creature_type != "thestral" and player.location.creature_type != "centaur":
            creature = random.choice(player.location.creatures)

            if random.random() < .6 and player.spells != []:
                print("You're being attacked by " + creature.name)
                recentWay = None
                def isInt(s):
                    try:
                        int(s)
                        return True
                    except ValueError:
                        return False
                if player.spells != []:
                    c = len(player.spells)
                    print("You know the following spells: ")
                    for i in range(len(player.spells)):
                        print(str(i + 1) + ". " + str(player.spells[i].name))
                    print()
                    spell = input("Enter the number of spell you want to use: ")
                    while not isInt(spell) or int(spell) > len(player.spells):
                        clear()
                        print("Please enter a valid number.")
                        print()
                        print("You know the following spells: ")
                        for i in range(len(player.spells)):
                            print(str(i + 1) + ". " + str(player.spells[i].name))
                        print()
                        spell = input("Enter the number of spell you want to use: ")

                    targetSpell = player.spells[int(spell)-1]

                    player.attackCreature(creature, targetSpell)
                    printSituation()
                    canBeAttacked = False
            else:
                print("You're being attacked by " + creature.name)
                print("You can type 'run' to run away, or 'attack' to attack the creature with spells you know.")
                print()
                command = input("What you'll do?")
                commandWords = command.split()

                while commandWords[0].lower() != "attack" and commandWords[0].lower() != "run":
                    print("Please enter a valid command.")
                    command = input("What you'll do?")
                    commandWords = command.split()

                if commandWords[0].lower() == "attack":
                    recentWay = None
                    def isInt(s):
                        try:
                            int(s)
                            return True
                        except ValueError:
                            return False
                    if player.spells != []:
                        c = len(player.spells)
                        clear()
                        print("You know the following spells: ")
                        for i in range(len(player.spells)):
                            print(str(i + 1) + ". " + str(player.spells[i].name))
                        print()
                        spell = input("Enter the number of spell you want to use: ")
                        while not isInt(spell) or int(spell) > len(player.spells):
                            clear()
                            print("Please enter a valid number.")
                            print()
                            print("You know the following spells: ")
                            for i in range(len(player.spells)):
                                print(str(i + 1) + ". " + str(player.spells[i].name))
                            print()
                            spell = input("Enter the number of spell you want to use: ")

                        targetSpell = player.spells[int(spell)-1]

                        player.attackCreature(creature, targetSpell)
                        printSituation()
                        canBeAttacked = False
                    else:
                        print("You don't know any spells... You can try to run, though")
                        command = input("What you'll do?")
                        commandWords = command.split()

                if commandWords[0].lower() == "run":
                    player.health -= creature.damage
                    canBeAttacked = False
                    print("You succeeded in running away, but you lost " + str(creature.damage) + " points of health.")

                else:
                    print("Please enter a valid command.")
                    commandSuccess = False

        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()
        if commandWords == []:
            print("Not a valid command...")
            commandSuccess = False
        else:
            if commandWords[0].lower() == "go":   #cannot handle multi-word directions
                if len(commandWords) < 2 or player.goDirection(commandWords[1]) == False:
                    print("Invalid destination, try again")
                    commandSuccess = False
                else:
                    canBeAttacked = True
                    recentWay = commandWords[1]
                    timePasses = True
            elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
                recentWay = None
                targetName = command[7:]
                target = player.location.getItemByName(targetName)
                if targetName.lower() == "deluminator":
                    player.deluminatorsCount += 1
                if target != False:
                    if player.itemsweight + target.weight <= 8:
                        player.pickup(target)
                    else:
                        print("You can't pickup this item, it is too heavy. Drop some to do this.")
                        commandSuccess = False
                else:
                    print("No such item.")
                    commandSuccess = False
            elif commandWords[0].lower() == "info":
                clear()
                print()
                print('================= Forbidden Forest Mysteries =================')
                print()
                print("H a g r i d: ")
                print("It's you again! One more detention? What?\nYou've accused this Slytherin guy again? I'm sorry.\nLet's go to the Forbidden Forest then. Do you remember?\nYou need to be very careful, you have the whole night to stay here.\nThere are many cratures who live in this place, some of them are kind\nand some are evil.\nReminder: they might attack you, and I don't want to bring\nyou to hospital tomorrow.\nAlso, because of yesterday's accident, you might not remember spells.\nBut I think that there might be some students' instructions left in the forest.\nRonald, I'll give you some Healing Potions... Just in case...\nOh, I almost forgot! Dumbledore wants you to bring 5 deluminators.")
                print()
                print()
                print("H i n t: ")
                print("You and Ronald are to spend a detention in a Forbidden Forest.\nType 'help' to see what you can do. Good luck!")
                print()
                input("Press enter when you ready to start...")
            elif commandWords[0].lower() == "drop":
                targetName = command[5:]
                target = player.getItemByName(targetName)
                if target != False:
                    player.drop(target)
                else:
                    print("No such item.")
                    commandSuccess = False
            elif commandWords[0].lower() == "use":
                recentWay = None
                targetName = command[4:]
                target = player.getItemByName(targetName)
                if target != False and isinstance(target, Healing):
                    player.use(target)
                else:
                    if target == False:
                        print("No such item.")
                        commandSuccess = False
                    elif not isinstance(target, Healing):
                        print("You can't use this item.")
                        commandSuccess = False
            elif commandWords[0].lower() == "learn":
                recentWay = None
                #printWay(recentWay)
                targetName = command[6:]
                target = player.location.getSpellByName(targetName)
                if target != False:
                    player.learnSpell(target)
                else:
                    print("You can't learn this spell here.")
                    commandSuccess = False
            elif commandWords[0].lower() == "inventory":
                player.showInventory()
            elif commandWords[0].lower() == "help":
                showHelp()
            elif commandWords[0].lower() == "open":
                recentWay = None
                #printWay(recentWay)
                def isInt(s):
                    try:
                        int(s)
                        return True
                    except ValueError:
                        return False
                targetName = command[5:]
                target = player.location.getContainerByName(targetName)
                if target:

                    if target.objects != []:
                        clear()
                        print()
                        print("This contains the following objects: ")
                        print()
                        for i in range(len(target.objects)):
                            print(str(i + 1) + ". " + str(target.objects[i].name) + ", " + str(target.objects[i].desc))
                        print()
                        object_i = input("Enter the number of object you want to take: ")
                        while not isInt(object_i) or int(object_i) > len(target.objects):
                            clear()
                            print("Please enter a valid number.")
                            print()
                            print("This contains the following objects: ")
                            for i in range(len(target.objects)):
                                print(str(i + 1) + ". " + str(target.objects[i].name) + ", " + str(target.objects[i].desc))
                            print()
                            object_i = input("Enter the number of object you want to take: ")

                        object = target.objects[int(object_i)-1]
                        if isinstance(object, Spell):
                            player.learnSpellfromCont(object)
                            target.removeObject(int(object_i) - 1)
                        elif isinstance(object, Healing) or isinstance(object, Item):
                            player.pickupFromCont(object)
                            target.removeObject(int(object_i)  - 1)

                    else:
                        clear()
                        print()
                        print("This bag is empty... ")
                        print()
                        input("Press enter to continue...")

                else:
                    print("No such container here.")
                    commandSuccess = False
            elif commandWords[0].lower() == "exit":
                playing = False
            elif commandWords[0].lower() == "attack":
                def isInt(s):
                    try:
                        int(s)
                        return True
                    except ValueError:
                        return False
                if player.spells != []:
                    c = len(player.spells)
                    clear()
                    print("You know the following spells: ")
                    for i in range(len(player.spells)):
                        print(str(i + 1) + ". " + str(player.spells[i].name))
                    print()
                    spell = input("Enter the number of spell you want to use: ")
                    while not isInt(spell) or int(spell) > len(player.spells):
                        clear()
                        print("Please enter a valid number.")
                        print()
                        print("You know the following spells: ")
                        for i in range(len(player.spells)):
                            print(str(i + 1) + ". " + str(player.spells[i].name))
                        print()
                        spell = input("Enter the number of spell you want to use: ")
                    targetName = command[7:]
                    target = player.location.getCreatureByName(targetName)
                    targetSpell = player.spells[int(spell)-1]
                    if target != False:
                        player.attackCreature(target, targetSpell)
                    else:
                        print("No such creature.")
                        commandSuccess = False
                else:
                    print("You don't know any spells...")
                    commandSuccess = False

            elif commandWords[0].lower() == "wait":
                def isInt(s):
                    try:
                        int(s)
                        return True
                    except ValueError:
                        return False
                targetNumber = command[5:]
                if isInt(targetNumber) and int(targetNumber) <= 5:
                    print("Success!")
                    for i in range(int(targetNumber)):
                        updater.updateAll()
                elif int(targetNumber) > 5:
                    print("Please enter a smaller number")
                else:
                    print("Please enter a number.")
                    commandSuccess = False
            elif commandWords[0].lower() == "me":
                recentWay = None
                clear()
                print()
                #printWay(recentWay)
                print(player.location.desc)
                print()
                print("You are holding folowing items: ", player.printItems())
                print("Your health is ", player.health)
                print()
                print("You know the following spells: ", player.printSpells())
                print()
                input("Press enter to continue...")
            elif commandWords[0].lower() == "inspect":
                targetName = command[8:]
                if player.location.getItemByName(targetName)!= False and player.getItemByName(targetName)!=False:
                    clear()
                    print(player.getItemByName(targetName).desc)
                    print()
                    input("Press enter to continue...")
                elif player.location.getItemByName(targetName)!= False:
                    clear()
                    print(player.location.getItemByName(targetName).desc)
                    print()
                    input("Press enter to continue...")
                elif player.getItemByName(targetName)!= False:
                    clear()
                    print(player.getItemByName(targetName).desc)
                    print()
                    input("Press enter to continue...")
                else:
                    print("No such item...")
                    commandSuccess = False
            elif commandWords[0].lower() == "ask":
                recentWay = None
                if timeSinceAskedRon < 10:
                    print()
                    print("Ronald is tired, he doesn't want to help you")
                    print()
                    input("Press enter to continue...")
                elif timeSinceAskedRon >= 10 and player.location.hasCreatures() and player.location.creature_type != "unicorn" and player.location.creature_type != "thestral" and player.location.creature_type != "centaur":
                    if player.location.creature_type == "spider":
                        print()
                        print("Ronald is afraid of spiders and he won't help you!")
                        print()
                        timeSinceAskedRon = 0
                        input("Press enter to continue...")
                    else:
                        creature = random.choice(player.location.creatures)
                        creature.die()
                        print("Ronald has attacked " + creature.name)
                        loot = [Healing('Healing Potion', 'Drink this to restore health', 2, 20), None]
                        choice = random.choice(loot)
                        if choice is not None:
                            print()
                            print("Ronald got", choice.name, " after attacking ", creature.name)
                            print()
                            choice.putInRoom(player.location)
                            timeSinceAskedRon = 0
                            input("Press enter to continue...")
                else:
                    player.items.append(Healing('Healing Potion', 'Drink this to restore health', 2, 20))
                    print("Ronald gave you a Healing Potion.")
                    timeSinceAskedRon = 0
                    input("Press enter to continue...")
            elif commandWords[0].lower() == "talk":
                recentWay = None
                targetName = command[5:]
                target = player.location.getCreatureByName(targetName)
                if target != False:
                    if target.type == "unicorn" or target.type == "thestral" or target.type == "centaur":
                        #clear()
                        loot = ["spell", "heal", "del", None]
                        choice = random.choice(loot)
                        if choice == "heal":
                            if 2 + player.itemsweight <= 8:
                                player.items.append(Healing('Healing Potion', 'Drink this to restore health', 2, 20))
                                print()
                                print(str(target.name) + " gave you a Healing potion and left.")
                                player.location.removeCreature(target)
                                print()
                                input("Press enter to continue...")
                            else:
                                Healing('Healing Potion', 'Drink this to restore health', 2, 20).putInRoom(player.location)
                                print()
                                print(str(target.name) + " gave you a Healing potion, but you do not have any space.")
                                player.location.removeCreature(target)
                                print()
                                input("Press enter to continue...")
                        elif choice == "spell":
                            if len(player.spells) == 3 or player.getSpellByName('Petrificus Totalus'):
                                if 2 + player.itemsweight <= 8:
                                    player.items.append(Healing('Healing Potion', 'Drink this to restore health', 2, 20))
                                    print()
                                    print(str(target.name) + " gave you a Healing potion and left.")
                                    player.location.removeCreature(target)
                                    print()
                                    input("Press enter to continue...")
                                else:
                                    Healing('Healing Potion', 'Drink this to restore health', 2, 20).putInRoom(player.location)
                                    print()
                                    print(str(target.name) + " gave you a Healing potion, but you do not have any space.")
                                    player.location.removeCreature(target)
                                    print()
                                    input("Press enter to continue...")
                            else:
                                player.spells.append(Spell("Petrificus Totalus", "This spell makes the creture weaker", 60))
                                print()
                                print(str(target.name) + " taught you how to use Petrificus Totalus and escaped in the forest.")
                                player.location.removeCreature(target)
                                print()
                                input("Press enter to continue...")
                        elif choice == "del":
                            if player.deluminatorsCount < 4:
                                if 1 + player.itemsweight <= 8:
                                    player.deluminatorsCount += 1
                                    player.items.append(Item('Deluminator', 'Bring this to Dumbledore', 1))
                                    print()
                                    print(str(target.name) + " gave you a deluminator and left.")
                                    player.location.removeCreature(target)
                                    print()
                                    input("Press enter to continue...")
                                else:
                                    print()
                                    Item('Deluminator', 'Bring this to Dumbledore', 1).putInRoom(player.location)
                                    print(str(target.name) + " gave you a deluminator, but you do not have any space.")
                                    player.location.removeCreature(target)
                                    print()
                                    input("Press enter to continue...")
                            else:
                                if 2 + player.itemsweight <= 8:
                                    player.items.append(Healing('Healing Potion', 'Drink this to restore health', 2, 20))
                                    print()
                                    print(str(target.name) + " gave you a Healing potion and left.")
                                    player.location.removeCreature(target)
                                    print()
                                    input("Press enter to continue...")
                                else:
                                    Healing('Healing Potion', 'Drink this to restore health', 2, 20).putInRoom(player.location)
                                    print()
                                    print(str(target.name) + " gave you a Healing potion, but you do not have any space.")
                                    player.location.removeCreature(target)
                                    print()
                                    input("Press enter to continue...")

                        elif choice == None:
                            print()
                            printSituation()
                            print("You scared " + str(target.name) + " and it left.")
                            print()
                            input("Press enter to continue...")
                    else:
                        printSituation()
                        print("This creature doesn't want to talk with you...")
                        commandSuccess = False

                else:
                    print("No such creature...")
                    commandSuccess = False
            else:
                print("Not a valid command...")
                commandSuccess = False
    if timePasses == True:
        timeSinceAskedRon += 1
        updater.updateAll()
