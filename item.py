import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, weight):
        self.name = name
        self.desc = desc
        self.loc = None
        self.weight = weight
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)
    def putInCont(self, cont):
        self.loc = cont
        cont.addObject(self)

class Healing(Item):
    def __init__(self, name, desc, weight, healing):
        super().__init__(name, desc, weight)
        self.healing = healing
