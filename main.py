from stats import *
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    def get_book_text(filepath):
        with open(filepath) as file:
            return file.read()
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(get_num_words(get_book_text(book_path)))
    print("--------- Character Count -------")
    sorted = sorted_chars(character_count(get_book_text(book_path)))
    for i in sorted:
        if i["char"].isalpha():
            print(i["char"]+":",i["num"])
    print("============= END ===============")

main()