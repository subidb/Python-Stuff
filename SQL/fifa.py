class TournamentMember:
    def __init__(self, idno, fname, lname,  age, country):
        self.idno = idno
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.age = age
        self.country = country.capitalize()


    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)

    def __repr__(self):
        member = "[{}, {}, {}]".format(self.fullname, self. age, self.country)
        return member


class Player(TournamentMember):
    def __init__(self, idno, fname, lname,  age, country, position, rating, goals=0):
        TournamentMember.__init__(self, idno, fname, lname,  age, country)
        self.position = position
        self.rating = rating
        self.goals = goals

    @property
    def team(self):
        return self.country

    def __repr__(self):  # print
        return "[({}, {}, {}) - Rating : {}, Goals : {}]"\
            .format(self.fullname, self.age, self.country, self.rating, self.goals)


class Manager(TournamentMember):
    def __init__(self, idno, fname, lname,  age, country, team):
        TournamentMember.__init__(self, idno, fname, lname,  age, country)
        self.team = team

    def __repr__(self):
        return "[({}, {}, {}) - Team : {}]" \
            .format(self.fullname, self.age, self.country, self.team)
