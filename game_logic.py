import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def display_game_state(mistakes, secret_word, guessed_letters):
    stage_index = min(max((0, mistakes)), len(STAGES) - 1)
    print(STAGES[stage_index])
    masked = ''.join(ch if ch in guessed_letters else '_' for ch in secret_word)
    print("Word: ", ' '.join(masked))
    print("\n")

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def prompt_letter(guessed_letters):
    """
        Input validation:
      - exactly ONE character
      - alphabetical only (a–z)
      - not previously guessed
    """
    while True:
        raw = input("Guess a letter (a–z): ").strip().lower()
        if len(raw) != 1 or not raw.isalpha():
            print("Please enter exactly one alphabetical character (a–z).")
            continue
        letter = raw
        if letter in guessed_letters:
            print(f"You already guessed '{letter}'. Try another letter.")
            continue
        return letter

def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    mistakes = 0
    mistake_limit = len(STAGES) - 1
    guessed_letters = set()
    # TODO: Build your game loop here.
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        if all(ch in guessed_letters for ch in secret_word):
            print("🎉 You saved the snowman! The word was: ", secret_word)
            break
        if mistakes >= mistake_limit:
            print("💧 Oh no! The snowman melted. The word was:", secret_word)
            break
        letter = prompt_letter(guessed_letters)
        guessed_letters.add(letter)
        if letter in secret_word:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(f"✓ Nice! '{letter}' is in the word.")
            if all(ch in guessed_letters for ch in secret_word):
                print("🎉 You saved the snowman! The word was:", secret_word)
                break
        else:
            mistakes += 1
            print(f"✗ Nope! '{letter}' is not in the word.")
            if mistakes >= mistake_limit:
                print("💧 Oh no! The snowman melted. The word was:", secret_word)
                break

def   ask_replay():
    while True:
        ans = input("Play again? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")