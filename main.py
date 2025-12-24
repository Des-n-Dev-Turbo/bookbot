import sys
from stats import get_num_words, get_num_letters, get_sorted_letter_counts

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    book_text = get_book_text(file_path)
    letters_count = get_num_letters(book_text)
    sorted_letters = get_sorted_letter_counts(letters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    get_num_words(book_text)
    print("--------- Character Count -------")
    for letter_info in sorted_letters:
        char = letter_info["char"]
        num = letter_info["num"]
        print(f"{char}: {num}")
    print("============ END ===============")

main()