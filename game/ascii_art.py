"""
ASCII Art Module
Contains hangman drawings for different game states.
"""


def get_hangman(wrong_count):
    """
    Return ASCII art for hangman based on number of wrong guesses.
    wrong_count ranges from 0 to 6.
    """
    stages = [
        # Stage 0: No wrong guesses
        """
   +---+
   |   |
       |
       |
       |
       |
=========
        """,
        # Stage 1: Head
        """
   +---+
   |   |
   O   |
       |
       |
       |
=========
        """,
        # Stage 2: Body
        """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
        """,
        # Stage 3: Left arm
        """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
        """,
        # Stage 4: Right arm
        """
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========
        """,
        # Stage 5: Left leg
        """
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========
        """,
        # Stage 6: Right leg (game over)
        """
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========
        """
    ]
    
    if wrong_count < 0 or wrong_count > 6:
        wrong_count = 0
    
    return stages[wrong_count]