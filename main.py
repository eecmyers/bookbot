import sys
from stats import countwords, unique_char_cnt, get_book_text,sort_my_dict, sort_on, print_my_list

def main(book_path):
    text = get_book_text(book_path)
    num_words = countwords(text)
    print("============BOOKBOT===========")
    print(f"Analyzing book found at {book_path}...")
    print("--------Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------Character Count-------")
    unsorted_dict = unique_char_cnt(text)
    my_new_dict = sort_my_dict(unsorted_dict)
    my_new_dict.sort(reverse = True, key=sort_on)
    print_my_list(my_new_dict)



if len(sys.argv) != 2:
    print("Requires bookpath arguemment, Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])


