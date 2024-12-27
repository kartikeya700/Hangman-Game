import random

from hangman_words import word_list
from hangman_art import logo, stages


def main():
    lives = 6

    print(logo)

    # chooses random word from given list of words
    chosen_word = random.choice(word_list)

    # prints starting stage of hangman
    placeholder = ""
    word_length = len(chosen_word)
    for i in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

    # defines flag which is used to stop game
    flag = 1
    # stores correct and incorrect guesses made by user
    correct_guess = []
    incorrect_guess = []

    while flag:
        # takes input from user
        guess = input("Guess a letter: ").lower()

        display = ""

        # checks if input is valid or not
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        # checks if the guessed letter is in the chosen word and appends display string acc
        for letter in chosen_word:
            if letter == guess:
                display += letter
            elif letter in correct_guess:
                display += letter
            else:
                display += "_"

        # if user has already guessed the letter
        if guess in incorrect_guess or guess in correct_guess:
            print(f"You have already guessed {guess}")
        else:
            # modifies number of lives for incorrect guess
            if guess not in chosen_word:
                lives -= 1
                incorrect_guess.append(guess)
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                # if no lives remain ends game
                if lives == 0:
                    flag = 0
                    print(f"****************************IT WAS {chosen_word.upper()}! YOU LOSE****************************")
                    continue
            # to print the new word to guess if guess was correct
            else:
                print(display)
                correct_guess.append(guess)

            if "_" not in display:
                flag = 0
                print("****************************YOU WIN!****************************")

            print(stages[lives])

        print(f"****************************{lives}/6 LIVES LEFT****************************")
        print("Word to guess: " + display)


main()
