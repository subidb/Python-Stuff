# from Creature import *
from Creatures import *  # using * imports everything

# import Creature
# import Creatures

def print_line():
    print("___________________________________________")
    
c1 = Creature("Wight", 5, 20) # (self, name, level, attackpower, health)
c1.attack()

print_line()

d1 = Dragon("Rhaegal", 25, 40, 50) # (self, name, level, attackpower, firepower, health)
d1.attack()
d1.flamethrower()

d2 = Dragon("Viserion", 20, 35, 50) # ( self, name, level, attackpower, icepower, health)

print_line()  
w1 = Direwolf("Summer", 26, 45, 40)
w1.name = "GreyWind"
# d1.type = "Ice"
# print(d1.type)
w1.attack()
w1.icefang() # equivalent to - > Direwolf.icefang(w1)


print_line()
print()

print(w1.status())
w1.level_up()
print()

print(w1.status())

print()
# Creature.level_raise = 2
Dragon.level_raise = 2
# d1.level_raise = 2

#Creature.cl_level_up(4)

print(d2.status())
d2.level_up()
print()
print(d2.status())

print()
# print(w1.__dict__)
w2 = Direwolf("Summer", 20, 40, 40, 95)
print(w2.status())
w2.level_up()

print(w2.status())

print("\nTotal number of Creatures = ", Creature.total_creatures)
print(w2.status())
c2_str = "Wight-5-20-95"
c2 = Creature.instance_from_string(c2_str)
# print(c2.status())
#
# w2.is_high(w2)

# print(help())

# print(isinstance(d2, Direwolf))
# print(issubclass(Dragon, Creature))


