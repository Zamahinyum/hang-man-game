"""
Wordlist Module
Handles word loading and random selection from categories.
"""

import random
from pathlib import Path


def get_categories():
    """Get list of available categories."""
    categories = ["Animals", "Countries", "Programming", "Science"]
    category_dir = Path("words/categories")
    
    if category_dir.exists():
        category_files = [f.stem for f in category_dir.glob("*.txt")]
        # Capitalize first letter to match format
        categories.extend([cat.capitalize() for cat in category_files if cat.capitalize() not in categories])
    
    return categories


def load_words_from_file(file_path):
    """Load words from a text file."""
    try:
        with open(file_path, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        return []


def load_words(category=None):
    """
    Load and return a random word from the specified category.
    If no category is specified, choose from all words.
    Returns: (word, category_name)
    """
    words = []
    selected_category = "Random"
    
    if category:
        # Try to load from specific category file
        category_file = Path(f"words/categories/{category.lower()}.txt")
        if category_file.exists():
            words = load_words_from_file(category_file)
            selected_category = category
        else:
            print(f"Category file not found: {category_file}")
    
    # If no words loaded yet, try main words file
    if not words:
        main_words_file = Path("words/words.txt")
        if main_words_file.exists():
            words = load_words_from_file(main_words_file)
            if category:
                selected_category = category if words else "Random"
    
    # If still no words, try to load from any category
    if not words:
        category_dir = Path("words/categories")
        if category_dir.exists():
            all_files = list(category_dir.glob("*.txt"))
            if all_files:
                chosen_file = random.choice(all_files)
                words = load_words_from_file(chosen_file)
                selected_category = chosen_file.stem.capitalize()
    
    if not words:
        print("Error: No words available!")
        return None, None
    
    word = random.choice(words)
    return word, selected_category