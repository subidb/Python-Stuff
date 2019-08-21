
class Creature:
    def __init__(self, name, level, health, attackpower):
        self.name = name
        self.level = level
        self.health = health
        self.attackpower = attackpower

    def attack(self):
        #print(self.name + " Attack!" + " Damage = ", int((self.level * self.attackpower**.5)))
        print(f"{self.name} Attack!" + " Damage = ", int((self.level * self.attackpower**.5)))
