def main():
    word_to_count = {}
    user_sentence = input("Enter any sentence you like:")
    while user_sentence != "":

        words = user_sentence.strip().replace(".", "").split(" ")
        for word in words:
            word_to_count[word] = word_to_count.get(word, 0) + 1
        user_sentence = input("Enter any sentence you like:")
    word_width = max(len(word) for word in word_to_count.keys())
    count_width = max(len(count) for count in word_to_count.values())

    print("Text: this is a collection of words of nice words this is a fun thing it is")
    for word, count in sorted(word_to_count.items()):
        print(f"{word:{word_width}}:{count: {count_width}}")


main()
