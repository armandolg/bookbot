def get_num_words(book_text):
    num_words = len(book_text.split())
    return f"Found {num_words} total words"

def character_count(book_text):
    lower_text = book_text.lower()
    dictionary_count = {}
    for i in lower_text:
        if i not in dictionary_count:
            dictionary_count[i] = 1
        else:
            dictionary_count[i] += 1
    return dictionary_count

def sort_on(item):
    return item["num"]

def sorted_chars(char_dict):
    sorted_list = []
    for i in char_dict:
        count = char_dict[i]
        sorted_list.append({"char": i, "num": count})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list