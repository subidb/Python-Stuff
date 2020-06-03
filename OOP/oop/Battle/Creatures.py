from Creature import Creature

class Dragon(Creature):
    def __init__(self, name, level, health, attackpower, firepower):
        Creature.__init__(self, name, level, health, attackpower)
        self.firepower = firepower

    def flamethrower(self):
        print("Flamethrower!, Damage = ", int((self.level * self.attackpower**.5 * self.firepower**.5)))

class Direwolf(Creature):
    def __init__(self, name, level, health, attackpower, icepower):
        Creature.__init__(self, name, level, health, attackpower)
        self.icepower = icepower

    def icefang(self):
        print("IceFang!, Damage = ", int((self.level * self.attackpower**.5 * self.icepower**.5)))
