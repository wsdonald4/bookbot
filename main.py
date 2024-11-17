def main():
    path = "books/frankenstein.txt"
    content = get_file_contents(path)
    words = count_words(content)
    count = dictionary(content)
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    sorted_list = char_dict(count)
    
    for item in sorted_list:
        if not item["ch"].isalpha():
            continue
        print(f"The '{item['ch']}' character was found '{item['num']}' times")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def get_file_contents(path):
    with open(path) as f:
        return f.read()
    
def sort_on(dict):
    return dict["num"]

def char_dict(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"ch": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def dictionary(text):
    lowered_words = text.lower()
    diction = {}

    for word in lowered_words:
        if word in diction:
            diction[word] += 1
        else:
            diction[word] = 1
    return diction

main()