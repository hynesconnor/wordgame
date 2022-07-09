import pandas as p
import random as r


# colored text solution, SO
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


# import list of words, convert to list
wordList = p.read_csv("data/words.csv", header=None)
wordList = wordList[0].to_list()
gameState = True

# select random index via random package
index = r.randint(0, len(wordList) - 1)
wordChoice = wordList[index]

# list used to display results of a guess
# #: no, $: yes, *: wrong place
resultList = ["#", "#", "#", "#", "#"]
# dataframe that holds all guess results during game

guessNum = 0

#
while guessNum < 6 and gameState:
    # guess and check proper length, needs fix
    guess = input("Enter your Guess: ")
    if len(guess) > 5 or len(guess) < 5:
        while len(guess) != 5: # solves for repeated length issues
            guess = input("Enter a guess that is 5 letters long: ")
    guess = guess.lower()
    guessNum = guessNum + 1

    # logic for word comparison
    # win condition
    if wordChoice == guess:
        print(colored(0, 255, 0, wordChoice))
        print("Correct! You Win")
        gameState = False # play again

    # comparing for exact letter matches
    else:
        for i in range(len(guess)):
            if wordChoice.__contains__(guess[i]):
                resultList[i] = "*"
                if guess[i] == wordChoice[i]:
                    resultList[i] = "$"
            else:
                resultList[i] = "#"

        # prints guess and results
        print(list(guess))
        for i in range(len(guess)):
            if resultList[i] == "*":
                print(colored(255, 255, 0, guess[i]), end="")
            elif resultList[i] == "$":
                print(colored(0, 255, 0, guess[i]), end="")
            else:
                print(colored(160, 160, 160, guess[i]), end="")
        print()

# declares loss
if gameState:
    print("You lost. The word is: " + wordChoice)
