# Snowman-Meltdown

A simple command-line word guessing game inspired by Hangman—save the snowman by guessing the secret word before he melts! Written entirely in Python with fun ASCII snowman drawings.

## Features

- **Word Guessing Gameplay**: Guess the secret word letter by letter.
- **ASCII Art**: Visual snowman stages show your progress and mistakes.
- **Mistake Limit**: The snowman melts one stage with every wrong guess.
- **Replay Option**: Play multiple rounds in a single session.
- **Clean, Validated Input**: Only accepts valid, new alphabetical guesses.

## How to Play

- Run the game (`python snowman.py`).
- You will see an empty word; guess one letter at a time.
- Each wrong guess causes the snowman to melt one stage—don’t let him disappear!
- Win by revealing every letter before the snowman melts.
- After each game, you can choose to play again or exit.

## Project Structure

Snowman-Meltdown/  
├── ascii_art.py # ASCII snowman stages  
├── game_logic.py # Game rules and main loop  
├── snowman.py # Entry-point script  
├── README.md # Project documentation  
└── **pycache**/ # Python cache files (ignore)

## Code Overview

- **ascii_art.py**: Defines the list of ASCII art snowman stages that visually represent player progress.
- **game_logic.py**: Contains the full word guessing logic, input validation, victory/defeat conditions, and replay prompt.
- **snowman.py**: Runs the game loop; imports game logic and kicks things off.

## Requirements

- Python 3.x (no extra dependencies)

## Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/Miami05/Snowman-Meltdown.git
```
```bash
cd Snowman-Meltdown
```

2. **Run the game:**
```
python snowman.py
```

## Customization

You can expand the game by:
- Adding more words to `WORDS` in `game_logic.py`.
- Creating additional snowman stages for smoother melting animation.
- Enhancing gameplay or scoring options.

## License

This game is licensed under the MIT License.

Enjoy saving snowmen from the meltdown!
