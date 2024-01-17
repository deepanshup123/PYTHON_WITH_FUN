# Creating the Word Puzzle Game like a Begginer

# this is list of guessing the word from letters

letters = [
    ['h', 'o', '1', 'i', 'd', 'a', 'y'],
    ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i','n','g'],
    ['b', 'o', 'o', 't', 'c', 'a', 'm', 'p'],
    ['f', '1', 'o', 'w', 'c', 'h', 'a', 'r', 't'],
    ['w', 'o', 'r', 'd', 's', 'c', 'a', 'p','e', 's']
]
words = [
    ["hi", "hay", "day", "had", "lay", "dal", "lad", "lid", "hold", "lady", "hail"],
    ["go", "an", "in", "no", "on", "map", "mom", "gap", "gag", "pig", "man", "ping",
    "pong", "pram", "prom", "ramp", "pair", "ring", "aim"],
    ["am", "at", "to", "cab", "cap", "cob", "cop", "map", "тор", "act", "bat", "camp", "comb", "boom", "pact", "atom"],
    ["of", "at", "or", "to", "caw", "cow", "how", "who", "calf", "claw", "flaw", "flow", "fowl", "wolf", "crow", "half"],
    ["we", "do", "as", "cap", "caw", "cop", "cow", "paw", "cod", "dew", "pad", "cape", "cope", "crap", "crew", "crop", "pace"]
]

score = 0
lives = 5
right = 0
guessWord = []

count = 0

while count < len(letters):
    if score > 0:
            userConfirmation = input("Do You Want to Go the Next Level(Y/N) : ")
            try:
                if userConfirmation == "y" or userConfirmation =="Y":
                    pass
                elif userConfirmation == "n" or userConfirmation == "N":
                    print("Thanks For Playing the Game!!")
                    print(score)
                    break
                else:
                    break
            except ValueError:
                print("Please Enter Only (Y/N)")
    print("Level {}".format(count + 1))
    print("Create the Three Words Using given Of these letters")
    for i in letters[count]:
        print(i, end="\t")
    print()
    guess = True
    while guess:
        if right >= 3:
            guess = False
            score += 3
            break

        if lives <= 0:
            guess = False
            break
        
        userGuessedWord = input("Word : ").lower()
        if userGuessedWord in words[count] and userGuessedWord not in guessWord:
            guessWord.append(userGuessedWord)
            right += 1
        else:
            print("Wrong Guess")
            lives -= 1
        
    if lives <= 0:
        # print("Thanks For Playing the Game!!")
        # print("Score : {}".format(score))
        break
    else:
        pass
    right = 0
    count += 1
    guessWord = []

print("Thanks For Playing the Game!!")
print("score:", score)