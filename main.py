import sys
from stats import word_count, char_count, char_sort


def main():
    book_text = get_book_text(sys.argv[1])
    count = char_count(book_text)
    sorted = char_sort(count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    #print(sorted)
    for c in sorted:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

def get_book_text(book_file_path):
    with open(book_file_path) as book:
        return book.read()
try:   
    main()
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)