def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(num_words(file_contents))

def num_words(text):
    words = text.split()
    return len(words)

main()
