guessWord = 'DEVELOPMENT'
guessTimes = []
wordBoard = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
wrongLetter = 0
gameInPlay = True

def showBoard():
    while gameInPlay:
        print(wordBoard)
        guesser = input("Please enter your letter guess.").upper()
        if len(guesser) > 1:
            print("Sorry please insert one letter guess.")
        else:
            checkGuess(guesser)
        
def checkGuess(let):
    if let in guessWord:
        if let in guessTimes:
            print(f"You have already chosen {let} in the word. Try again.")
        else:
            guessTimes.append(let)
            correctLetter(let)
    else:
        if let in guessTimes:
            print(f"You have already tried {let} in the word. Try again.")
        else:
            global wrongLetter
            wrongLetter = wrongLetter + 1
            print(f"This letter is not in the word. You have {5 - wrongLetter} chances left.")
            if wrongLetter >= 5:
                global gameInPlay
                gameInPlay = False
                print("Game Over. You lose it all.")

def correctLetter(let):
    for i in range(len(guessWord)):
        if guessWord[i] == let:
            wordBoard[i] = let
        if '_' not in wordBoard:
            global gameInPlay
            gameInPlay = False
            print(wordBoard)
            print(f"Great Job! You win the game. The word was {guessWord}.")

showBoard()