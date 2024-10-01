import random

sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The only thing we have to fear is fear itself."
]

def get_random_text():
    """
    Get a random sample text from the predefined list.

    Returns:
        str: A randomly selected sample text.
    """
    return random.choice(sample_texts)