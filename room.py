import random
import updater
from creature import Creature

class Room:
    def __init__(self, description, creature_type):
        self.desc = description
        self.creatures = []
        self.exits = []
        self.items = []
        self.spells = []
        self.containers = []
        self.door = None
        self.creature_type = creature_type
        updater.register(self)
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
        return False
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addItem(self, item):
        self.items.append(item)
    def addSpell(self, spell):
        self.spells.append(spell)
    def removeItem(self, item):
        self.items.remove(item)
    def removeSpell(self, spell):
        self.spells.remove(spell)
    def addCreature(self, creature):
        self.creatures.append(creature)
    def addContainer(self, container):
        self.containers.append(container)
    def removeContainer(self, container):
        self.containers.remove(container)
    def removeCreature(self, creature):
        self.creatures.remove(creature)
    def hasItems(self):
        return self.items != []
    def hasSpells(self):
        return self.spells != []
    def hasDoor(self):
        return self.door != None
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def getSpellByName(self, name):
        for i in self.spells:
            if i.name.lower() == name.lower():
                return i
        return False
    def getContainerByName(self, name):
        for i in self.containers:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasCreatures(self):
        return self.creatures != []
    def hasContainers(self):
        return self.containers != []
    def getCreatureByName(self, name):
        for i in self.creatures:
            if i.name.lower() == name.lower():
                return i
        return False
    def getDoorInLocation(self):
        return self.door
    def randomNeighbor(self):
        return random.choice(self.exits)[1]
    def update(self):
        names = ["Vlad", "Kostya", "Bella", "Katya", "Sonya", "Tolya", "Sasha", "Igor", "Pasha", "Nadya", "Mikhail"]
        if len(self.creatures) < 4:
            if random.random() < .5:
                Creature(random.choice(names), self, self.creature_type)
