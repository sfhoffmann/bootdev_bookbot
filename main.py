import sys
import argparse
from stats import word_count, char_count, char_sort


def main():
    parser = argparse.ArgumentParser(description="Count characters in a file.")
    parser.add_argument("filename", help="Path to the file to analyze")
    parser.add_argument("--sort", "-s",
                        choices=["count", "alphabetical"],
                        default="count",
                        help="Sort results by count (default) or alphabetial")
    
    args = parser.parse_args()
    book_text = get_book_text(args.filename)
    count = char_count(book_text)
    sorted = char_sort(count, args.sort)

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
    print("Usage: python3 main.py <path_to_book> <--sort/-s count/alphabetical>")
    sys.exit(1)