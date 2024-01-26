# variables that define the Number of tries and controlling the loop
tries = 6
word_guessed = False

# variables that define the letters used and the word
used_letters = []
word_to_guess = "java"
guess_list = ["_" for i in range(len(word_to_guess))]

"""
This function allows to check if the letter given by the user
is in the word that is supposed to be guessed. If it is not
the user has one try less. All of the words given by the user
are stored.
"""
def guess(letter, word, used_letters_list, guess_print_list, number_of_tries):
    used_letters_list.append(letter)
    if (letter in word):
        if word.count(letter) > 1:
            index = 0
            while index < len(word) and index != -1:
                index = word.find(letter, index)
                guess_print_list[index] = letter
                index += 1
        else:
            index = word.find(letter)
            guess_print_list[index] = letter
    else:
        number_of_tries -= 1
    return number_of_tries

"""
This loop control the times the user can input letters using
the tries and the variable that indicates if the word is already
guessed by the user. The user can only input different letters.
When the user is out of tries it is Game Over!
"""
while (tries > 0 and word_guessed == False):
    print("You have", tries, "tries left")
    print("Used letters:", ", ".join(used_letters))
    print("Word:", " ".join(guess_list))
    if "_" not in guess_list:
        print("You guessed the word", word_to_guess + "!")
        word_guessed = True
    else:
        if "_" in guess_list:
            letter_guessed = input("Guess a letter: ")
            if letter_guessed in used_letters:
                print("The letter is already in use, please try a different one")
                print("\n")
            else:
                if letter_guessed not in word_to_guess and tries == 1:
                    print("\n")
                    print("Game Over!")
                    tries = 0
                elif tries > 1:
                    print("\n")
                    tries = guess(letter_guessed, word_to_guess, used_letters, guess_list, tries)