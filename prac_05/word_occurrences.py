def main():
    user_sentence = input("Enter any sentence you like:")
    words = user_sentence.strip().replace(".","").split(" ")
    word_to_count = {}
    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1



main()
