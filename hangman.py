import random


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = ("acres adult advice arrangement attempt august autumn border breeze brick calm canal casey cast chose claws coach constantly contrast cookies customs damage danny deeply depth discussion doll donkey egypt ellen essential exchange exist explanation facing film finest fireplace floating folks fort garage grabbed grandmother habit happily harry heading hunter illinois image independent instant january kids label lee lungs manufacturing martin mathematics melted memory mill mission monkey mount mysterious neighborhood norway nuts occasionally official ourselves palace pennsylvania philadelphia plates poetry policeman positive possibly practical pride promised recall relationship remarkable require rhyme rocky rubbed rush sale satellites satisfied scared selection shake shaking shallow shout silly simplest slight slip slope soap solar species spin stiff swung tales thumb tobacco toy trap treated tune university vapor vessels wealth wolf zoo").split()


def render_word(word, letters_guessed):
    for letter in word:
        if letter in letters_guessed:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")
    print("")


def get_input(letters_guessed):
    valid = False
    while not valid:
        print("Please enter your guess:")
        guess = input(">")
        if ((len(guess) == 1) and (guess.isalpha()) and guess not in letters_guessed):
            valid = True
    return guess.lower()


def print_guessed(letters_guessed):
    letters = set(letters_guessed)
    if len(letters_guessed) > 0:
        print(f"You have already guessed: {', '.join(letter for letter in letters)}")
    else:
        print("You have already guessed: Nothing")


def main():
    guesses_allowed = 6
    won = False
    print("Welcome to Hangman!\n\n")
    word = random.choice(words).lower()
    letters_guessed = []
    errors_made = 0
    while (errors_made < guesses_allowed) and not won:
        render_word(word, letters_guessed)
        print_guessed(letters_guessed)
        print(HANGMANPICS[errors_made][1::])
        print(f"You only have {guesses_allowed - errors_made} mistake(s) left!")
        guess = get_input(letters_guessed)
        letters_guessed.append(guess)
        if guess not in word:
            errors_made += 1
        else:
            if (all(x in letters_guessed for x in list(word))):
                won = True
        print("\n")
    if won:
        print("Well done! You got it!")
    else:
        print("Uh-oh! You didn't get it in time...")
    print(f"The word was {word.upper()}!")

    input("Press enter to exit")


if __name__ == "__main__":
    main()
