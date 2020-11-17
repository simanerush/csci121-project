import os
import random
from item import Item, Healing

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.health = 50
        self.alive = True
        self.spells = []
        self.itemsweight = 0
        self.damage = 10
        self.creaturesAttacked = 0
    def goDirection(self, direction):
        if self.location.getDestination(direction):
            self.location = self.location.getDestination(direction)
        else:
            return False
    def pickup(self, item):
        self.itemsweight += item.weight
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)
    def pickupFromCont(self, item):
        self.itemsweight += item.weight
        self.items.append(item)
        item.loc = self
    def learnSpell(self, spell):
        self.spells.append(spell)
        self.location.removeSpell(spell)
    def learnSpellfromCont(self, spell):
        self.spells.append(spell)
    def drop(self, item):
        self.itemsweight -= item.weight
        self.removeItem(item)
        item.loc = self.location
        self.location.items.append(item)
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def removeItem(self, item):
        self.items.remove(item)
    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")
    def printItems(self):
        if len(self.items) == 0:
            return "You don't carry anything..."
        else:
            string = ''
            for i in range(len(self.items)):
                string += (str(i + 1) + '. ' + self.items[i].name + '\n')

            return string
    def printSpells(self):
        if len(self.spells) == 0:
            return "You don't know any spells..."
        else:
            string = ''
            for i in range(len(self.spells)):
                string += (str(i + 1) + '. ' + self.spells[i].name + '\n')

            return string

    def attackCreature(self, cr, spell):
        if self.creaturesAttacked == 5:
            self.health += 5
            self.creaturesAttacked = 0

        while cr.health > 0 and self.health > 0:
            clear()
            print("You are attacking " + cr.name + " using " + spell.name)
            print()
            print("Your health is " + str(self.health) + ".")
            print(cr.name + "'s health is " + str(cr.health) + ".")
            print()
            self.health -= cr.damage
            cr.health -= spell.damage
            print()
            input("Press enter to continue...")
        if self.health <= 0:
            clear()
            print("You died.")
            self.alive = False
        if cr.health <= 0 and self.health > 0:
            clear()
            print("You win. Your health is now " + str(self.health) + ".")
            self.creaturesAttacked += 1
            if cr.type != "thestral" and cr.type != "unicorn" and cr.type != "centaur":
                loot = [Healing('Healing Potion', 'Drink this to restore health', 2, 20), None]
                choice = random.choice(loot)
                if choice != None:
                    if self.itemsweight + choice.weight <= 8:
                        self.items.append(choice)
                        print()
                        print("You've got", choice.name)
                        print()
                    else:
                        print()
                        print("Oops! You've got", choice.name, ", but you can't carry it.")
                        print()
                        choice.putInRoom(self.location)
            else:
                print("You have killed the kind creature. Maybe try to talk to it next time?")
            cr.die()
        print()
        input("Press enter to continue...")

    def use(self, item):
        self.health += item.healing
        self.removeItem(self.getItemByName(item.name))
