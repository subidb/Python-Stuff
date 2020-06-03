from Creature import Creature
from Creatures import Dragon
from Creatures import Direwolf

# import Creature
# import Creatures

c1 = Creature("Wight", 5, 100, 20)
c1.attack()

print("___________________________________________")
d1 = Dragon("Rhaegal", 25, 100, 50, 50)
d1.attack()
d1.flamethrower()

print("___________________________________________")
d1 = Direwolf("Summer", 21, 100, 40, 50)
d1.attack()
d1.icefang()
