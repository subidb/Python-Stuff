
class Creature:

    total_creatures = 0 # class variables
    level_raise = 1

    def __init__(self, name, level, attackpower, health=100): # constructor / init method
        self.name = name  # instance variables
        self.level = level
        self.attackpower = attackpower
        # self.health = health
        if health is None:
            self.health = 100
        else:
            self.health = health

        Creature.total_creatures += 1

    def attack(self): #: game
        print(f"{self.name} Attack!" + " Damage = ", int((self.level * self.attackpower**.5)))
        # print(self.name + " Attack!" + " Damage = ", int((self.level * self.attackpower**.5)))

    def status(self):
        print("\n{} : Health = game {} ".format(self.name, self.health))
        return 'level = {}, power = {}'.format(self.level, self.attackpower)

    def level_up(self):
        print("\nLevelling up!, {} levelled up to level {}! ".format(self.name, self.level + self.level_raise))
        self.level += self.level_raise
        self.attackpower = int(self.attackpower* 1.05)
        # self.level += Creature.level_raise
        # ^ makes it unable to change (level_raise_amount of only one instance/ a child class)

    @classmethod
    def cl_level_up(cls, amount):
        cls.level_raise = amount

    @classmethod
    def instance_from_string(cls, c_str):
        s1, s2, s3, s4 = c_str.split('-')
        return cls(s1, s2, s3, s4)

    @staticmethod # used when (self) or (cls) is not in the body of the function
    def is_high(x):
        if x.level > 20:
            print("\n{} is above 20".format(x.name))

