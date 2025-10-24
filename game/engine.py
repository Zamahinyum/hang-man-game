"""
Game Engine Module
Contains core gameplay logic for Hangman.
"""

from ui.display import display_game_state, display_win, display_loss
from game.ascii_art import get_hangman
from pathlib import Path
from datetime import datetime


def create_log_file(game_num, category, word, guesses, wrong_guesses, result, points, total_score, stats):
    """Create a log file for the current game."""
    log_dir = Path(f"game_log/game{game_num}")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_file = log_dir / "log.txt"
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"Game {game_num} Log\n")
        f.write(f"Category: {category}\n")
        f.write(f"Word: {word}\n")
        f.write(f"Word Length: {len(word)}\n")
        f.write(f"\nGuesses (in order):\n")
        
        for i, (guess, correct) in enumerate(guesses, 1):
            status = "Correct" if correct else "Wrong"
            f.write(f"{i}. {guess} → {status}\n")
        
        f.write(f"\nWrong Guesses List: {', '.join(wrong_guesses)}\n")
        f.write(f"Wrong Guesses Count: {len(wrong_guesses)}\n")
        f.write(f"Remaining Attempts at End: {6 - len(wrong_guesses)}\n")
        f.write(f"Result: {result}\n")
        f.write(f"Points Earned: {points}\n")
        f.write(f"Total Score (after this round): {total_score}\n")
        f.write(f"Games Played: {stats['games_played']}\n")
        f.write(f"Wins: {stats['wins']}\n")
        f.write(f"Losses: {stats['losses']}\n")
        
        win_rate = (stats['wins'] / stats['games_played'] * 100) if stats['games_played'] > 0 else 0
        f.write(f"Win Rate: {win_rate:.2f}%\n")
        f.write(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")
        
        # Progress trace
        f.write("\nSession Notes:\n")
        f.write(f"- ASCII hangman reached state {len(wrong_guesses)} after {len(wrong_guesses)} wrong guess(es).\n")
        f.write("- Progress trace:\n")
        
        # Reconstruct progress
        progress = ['_'] * len(word)
        f.write(f"  {' '.join(progress)}\n")
        
        for guess, correct in guesses:
            if correct and len(guess) == 1:
                for i, letter in enumerate(word.lower()):
                    if letter == guess.lower():
                        progress[i] = letter
            f.write(f"  -> {' '.join(progress)}")
            if not correct:
                f.write(f" ({guess} wrong — no progress change)")
            f.write("\n")
        
        f.write("-" * 50 + "\n")


def calculate_score(word_length, wrong_guesses):
    """Calculate score based on word length and wrong guesses."""
    base_score = word_length * 10
    penalty = wrong_guesses * 5
    return max(0, base_score - penalty)


def validate_input(user_input, guessed_letters):
    """
    Validate user input.
    Returns: (is_valid, input_type, message)
    input_type can be: 'letter', 'word_guess', 'quit', 'invalid'
    """
    user_input = user_input.strip().lower()
    
    if not user_input:
        return False, 'invalid', "Please enter something."
    
    if user_input == 'quit':
        return True, 'quit', ""
    
    if user_input == 'guess':
        return True, 'word_guess', ""
    
    if len(user_input) > 1:
        return False, 'invalid', "Please enter only a single letter (or 'guess' for full word, 'quit' to exit)."
    
    if not user_input.isalpha():
        return False, 'invalid', "Please enter only alphabetic characters."
    
    if user_input in guessed_letters:
        return False, 'invalid', f"You already guessed '{user_input}'. Try a different letter."
    
    return True, 'letter', ""


def get_current_progress(word, guessed_letters):
    """Get the current progress of the word with guessed letters revealed."""
    return ' '.join([letter if letter.lower() in guessed_letters else '_' for letter in word])


def play_game(word, category, game_num):
    """
    Main game loop.
    Returns: (result, points) where result is 'Win' or 'Loss'
    """
    word = word.lower()
    guessed_letters = set()
    wrong_guesses = []
    max_wrong = 6
    guess_history = []  # List of (guess, is_correct) tuples
    
    print(f"\nNew word selected from '{category}' (length {len(word)})")
    
    while True:
        # Display current game state
        progress = get_current_progress(word, guessed_letters)
        display_game_state(
            progress,
            sorted(guessed_letters),
            max_wrong - len(wrong_guesses),
            get_hangman(len(wrong_guesses))
        )
        
        # Check win condition
        if '_' not in progress.replace(' ', ''):
            points = calculate_score(len(word), len(wrong_guesses))
            display_win(word, points)
            
            # Create log with updated stats
            from main import load_statistics
            stats = load_statistics()
            stats['games_played'] = game_num
            stats['wins'] += 1
            stats['total_score'] += points
            
            create_log_file(game_num, category, word, guess_history, wrong_guesses, 
                          "Win", points, stats['total_score'], stats)
            return "Win", points
        
        # Check loss condition
        if len(wrong_guesses) >= max_wrong:
            display_loss(word)
            
            # Create log with updated stats
            from main import load_statistics
            stats = load_statistics()
            stats['games_played'] = game_num
            stats['losses'] += 1
            
            create_log_file(game_num, category, word, guess_history, wrong_guesses, 
                          "Loss", 0, stats['total_score'], stats)
            return "Loss", 0
        
        # Get user input
        user_input = input("\nEnter a letter (or type 'guess' to guess full word, 'quit' to exit): ").strip()
        
        is_valid, input_type, message = validate_input(user_input, guessed_letters)
        
        if not is_valid:
            print(message)
            continue
        
        if input_type == 'quit':
            print("\nGame aborted.")
            # Create log for aborted game
            from main import load_statistics
            stats = load_statistics()
            stats['games_played'] = game_num
            stats['losses'] += 1
            
            create_log_file(game_num, category, word, guess_history, wrong_guesses, 
                          "Loss (Quit)", 0, stats['total_score'], stats)
            return "Loss", 0
        
        if input_type == 'word_guess':
            full_word = input("Enter your guess for the full word: ").strip().lower()
            if full_word == word:
                guessed_letters.update(word)
                guess_history.append((full_word, True))
                print(f"Correct! You guessed the word!")
            else:
                wrong_guesses.append(full_word)
                guess_history.append((full_word, False))
                print(f"Wrong! '{full_word}' is not the word.")
            continue
        
        # Process letter guess
        letter = user_input.lower()
        guessed_letters.add(letter)
        
        if letter in word.lower():
            guess_history.append((letter, True))
            print(f"Correct! Progress: {get_current_progress(word, guessed_letters)}")
        else:
            wrong_guesses.append(letter)
            guess_history.append((letter, False))
            print(f"Wrong! Progress: {get_current_progress(word, guessed_letters)}")