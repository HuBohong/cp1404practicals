def main():
    word_to_count = {}
    user_sentence = input("Enter any sentence you like:")
    while user_sentence != "":

        words = user_sentence.strip().replace(".", "").split(" ")
        for word in words:
            word_to_count[word] = word_to_count.get(word, 0) + 1
        user_sentence = input("Enter any sentence you like:")


main()
