def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_num_characters(text)
    book_report(num_words, char_counts, book_path)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_characters(text):
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts
        
def sort_on(dict):
    return dict["count"]


def book_report(num_words, char_counts, book_path):
    list_of_char_dicts = []
    
    # convert dictionary of counts to list of dictionaries so it can be sorted
    for key, value in char_counts.items():
        list_of_char_dicts.append({"char": key, "count": value})
    
    # sort the list of dictionaries using the sort_on function to sort on the 'count' key
    list_of_char_dicts.sort(reverse=True, key=sort_on)

    # print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")
    
    for char_list in list_of_char_dicts:
        #print(f"Character: {char_list['char']}, Value: {char_list['count']}")
        if char_list['char'].isalpha():
            print(f"The '{char_list['char']}' character was found {char_list['count']} times")
    
    print("--- End report ---")




main()