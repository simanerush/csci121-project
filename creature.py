import random
import updater

class Creature:
    def __init__(self, name, room, type):
        self.type = type
        #troll, hippogriff, acromantula, thestral, dog, centaur, unicorn
        if self.type == "troll":
            self.peaceful = False
            self.name = "Troll " + name
            self.health = 100
            self.room = room
            self.damage = 20
            room.addCreature(self)
            updater.register(self)

        elif self.type == "hippogriff":
            self.peaceful = False
            self.name = "Hippogriff " + name
            self.health = 200
            self.room = room
            self.damage = 20
            room.addCreature(self)
            updater.register(self)

        elif self.type == "acromantula":
            self.peaceful = False
            self.name = "Spider " + name
            self.health = 10
            self.room = room
            self.damage = 5
            room.addCreature(self)
            updater.register(self)

        elif self.type == "thestral":
            self.peaceful = False
            self.name = "Thestral " + name
            self.health = 60
            self.room = room
            self.damage = 10
            room.addCreature(self)
            updater.register(self)

        elif self.type == "dog":
            self.peaceful = False
            self.name = "Three-headed dog " + name
            self.health = 30
            self.room = room
            self.damage = 15
            room.addCreature(self)
            updater.register(self)

        elif self.type == "centaur":
            self.peaceful = True
            self.name = "Centaur " + name
            self.health = 100
            self.room = room
            self.damage = 20
            room.addCreature(self)
            updater.register(self)

        elif self.type == "unicorn":
            self.peaceful = True
            self.name = "Unicorn " + name
            self.health = 100
            self.room = room
            self.damage = 10
            room.addCreature(self)
            updater.register(self)

    def update(self):
        # if random.random() < .5:
        #     self.moveTo(self.room.randomNeighbor())
        pass
    def moveTo(self, room):
        self.room.removeCreature(self)
        self.room = room
        room.addCreature(self)
    def attack(self, player):
        pass
    def die(self):
        self.room.removeCreature(self)
        updater.deregister(self)
