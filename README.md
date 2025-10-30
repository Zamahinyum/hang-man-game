# Hangman Game

A terminal-based Hangman game implemented in Python with a modular project structure, featuring categories, scoring, persistent statistics, and ASCII art.

## Features

- **Multiple Categories**: Choose from Animals, Countries, Programming, or Science
- **Large Word Database**: Over 1000 words across all categories
- **Scoring System**: Earn points based on word length and performance
- **Persistent Statistics**: Track games played, wins, losses, win rate, and scores
- **Game Logging**: Automatic logging of each game session with detailed information
- **ASCII Art**: Visual hangman representation that updates with each wrong guess
- **Input Validation**: Robust validation for user inputs
- **Full Word Guessing**: Option to guess the entire word at once

## Project Structure

```
hangman_game/
├── main.py                 # Entry point - game flow control
├── words/
│   ├── words.txt          # Main wordlist (1000+ words)
│   └── categories/
│       ├── animals.txt    # Animal words
│       ├── countries.txt  # Country names
│       ├── programming.txt # Programming terms
│       └── science.txt    # Science terms
├── game/
│   ├── engine.py          # Core gameplay logic
│   ├── wordlist.py        # Word loading and selection
│   └── ascii_art.py       # Hangman ASCII art drawings
├── ui/
│   └── display.py         # Display functions and UI
├── game_log/              # Auto-generated game logs
│   ├── game1/
│   │   └── log.txt
│   ├── game2/
│   │   └── log.txt
│   └── statistics.json    # Persistent game statistics
└── README.md
```

## How to Run

1. **Clone or download** the project to your local machine

2. **Navigate** to the `hangman_game` directory:
   ```bash
   cd hangman_game
   ```

3. **Run the game**:
   ```bash
   python main.py
   ```

4. **Follow the on-screen prompts** to play!

## Gameplay Instructions

1. **Choose an option** from the main menu:
   - Play Game
   - View Statistics
   - Quit

2. **Select a category** (or press Enter for a random word from all categories)

3. **Guess letters** one at a time:
   - Enter a single letter to guess
   - Type `guess` to guess the full word
   - Type `quit` to exit the current game

4. **Win or lose**:
   - Win by revealing all letters before 6 wrong guesses
   - Lose if you make 6 wrong guesses

## Wordlist Format

- **Main wordlist**: `words/words.txt` contains 1000+ words (one per line)
- **Category files**: Located in `words/categories/`, each contains words specific to that category
- All words are lowercase, one word per line
- No special characters or spaces in words

## Categories

The game includes four main categories:

1. **Animals**: Various animals, birds, reptiles, and sea creatures
2. **Countries**: Country names and territories from around the world
3. **Programming**: Programming languages, frameworks, tools, and concepts
4. **Science**: Chemistry, biology, physics terms and concepts

## Scoring Method

Points are calculated based on:
- **Base Score**: Word length × 10
- **Penalty**: Wrong guesses × 5
- **Formula**: `(word_length × 10) - (wrong_guesses × 5)`

**Example**: 
- Word: "python" (length 6)
- Wrong guesses: 2
- Score: (6 × 10) - (2 × 5) = 60 - 10 = **50 points**

## Statistics Tracked

The game tracks the following statistics across all sessions:
- **Games Played**: Total number of games
- **Wins**: Number of games won
- **Losses**: Number of games lost
- **Win Rate**: Percentage of games won
- **Total Score**: Cumulative score across all games
- **Average Score per Game**: Mean score per game

Statistics are stored in `game_log/statistics.json` and persist between sessions.

## Game Logs

Each game automatically creates a log file in `game_log/gameN/log.txt` containing:
- Game number
- Selected category and word
- Word length
- All guesses in order (marked as correct/wrong)
- List of wrong guesses
- Wrong guess count
- Remaining attempts at game end
- Final result (Win/Loss)
- Points earned
- Updated total score
- Updated statistics
- Timestamp
- Session notes with progress trace

Logs are created automatically and never overwritten.

## ASCII Art States

The hangman has 7 states (0-6 wrong guesses):
- **State 0**: Empty gallows
- **State 1**: Head
- **State 2**: Body
- **State 3**: Left arm
- **State 4**: Right arm
- **State 5**: Left leg
- **State 6**: Right leg (Game Over)

## Technical Details

- **Python Version**: Compatible with Python 3.6+
- **Dependencies**: None (uses only Python standard library)
- **Path Management**: Uses `pathlib` for cross-platform compatibility
- **File Operations**: Automatic directory creation with `mkdir(parents=True, exist_ok=True)`
- **Modularity**: Each module has a clear, single responsibility

## Module Responsibilities

- **main.py**: Entry point, orchestrates game flow, manages statistics
- **game/engine.py**: Core game logic, input validation, score calculation, logging
- **game/wordlist.py**: Loads words from files, handles category selection
- **game/ascii_art.py**: Provides ASCII art for different game states
- **ui/display.py**: All display and print functions for user interface

## Development Notes

- All file operations use `pathlib` for platform independence
- Game logs are human-readable text files
- No external dependencies required
- Modular design allows easy extension and modification.

## License

This project is created for educational purposes.

---

**Enjoy playing Hangman!** 🎮
