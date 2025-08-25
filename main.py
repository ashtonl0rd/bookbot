import sys

from stats import count_words_in_book, count_of_each_character, sorted_dictionary_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # print(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at path:", sys.argv[1])
    print("----------- Word Count ----------")
    print(count_words_in_book(sys.argv[1]))
    print("--------- Character Count -------")
    # print(count_of_each_character())
    char_report = sorted_dictionary_list(count_of_each_character(sys.argv[1]))
    for r in char_report:
        print(f"{r['char']}: {r['num']}")
main()