import sys
from stats import word_count
from stats import character_count
from stats import sort_on

def main(filepath):
    text = get_book_text(filepath)
    number_words = word_count(text)
    number_characters = character_count(text)
    sorted_list = sort_on(number_characters)
    
    print('============ BOOKBOT ============'
        '\nAnalyzing book found at books/frankenstein.txt...'
        '\n----------- Word Count ----------'
        f'\nFound {number_words} total words'
        '\n--------- Character Count -------')
    for item in sorted_list:
        character = item["character"]
        count = item["count"]
        if character.isalpha():
            print(f'{character}: {count}')
    print('============= END ===============')
        
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

inputs = sys.argv

if len(inputs) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(inputs[1])




