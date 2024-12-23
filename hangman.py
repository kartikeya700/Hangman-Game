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
    correct_guess = []

    while flag:
        # takes input from user
        guess = input("Guess a letter: ").lower()

        display = ""
        
        # if user has already guessed the letter 
        if guess in correct_guess:
            print(f"You have already guessed {guess}")

        # checks if the guessed letter is in the chosen word and appends display string acc
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_guess.append(guess)
            elif letter in correct_guess:
                display += letter
            else:
                display += "_"

        # modifies number of lives for incorrect guess
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            # if no lives remain end game
            if lives == 0:
                flag = 0
                print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************")
                break
        # prints the word after guess was made
        else:
            print(display)

        if "_" not in display:
            flag = 0
            print("****************************YOU WIN!****************************")
        
        # prints the hangman stage, number of lives remaining and new word to guess
        print(stages[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        print("Word to guess: " + display)


main()