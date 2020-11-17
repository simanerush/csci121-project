import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Container:
    def __init__(self, name, objects):
        self.name = name
        self.objects = objects

    def putInRoom(self, room):
        self.loc = room
        room.addContainer(self)

    def addObject(self, object):
        self.objects.append(object)

    def removeObject(self, index):
        self.objects.pop(index)
