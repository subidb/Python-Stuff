from questions import Question

questions = [
    Question("Who is the best footballer of the 21st century?\n "
    "(a)Lionel Messi (b)Zinedine Zidane (c)Cristiano Ronaldo (d) Ronaldo9\n", "a"),
    Question("Which country has the most World cups?\n "
    "(a)Germany (b)Italy (c)Brazil (d)France\n", 'c'),
    Question("Which player has the most world cup Goals?\n"
    "(a)Ronaldo9 (b)Miroslav Klose (c)Thomas Muller (d)Pele\n", 'b'),
    Question("Which of the following clubs have not won 'THE TREBLE?''\n"
    "(a)Bayern Munich (b)FC Barcelona (c)Ajax (d)Real Madrid\n", 'd'),
    Question("Which player won Both the Best Player and the Best Goalkeeper in a World Cup Tournamnet?\n"
    "(a)Oliver Kahn (b)Manuel Neuer (c)Iker Casillas (d)David de gea\n", 'a')
]

def quiz(questions):
    score = 0
    for q in questions:
        ans = input(q.ques)
        if ans == q.ans:
            score += 1
            print("\nCorrect!\n")
        else:
            print("\nIncorrect!, the correct option is: ", q.ans, "\n")
    print("\nYour score is :", score, "/", len(questions))

quiz(questions)
