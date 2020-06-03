from Creature import Creature


class Dragon(Creature):

    def __init__(self, name, level, attackpower, firepower, health=None):
        # super().__init__(name, level, health, attackpower)
        Creature.__init__(self, name, level, attackpower, health)
        self.firepower = firepower

    def flamethrower(self):
        print("Flamethrower!, Damage = ", int((self.level * self.attackpower**.5 * self.firepower**.5)))


class Direwolf(Creature):

    def __init__(self, name, level, attackpower, icepower, health=None):
        Creature.__init__(self, name, level, attackpower, health)
        self.icepower = icepower

    def icefang(self):
        print("IceFang!, Damage = ", int((self.level * self.attackpower**.5 * self.icepower**.5)))
