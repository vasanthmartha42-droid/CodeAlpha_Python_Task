********hangman.py************
import random

def play_hangman():
    words = ["python", "hangman", "developer", "programming", "keyboard"]
    word = random.choice(words)
    
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    
    while wrong_guesses < max_wrong:
        # Build the display string (letter if guessed, else underscore)
        display = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print("\nWord: " + display)
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        
        # Check win condition
        if "_" not in display:
            print("\n🎉 You won! The word was:", word)
            return
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")
    
    print("\n💀 You lost! The word was:", word)

if __name__ == "__main__":
    play_hangman()
