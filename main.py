def main():
    path = "books/frankenstein.txt"
    content = get_file_contents(path)
    words = count_words(content)
    print(f"you have {words} in the document!")


def count_words(text):
    words = text.split()
    return len(words)

def get_file_contents(path):
    with open(path) as f:
        return f.read()


main()