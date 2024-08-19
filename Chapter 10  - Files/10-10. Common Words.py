def count_words(filename, word):
    """Count word in file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
    print(f"The word {word} appears in {filename}, {word_count} times!")

filename = 'alice.txt'
count_words(filename, 'rabbit')

