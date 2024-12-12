
def count_words(content):
    return len(content.split())

def count_by_letters(content):
    counter = {}
    for c in content.lower():
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter

def ordered_letters_count(counter):
    items = []
    for k in counter:
        if k.isalpha():
            items.append({ "letter": k, "count": counter[k] })
    
    return sorted(items, key=lambda x: x["count"], reverse=True)

if __name__ == '__main__':

    with open('books/frankenstein.txt') as f:
        content = f.read()

        print('--- Begin report of books/frankenstein.txt ---')

        print(count_words(content))

        print()

        for item in ordered_letters_count(count_by_letters(content)):
            print(f"The '{item["letter"]}' character was found {item["count"]} times")
        print('--- End report ---')