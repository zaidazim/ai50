from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
statement0 = And(AKnight, AKnave)
knowledge0 = And(
    # And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    Biconditional(AKnight, Not(AKnave)),
    Implication(AKnight, statement0),
    Implication(AKnight, Not(statement0))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement1 = And(AKnave, BKnave)
knowledge1 = And(
    Biconditional(AKnight, Not(AKnave)),     # A is either a knight or a knave 
    Biconditional(BKnight, Not(BKnave)),     # B is either a knight or a knave 
    Implication(AKnave, Not(statement1)),    # Statement1 is false if A is knave
    Implication(AKnight, statement1)         # Statement1 is true if A is knight
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
statement2 = Or(And(AKnight, BKnight), And(AKnave, BKnave))
statement_2 = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    Biconditional(AKnight, Not(AKnave)),     # A is either a knight or a knave 
    Biconditional(BKnight, Not(BKnave)),     # B is either a knight or a knave 
    Implication(AKnight, statement2),
    Implication(AKnave, Not(statement2)),
    Implication(BKnight, statement_2),
    Implication(BKnave, Not(statement_2))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
statement3 = Or(AKnight, AKnave)
statement_3 = And(AKnave, CKnave)
statement_4 = AKnight
knowledge3 = And(
    Biconditional(AKnight, Not(AKnave)),     # A is either a knight or a knave
    Biconditional(BKnight, Not(BKnave)),     # B is either a knight or a Knave
    Biconditional(CKnight, Not(CKnave)),     # C is either a knight or a knave
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    Implication(BKnight, statement_3),
    Implication(BKnave, Not(statement_3)),
    Implication(CKnight, And(statement_4, Not(statement_3))),
    Implication(CKnave, And(Not(statement_4), statement_3))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
