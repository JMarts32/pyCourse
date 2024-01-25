# variables that define the Number of tries and controlling the loop
tries = 6
word_guessed = False

# variables that define the letters used and the word
used_letters = []
word = "hangman"
guess = "_  " * len(word)

def guess(letter, word):
    word.find(letter)

while (tries > 0 or word_guessed):
    print("You have", tries, "tries left")
    print("Used letters:", ", ".join(used_letters))

    letter_guessed = input("Guess a letter: ")