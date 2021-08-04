import random
def hangman():

    word = random.choice(["thor", "ironman", "avengers", "avatar", "godfather", "aliens", "jumanji", "aladdin", "cinderella", "batman", "spiderman", "twilight", "hulk", "deathnote", "conjuring", "annabelle"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("\nYou win!")
            break

        print("\nGuess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("\n9 turns left")
                print("  --------  \n")
            if turns == 8:
                print("\n8 turns left")
                print("  --------  ")
                print("     O      \n")
            if turns == 7:
                print("\n7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      \n")
            if turns == 6:
                print("\n6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       \n")
            if turns == 5:
                print("\n5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     \n")
            if turns == 4:
                print("\n4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     \n")
            if turns == 3:
                print("\n3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     \n")
            if turns == 2:
                print("\n2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     \n")
            if turns == 1:
                print("\n1 turn left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     \n")
            if turns == 0:
                print("\nYou loose")
                print("\nYou let a kind man die :(")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     \n")
                break


name = input("Enter your name to start the game :\n")
print("\nWelcome  " , name )
print("\n----------------------------\n")
print("This is the Ultimate Hangman Game\n")
print("(Try to guess the Movie in less than 10 Attempts, Otherwise You will Loose)")
print("(At your each wrong attempt the the man will start hanging step by step)")
print("(When ur all wrong attempts are over, the man will hang and your game over, You loose)")
print("(If you guess the movie correct before mag hangning, you won Hurray!!!)\n")
hangman()
print()

