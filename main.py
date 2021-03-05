import random
import json

data = json.load(open("data.json"))
x = []
for key in data.keys():
    x.append(key)


def meaning(word):
    word = word.lower()
    if word in data:
        print(data[word])
        print("contains only smaller case letters:")
    elif word.title() in data:
        print(data[word.title()])
        print("1st letter is a upper case letters:")
    elif word.upper() in data:
        print(data[word.upper()])
        print("contains only upper case letters:")
    else:
        print("No meaning found")


def hangman():
    word = random.choice(x)
    validletters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- '
    if validletters not in word:
        word = random.choice(x)
    print("Meaning of the word:")
    meaning(word)
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""

        print("guess the word:", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            if guess != '-':
                turns = turns - 1
                if turns == 9:
                    print("9 turns left ")
                    print(" -------")
                if turns == 8:
                    print("8 turns left ")
                    print(" ------- ")
                    print("    O    ")
                if turns == 7:
                    print("7 turns left ")
                    print(" ------- ")
                    print("    O    ")
                    print("    |    ")
                if turns == 6:
                    print("6 turns left ")
                    print(" ------- ")
                    print("    O /  ")
                    print("    |    ")
                if turns == 5:
                    print("5 turns left ")
                    print(" ------- ")
                    print("  \ O /  ")
                    print("    |    ")
                if turns == 4:
                    print("4 turns left ")
                    print(" ------- ")
                    print("  \ O /  ")
                    print("    |    ")
                    print("   /     ")
                if turns == 3:
                    print("3 turns left ")
                    print(" ------- ")
                    print("  \ O /  ")
                    print("    |    ")
                    print("   / \   ")
                if turns == 2:
                    print("2 turns left ")
                    print(" ------- ")
                    print("  \ O-/--")
                    print("    |    ")
                    print("   / \   ")
                if turns == 1:
                    print("1 turns left ")
                    print("Last breath!")
                    print(" ------- ")
                    print("  \ O-/-|")
                    print("    |    ")
                    print("   / \   ")
                if turns == 0:
                    print("You loose ")
                    print("you let a poor man die!!")
                    print(" ------- ")
                    print("    O--| ")
                    print("  / | \  ")
                    print("   / \   ")
                    print("The word is:")
                    print(word)
                    break

        if main == word:
            print(main)
            print("you win!")
            break


name = input("Enter your name : ")
print("welcome ", name)
print("-------------")
print("Try to guess the word in 10 attempts")
hangman()
