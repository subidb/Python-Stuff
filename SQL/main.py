from fifa import *

# member1 = TournamentMember(1, "John", "Terry", 32, "England", None)
#
# print(member1)

# (self, idno, fname, lname,  age, country):
# player : (self, idno, fname, lname,  age, country, position, rating, goals):
# manager : (self, idno, fname, lname,  age, nationality, team):

player1 = Player(1, "John", "Terry", 32, "england", "CB", 88)
manager1 = Manager(1, "Pep", "Guardiola", 40, "Spain", "Spain")

member3 = TournamentMember(1, "David", "Silva", 28, "Spain")

# print(player1)
# print(manager1)
# print(player1.fname, player1.age)