import sqlite3
from fifa import *
from main import *

# conn = sqlite3.connect(':memory:')  # in memory database

conn = sqlite3.connect('tournament_members.db')  # creates or connects to a db file

c = conn.cursor()


# c.execute("""CREATE TABLE members(
#             id integer,
#             fname text,
#             lname text,
#             age integer,
#             country text
# )
# """)

# c.execute("INSERT INTO members VALUES (1, 'Peter', 'Crouch', 34, 'England')")
# -# c.execute("INSERT INTO members VALUES (2, 'Peter', 'Baily', 'England')")  # error: table has 5 columns, 4 supplied

# c.execute("INSERT INTO members VALUES (2, 'Jaime', 'Vardy', 28, 'England')")
#

# c.execute("DELETE FROM members WHERE fname = 'John' ")
#
# c.execute("DELETE FROM members")

# c.execute("SELECT * FROM members")
# memberlist = c.fetchall()

member1 = TournamentMember(3, "John", "Terry", 32, "England")
member2 = TournamentMember(4, "Alex", "Ferguson", 60, "England")

# c.execute("INSERT INTO members VALUES (?, ?, ?, ?, ?)",  # tuple
#           (member1.idno, member1.fname, member1.lname, member1.age, member1.country))

# c.execute("INSERT INTO members VALUES(:idno, :fname, :lname, :age, :country)",
#           {'idno': member2.idno, 'fname': member2.fname, 'lname': member2.lname,
#            'age': member2.age, 'country':member2.country})


# c.execute("SELECT * FROM members WHERE fname = 'Jaime'")

c.execute("SELECT * FROM members WHERE lname=?", ('Ferguson',))
memberlist = c.fetchall()

c.execute("SELECT * FROM members")
memberlist = c.fetchall()

c.execute("SELECT age FROM members WHERE country=:country", {'country': 'England'})
memberlist = c.fetchall()

conn.commit()
conn.close()

for member in memberlist:
    print(member)