Hangman Game

A classic implementation of the Hangman word guessing game in Python.

Description
Hangman is a word guessing game where players try to guess a hidden word letter by letter. Each incorrect guess brings the player one step closer to being "hanged" (losing the game). The player wins by guessing all the letters in the word before running out of lives.
This implementation features:

Random word selection from a predefined word list
ASCII art for the hangman stages
Visual feedback on game progress
6 lives (attempts) to guess the word

Files

game.py - The main game script,
words_for_game.py - Contains the list of words to choose from,
game_visuals.py - Contains ASCII art for the game logo and hangman stages

How to Play
Run the game using Python:
python game.py

The game will select a random word and display it as underscores.
Guess a letter by typing it and pressing Enter.
If your guess is correct, the letter will be revealed in the word.
If your guess is wrong, you lose a life and the hangman drawing progresses.
Continue guessing until you either:

Correctly guess all the letters in the word (you win!)
Run out of lives (you lose!)



Game Rules

You have 6 lives (incorrect guesses) before you lose
Only single letter guesses are accepted
Repeated guesses of the same letter are identified and won't cost you a life
All words are in lowercase

Requirements

Python 3.x
No additional packages needed

Sample Game Output
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

Word to guess: _ _ _ _
****************************6/6 LIVES LEFT****************************
Guess a letter: a
You guessed a, that's not in the word. You lose a life

Word to guess: _ _ _ _
  +---+
  |   |
  O   |
      |
      |
      |
=========
****************************5/6 LIVES LEFT****************************
Future Improvements
Potential enhancements for the game:

Difficulty levels (different word lengths or categories)
Score tracking
Hint system
Graphical user interface
