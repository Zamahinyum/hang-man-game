"""
Display Module
Handles all user interface and display functions.
"""


def display_welcome():
    """Display welcome message."""
    print("=" * 50)
    print("        WELCOME TO HANGMAN!")
    print("=" * 50)
    print("Guess the word one letter at a time.")
    print("You have 6 wrong guesses before you lose!")
    print("=" * 50)


def display_menu():
    """Display main menu and return user choice."""
    print("\n" + "=" * 50)
    print("MAIN MENU")
    print("=" * 50)
    print("1. Play Game")
    print("2. View Statistics")
    print("3. Quit")
    print("=" * 50)
    return input("Enter your choice (1-3): ").strip()


def display_game_state(progress, guessed_letters, remaining_attempts, hangman_art):
    """Display current game state."""
    print("\n" + "=" * 50)
    print(progress)
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    print(f"Remaining attempts: {remaining_attempts}")
    print(hangman_art)
    print("=" * 50)


def display_win(word, points):
    """Display win message."""
    print("\n" + "=" * 50)
    print("*** CONGRATULATIONS! YOU WIN! ***")
    print("=" * 50)
    print(f"Word: {word}")
    print(f"Points earned this round: {points}")
    print("=" * 50)


def display_loss(word):
    """Display loss message."""
    print("\n" + "=" * 50)
    print("*** GAME OVER - YOU LOST! ***")
    print("=" * 50)
    print(f"The word was: {word}")
    print("Better luck next time!")
    print("=" * 50)


def display_statistics(stats):
    """Display game statistics."""
    games_played = stats.get("games_played", 0)
    wins = stats.get("wins", 0)
    losses = stats.get("losses", 0)
    total_score = stats.get("total_score", 0)
    
    win_rate = (wins / games_played * 100) if games_played > 0 else 0
    avg_score = (total_score / games_played) if games_played > 0 else 0
    
    print("\n" + "=" * 50)
    print("GAME STATISTICS")
    print("=" * 50)
    print(f"Games Played: {games_played}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Total Score: {total_score}")
    print(f"Average Score per Game: {avg_score:.2f}")
    print("=" * 50)