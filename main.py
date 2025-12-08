import sys
from stats import word_count, character_count, sort_on, print_result_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    book_path = "books/frankenstein.txt"
    book = (get_book_text(book_path))
    number_of_words = word_count(book)
    character_dict = character_count(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    sorted_dict = (print_result_dict(character_dict))
    for item in sorted_dict:
        print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()