
import random
from words_for_game import word_list
from game_visuals import logo

lives = 6
# Displays the game logo
print(logo)
# Chooses a random word from the word_list
chosen_word = random.choice(word_list)

# Initializes empty placeholder string
placeholder = ""
# Gets the length of the chosen word
word_length = len(chosen_word)
# Creates a placeholder with underscores for each letter in the chosen word
for position in range(word_length):
    placeholder += "_"
# Displays the initial placeholder
print("Word to guess: " + placeholder)
# Initializes game state variable
game_over = False
# List to track correctly guessed letters
correct_letters = []

# Main game loop continues until game_over becomes True
while not game_over:
    
    # Displays the current number of lives remaining
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    # Gets letter input from the player and converts to lowercase
    guess = input("Guess a letter: ").lower()
    
    # Checks if the letter has been guessed correctly before
    if guess in correct_letters:
        print(f"You have already guessed letter {guess}")
    
    # Creates a new display string to show progress
    display = ""
    # Iterates through each letter in the chosen word
    for letter in chosen_word:
        # If the letter matches the current guess, displays the letter
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        # If the letter has already been guessed correctly before, displays the letter
        elif letter in correct_letters:
            display += letter
        # Otherwise displays an underscore for unknown letters
        else:
            display += "_"
    # Shows the updated display
    print("Word to guess: " + display)
    
    # Handles incorrect guesses
    if guess not in chosen_word:
        # Decreases remaining lives by 1
        lives -= 1
        # Informs player their guess was incorrect
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        # Checks if player has run out of lives
        if lives == 0:
            # Ends the game if no lives remain
            game_over = True
            # Shows the correct word
            print(f"The word you failed to guess was {chosen_word}")
            # Displays losing message
            print(f"***********************YOU LOSE**********************")
    
    # Checks for win condition (no more underscores in display)
    if "_" not in display:
        # Ends the game if all letters have been guessed
        game_over = True
        # Displays winning message
        print("****************************YOU WIN****************************")
    
    # Imports the ASCII art stages from hangman_art module
    from hangman_art import stages
    # Displays the current hangman stage based on lives remaining
    print(stages[lives])
