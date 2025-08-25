def get_book_text(filepath):
    with open(filepath) as f:
        filepath_content = f.read()
    return filepath_content

def count_words_in_book(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def count_of_each_character(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split()
    convert_to_lowercase = [word.lower() for word in words]
    char_count = {}
    for word in convert_to_lowercase:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_dictionary_list(char_count):
    sorted_list = list(char_count.items())
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    result_list = []
    for s in sorted_list:
        if s[0].isalpha():
            new_dict = {"char": s[0], "num": s[1]}
            result_list.append(new_dict)
    return result_list
