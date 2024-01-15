import string


def read_file(file_path):
    """Read the content of a text file.

    Args:
        file_path (str): The path of the file to read.

    Returns:
        str: The content of the file, or an empty string if the file is not found.
    """
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return ""


def process_text(text):
    """Remove punctuation and convert to lowercase.

    Args:
        text (str): The text to process.

    Returns:
        list: A list of words in the text.
    """
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    return words


def count_word_frequency(words):
    """Count the frequency of each word in a list of words.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary of word-frequency pairs.
    """
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency


def display_word_frequency(word_frequency):
    """Display the word frequency in a formatted way.

    Args:
        word_frequency (dict): A dictionary of word-frequency pairs.
    """
    print("Word frequency:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    try:
        file_path = input("Enter the path of text file: ")
        text = read_file(file_path)

        if text:
            words = process_text(text)
            word_frequency = count_word_frequency(words)
            display_word_frequency(word_frequency)
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
