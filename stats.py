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

def char_sort(char_dict, sort_by):
    sorted_chars = []
    for char in char_dict:
        sorted_chars.append(
            {"char": char, "num": char_dict[char]}
        )
    sort_key = gen_sort_key(sort_by)
    if sort_by == "alphabetical":
        sorted_chars.sort(key=sort_key)
    else:
        sorted_chars.sort(reverse=True, key=sort_key)
    return sorted_chars

def gen_sort_key(sort_param):
    def sort_on(chars):
        if sort_param == "count":
            return chars["num"]
        elif sort_param == "alphabetical":
            return chars["char"]
    return sort_on