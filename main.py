from stats import word_count
from stats import char_count
from stats import char_sort

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(f"{word_count(book_text)} words found in the document")
    #print(char_count(book_text))
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
   
main()