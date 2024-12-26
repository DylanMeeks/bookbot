def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(f"# of words: {num_words(file_contents)}")

    char_appear = num_char_appear(file_contents)
    print(char_appear)

def num_words(text):
    words = text.split()
    return len(words)

def num_char_appear(text):
    appearences = {}
    for char in text.lower():
        appearences[char] += 1

    return appearences

main()
