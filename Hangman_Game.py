import random

# List of words to choose from , you can add whatever you want but in string
words = ['python', 'javascript', 'css', 'java', 'csharp', 'swift', 'hasnat']

# Hangman diagram representation manually
hangman_diagrams = [
    '''
       ------
       |    |
       |    
       |   
       |    
       |    
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   
       |    
       |    
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |    |
       |    
       |    
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|
       |    
       |    
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |    
       |    
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |    
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
    --------
    '''
]


def play_game():
    # Choose a random word from the list
    word = random.choice(words)

    # Create a list of underscores for the word
    guesses = ['_'] * len(word)

    # Set the number of incorrect guesses allowed
    max_incorrect_guesses = len(hangman_diagrams) - 1

    # Keep track of incorrect guesses
    incorrect_guesses = 0

    # Keep track of the letters already guessed
    letters_guessed = []

    # Game loop
    while True:
        # Print the current state of the game
        print(hangman_diagrams[incorrect_guesses])
        print(' '.join(guesses))
        print(f'Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}')
        print(f'Letters guessed: {", ".join(letters_guessed)}')

        # Check if the player has won
        if ''.join(guesses) == word:
            print(f'Congratulations! You guessed the word "{word}"!')
            break

        # Check if the player has lost
        if incorrect_guesses >= max_incorrect_guesses:
            print(f'Sorry, you ran out of guesses. The word was "{word}".')
            break

        # Get a guess from the player
        guess = input('Guess a letter: ').lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
            continue

        # Check if the letter has already been guessed
        if guess in letters_guessed:
            print('You already guessed that letter. Try again.')
            continue

        # Add the letter to the list of guessed letters
        letters_guessed.append(guess)

        # Check if the letter is in the word
        if guess in word:
            # Update the guesses list with the correctly guessed letter(s)
            for i in range(len(word)):
                if word[i] == guess:
                    guesses[i] = guess
        else:
            # Increment the incorrect guess count
            incorrect_guesses += 1


def main():
    while True:
        play_game()

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (c for continue, q for quit): ").lower()
        if play_again == 'q':
            print("Thanks for playing!")
            break
        elif play_again != 'c':
            print("Invalid input. Exiting...")
            break


# Start the game
main()