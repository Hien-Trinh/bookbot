def main():
    book_path = "books/frankenstein.txt"
    book_string = getFileText(book_path)
    book_word_count = getWordCount(book_string)
    book_character_count = getCharacterCount(book_string)
    print(f"--- Begin report of {book_path} ---")
    print(f"{book_word_count} words found in the document\n")
    printCharacterCount(book_character_count)
    print("--- End report ---")

def getFileText(path: str) -> str:
    with open(path) as f:
        return f.read()

def getWordCount(string: str) -> int:
    return len(string.split())

def getCharacterCount(string: str) -> dict:
    character_count = {}
    for char in string:
        lowered_char = char.lower()
        if lowered_char in character_count:
            character_count[lowered_char] += 1
        else:
            character_count[lowered_char] = 1

    return character_count

def printCharacterCount(character_count: dict) -> None:
    sorted(character_count, key = lambda x: character_count[x])
    for char in sorted(character_count, key = character_count.get, reverse = True):
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {character_count[char]} times")

    return

main()