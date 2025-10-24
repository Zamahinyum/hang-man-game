"""
Hangman Game - Main Entry Point
This module serves as the entry point for the Hangman game.
It orchestrates the game flow by calling functions from other modules.
"""

from game.engine import play_game
from game.wordlist import load_words, get_categories
from ui.display import display_welcome, display_statistics, display_menu
from pathlib import Path
import json


def load_statistics():
    """Load game statistics from file."""
    stats_file = Path("game_log/statistics.json")
    if stats_file.exists():
        with open(stats_file, 'r') as f:
            return json.load(f)
    return {
        "games_played": 0,
        "wins": 0,
        "losses": 0,
        "total_score": 0
    }


def save_statistics(stats):
    """Save game statistics to file."""
    stats_file = Path("game_log/statistics.json")
    stats_file.parent.mkdir(parents=True, exist_ok=True)
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=4)


def main():
    """Main game loop."""
    display_welcome()
    stats = load_statistics()
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            # Play game
            categories = get_categories()
            print("\nAvailable categories:", ", ".join(categories))
            category = input("Choose a category (or press Enter for random): ").strip()
            
            if category and category not in categories:
                print(f"Invalid category. Using random word.")
                category = None
            
            word, selected_category = load_words(category)
            
            if not word:
                print("Error loading word. Please try again.")
                continue
            
            result, points = play_game(word, selected_category, stats["games_played"] + 1)
            
            # Update statistics
            stats["games_played"] += 1
            if result == "Win":
                stats["wins"] += 1
            else:
                stats["losses"] += 1
            stats["total_score"] += points
            
            save_statistics(stats)
            display_statistics(stats)
            
        elif choice == '2':
            # View statistics
            display_statistics(stats)
            
        elif choice == '3':
            # Quit
            print("\nThanks for playing Hangman! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()