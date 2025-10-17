"""
CP1404/CP5632 Practical 5
word occurrences program
estimate: 20min
actual: 1h (bug fix spend longer)
"""

def main():
    """Main function to count word occurrences."""
    word_to_count = {}
    get_format_sentence(word_to_count)
    word_width, count_width = get_format_width(word_to_count)
    count_word(word_to_count, word_width, count_width)


def get_format_sentence(word_to_count):
    """Get user sentence and count word occurrences."""
    user_sentence = input("Enter any sentence you like:")
    while user_sentence != "":
        words = user_sentence.strip().replace(".", "").split(" ")
        for word in words:
            word_to_count[word] = word_to_count.get(word, 0) + 1
        user_sentence = input("Enter any sentence you like:")


def get_format_width(word_to_count):
    """Get the width for formatting output."""
    if len(word_to_count) > 0:
        word_width = max(len(word) for word in word_to_count.keys())
        count_width = max(len(str(count)) for count in word_to_count.values())
    else:
        word_width = 0
        count_width = 0
    return word_width, count_width


def count_word(word_to_count, word_width, count_width):
    """Print word occurrences in formatted way."""
    print("Text: this is a collection of words of nice words this is a fun thing it is")
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{word_width}}:{count: {count_width}}")


main()
