import random, sys, time

color = sys.stdout.shell
color.write("\nWelcome to Wordle! \nYou can begin guessing now!\n\n", "NORMAL")

WORDLIST = []

words = open("C:/Users/rsmit/Repos/Wordle-Python/words.txt", "r")
valid_guesses = open("C:/Users/rsmit/Repos/Wordle-Python/valid_guesses.txt", "r")

for line in words:
    WORDLIST.append(str.rstrip(line))
    
valid_string = ""
for line in valid_guesses:
    valid_string += line
VALIDLIST = valid_string.split(' ')

def is_valid(guess):
    ''' Check for validity of input '''
    if guess.upper() not in VALIDLIST:
        return False
    return True

def choose_word():
    ''' Select a random word from the list '''
    index = random.randint(0, len(WORDLIST) - 1)
    return WORDLIST[index]

def get_guess(i):
    ''' Get a valid guess from the user '''
    color.write(str(i + 1) + ": ")
    guess = input()
    if is_valid(guess):
        return guess
    else:
        print("Not in word list.")
        return get_guess(i)

def fill_boxes(guess, answer):
    ''' Fill the boxes with the correct colour '''
    print()
    for i in range(len(guess)):
        time.sleep(0.2)
        if guess[i] == answer[i].casefold():
            color.write(guess[i].upper() + " ", "STRING")
        elif guess[i] in answer.casefold():
            color.write(guess[i].upper() + " ", "KEYWORD")
        else:
            color.write(guess[i].upper() + " ", "NORMAL")
    print("\n")
    if guess.casefold() == answer.casefold():
        color.write("You have guessed the word.", "STRING")
        sys.exit(0)

def play():
    ''' Play the game '''
    answer = choose_word()
    for i in range(6):
        guess = get_guess(i)
        fill_boxes(guess, answer)
    color.write("Sorry, the word was " + answer + ".", "COMMENT")

play()
