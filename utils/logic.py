def calculate_speed(typed_text, time_taken):
    """
    Calculate typing speed in words per minute.

    Args:
        typed_text (str): The text typed by the user.
        time_taken (float): The time taken to type the text in seconds.

    Returns:
        float: The typing speed in words per minute.
    """
    word_count = len(typed_text.split())
    words_per_minute = (word_count / time_taken) * 60
    return words_per_minute

def calculate_accuracy(sample_text, typed_text):
    """
    Calculate the accuracy of the typed text compared to the sample text.

    Args:
        sample_text (str): The sample text provided to the user.
        typed_text (str): The text typed by the user.

    Returns:
        float: The accuracy percentage.
    """
    sample_words = sample_text.split()
    typed_words = typed_text.split()

    correct_words = 0
    for sample_word, typed_word in zip(sample_words, typed_words):
        if sample_word == typed_word:
            correct_words += 1

    accuracy = (correct_words / len(sample_words)) * 100
    return accuracy