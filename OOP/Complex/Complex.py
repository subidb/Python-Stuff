class Pokemon:
    def __init__(self, name, type_, ovstat, level):
        self.name = name
        self.type = type_
        self.ovstat = ovstat
        self.level = level
       # self.attpower = int(self.level * (self.ovstat/10))

    def print_info(self):
        print("\n{}:\nType:{}, Statpower:{}, Level:{}".format(self.name, self.type, self.ovstat, self.level))

    def __repr__(self):
        return "\n[{}, Type:{}, Statpower:{}, Level:{}]".format(self.name, self.type, self.ovstat, self.level)

    def __str__(self):
        return "\n{}:\nType:{}, Statpower:{}, Level:{}".format(self.name, self.type, int(self.ovstat), self.level)

    def __len__(self):
        return len(self.name)

    def level_up(self):
        print("\nlevelling up! {} grew to level {}!".format(self.name, self.level+1))
        self.level += 1

    @property
    def attpower(self):
        return int(self.level * (self.ovstat/10))

    @attpower.setter
    def attpower(self, att):
        self.ovstat = ((att * 10) / self.level)

    def attack(self):
        print("\nGeneric attack! damage = {}".format(int(self.attpower)))


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return "{}".format(complex(self.real, self.imag))

    # def __repr__(self):
    #     return "{}+{}i".format(self.real, self.imag)

    def __add__(self, other):
        sum = str(Complex(self.real + other.real, self.imag + other.imag))
        sum1 = sum.replace('j','i')
        return sum1


