def print_upper_words(words, must_start_with):
    """Take list of letters and print out only the words in uppercase thatg start with those letters

    For example:
        print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'], must_start_with={"h", "y"})
        should print out:
            HELLO
            HEY
            YO
            YES
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(['hi', 'hello', 'world', 'wattup',
                  'elephant', 'eggs'], ['h'])
print_upper_words(['hi', 'hello', 'world', 'wattup',
                  'elephant', 'eggs'], ['h', 'w'])
print_upper_words(['hi', 'hello', 'world', 'WATTUP',
                  'elephant', 'eggs'], {'a', 'e'})
print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'],
                  must_start_with={"h", "y"})
