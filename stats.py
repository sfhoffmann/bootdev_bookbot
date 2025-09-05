def word_count(book_text):
    return len(book_text.split())

def char_count(book_text):
    lower_book_text = book_text.lower()
    chars = {}
    for char in lower_book_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars    