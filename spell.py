import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Spell:
    def __init__(self, name, desc, damage):
        self.name = name
        self.desc = desc
        self.loc = None
        self.damage = damage
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addSpell(self)
    def putInCont(self, cont):
        self.loc = cont
        cont.addObject(self)
