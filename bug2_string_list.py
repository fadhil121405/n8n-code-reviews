"""
bug2_string_list.py
Berisi fungsi-fungsi manipulasi string & list.
File ini SENGAJA mengandung bug untuk keperluan testing AI agent.
"""


def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


def reverse_string(s):
    return s[::-1]


def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count


def split_and_join(s, delimiter=","):
    parts = s.split(delimiter)
    return delimiter.join(parts)


if __name__ == "__main__":
    print(add_item("apel"))
    print(add_item("jeruk"))

    try:
        print(reverse_string("hello"))
    except IndexError as e:
        print("Error di reverse_string:", e)

    print(remove_duplicates([1, 2, 2, 3, 3, 3]))
    print(count_vowels("Programming"))

    try:
        print(split_and_join("a,b,c"))
    except AttributeError as e:
        print("Error di split_and_join:", e)
        


