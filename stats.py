def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_num_letters(text):
    lower_text = text.lower()
    letters_count = {}

    for char in lower_text:
        if char.isalpha():
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1
    
    return letters_count

def sort_on(items):
    return items["num"]

def get_sorted_letter_counts(letters_dictionary):
    sorted_letters = []
    for letter in letters_dictionary:
        sorted_letters.append({ "char": letter, "num": letters_dictionary[letter] })

    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters
