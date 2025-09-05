from stats import word_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{word_count(book_text)} words found in the document")

def get_book_text(book_file_path):
    with open(book_file_path) as book:
        return book.read()
   
main()