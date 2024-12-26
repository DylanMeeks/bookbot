def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---\n")
    print(f"# of words: {num_words(file_contents)}")

    char_appear = num_char_appear(file_contents)
    chars = []
    for char in char_appear:
        if char.isalpha():
            chars.append({"char": char, "count": char_appear[char]})

    chars.sort(reverse=True, key=sort_on)
    for char in chars:
        print(f"The '{char["char"]}' character was found {char["count"]} times")

    print("--- End Report ---")

def num_words(text):
    words = text.split()
    return len(words)

def num_char_appear(text):
    appearences = {}
    for char in text.lower():
        if char in appearences:
            appearences[char] += 1
        else:
            appearences[char] = 1

    return appearences

main()
