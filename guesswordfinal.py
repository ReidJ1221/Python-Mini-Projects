import random
secret_words = ["joshua", "van", "rufus", "randolph", "crow", "elaine"]
picked_word = random.choice(secret_words)
dashes = "-"*len(picked_word)
guesses_left = 10
guessed_letters = set()

def get_guess():
    while True:
        guess = input("Guess a letter: ")
        if not guess.isalpha():
            print("Please enter a letter instead of something else")
        elif guess.isupper():
            print("Please enter a lowercase letter")
        elif len(guess) > 1:
            print("Please enter only one letter. ")
        elif guess.isdigit():
            print("Please enter a letter instead of a number")
        else:
            return guess

def update_dashes(picked_word, dashes, guess):
    result = ""
    for i in range(len(picked_word)):
        if picked_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result

try:
    while guesses_left > 0:
        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            print(f"You have {guesses_left} guesses left")
            print(dashes)
            continue

        guessed_letters.add(guess)

        if guess in picked_word:
            print("That guess is in the secret word.")
            print(f"You have {guesses_left} guesses left")
            dashes = update_dashes(picked_word, dashes, guess)
            print(dashes)
            guessed_letters.add(guess)

        else:
            guesses_left -= 1
            print("Try again, guess is not in the secret word.")
            print(f"You have {guesses_left} guesses left")
            print(dashes)

        if "-" not in dashes:
            print(f"You won, the secret word was {picked_word}.")
            break
        elif guesses_left == 0:
            print(f"You lost! The secret word was {picked_word}.")
            break
except KeyboardInterrupt:
    print("Forced game closure!")