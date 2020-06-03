import sqlite3
from fifa import *
from main import *


conn = sqlite3.connect(':memory:')  # in memory database

# conn = sqlite3.connect('tournament_members.db')  # creates or connects to a db file

c = conn.cursor()

c.execute("""CREATE TABLE members(
            id integer,
            fname text,
            lname text,
            age integer,
            country text
)
""")


def insert_mem(mem):
    with conn:
        c.execute("INSERT INTO members VALUES(:idno, :fname, :lname, :age, :country)",
                  {'idno': mem.idno, 'fname': mem.fname, 'lname': mem.lname,
                   'age': mem.age, 'country': mem.country})


def getby_country(country):
    c.execute("SELECT * FROM members WHERE country=:country", {'country': country})
    return c.fetchall()


def deleteall():
    c.execute("DELETE FROM members WHERE fname = 'John' ")
 

def displayall():
    c.execute("SELECT * FROM members")
    return c.fetchall()


# c.execute("INSERT INTO members VALUES (1, 'Peter', 'Crouch', 34, 'England')")
# # c.execute("INSERT INTO members VALUES (2, 'Peter', 'Baily', 'England')")  # error: table has 5 columns, 4 supplied
#
# c.execute("INSERT INTO members VALUES (2, 'Jaime', 'Vardy', 28, 'England')")


# c.execute("DELETE FROM members")


member1 = TournamentMember(3, "John", "Terry", 32, "England")
member2 = TournamentMember(4, "Alex", "Ferguson", 60, "England")

insert_mem(member1)
insert_mem(member2)
insert_mem(member3)

memberlist = displayall()
memberlist.sort()
conn.close()

for member in memberlist:
    print(member)
