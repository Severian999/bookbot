with open("books/frankenstein.txt") as f:

    file_contents = f.read()

def word_count(book):
    count = book.split()
    return count

def char_count(book):
    # convert to lowercase
    book = book.lower()
    char_dict = {}
    for letter in book:
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    return char_dict

def make_report(words, chars):
    word_total = len(words)
    char_total = []
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} words found in the document")
    for char in chars:
        if char.isalpha():
            char_total.append(f"The '{char}' character was found {chars[char]} times")
    char_total.sort()
    for line in char_total:
        print(line)
    
    



total_words = word_count(file_contents)
total_chars = char_count(file_contents)
make_report(total_words, total_chars)