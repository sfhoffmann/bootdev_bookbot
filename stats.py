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

def char_sort(char_dict):
    sorted_chars = []
    for char in char_dict:
        sorted_chars.append(
            {"char": char, "num": char_dict[char]}
        )
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

def sort_on(chars):
    return chars["num"]