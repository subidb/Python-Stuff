from Complex import*

snorlax1 = Pokemon("Snorlax", "Normal", 540, 40)

print(snorlax1)
snorlax1.attack()

snorlax1.level_up()
print(snorlax1)

snorlax1.attack()

snorlax1.attpower = 500
snorlax1.attack()

print(snorlax1)

# print(repr(snorlax1)) # eqv to : print(snorlax1.__repr__())
# print(str(snorlax1))

# print(len(snorlax1))
# print(1+2) = print(int.__add__(1, 2))


print("_____________________________________\n")
c1 = Complex(2, 3)
c2 = Complex(6, -4)

# print(c1)
# print(c1+c2)
