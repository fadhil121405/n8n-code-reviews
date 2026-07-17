"""
bug2_string_list.py
Berisi fungsi-fungsi manipulasi string & list.
File ini SENGAJA mengandung bug untuk keperluan testing AI agent.
"""


def add_item(item, items=None):
    # BUG KLASIK: mutable default argument.
    # List 'items' akan terus "nempel" antar pemanggilan fungsi,
    # bukan list baru setiap kali dipanggil.
    if items is None:
        items = []
    items.append(item)
    return items


def reverse_string(s):
    result = s[::-1]
    return result


def remove_duplicates(items):
    unique = []
    for item in items:
        # BUG: seharusnya "not in", tapi ditulis "in" tanpa negasi
        # sehingga logikanya kebalik, hasil malah cuma nyimpen duplikat
        if item not in unique:
            unique.append(item)
    return unique


def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        # BUG: tidak di-lowercase dulu, jadi huruf vokal kapital (A, E, I, O, U) tidak terhitung
        if char.lower() in vowels:
            count += 1
    return count


def split_and_join(s, delimiter=","):
    parts = s.split(delimiter)
    # BUG: salah urutan argumen join, harusnya delimiter.join(parts)
    return delimiter.join(parts)


if __name__ == "__main__":
    print(add_item("apel"))          # ['apel']
    print(add_item("jeruk"))         # seharusnya ['jeruk'], tapi jadi ['apel', 'jeruk']

    try:
        print(reverse_string("hello"))
    except IndexError as e:
        print("Error di reverse_string:", e)

    print(remove_duplicates([1, 2, 2, 3, 3, 3]))  # seharusnya [1,2,3]
    print(count_vowels("Programming"))            # seharusnya 3

    try:
        print(split_and_join("a,b,c"))
    except AttributeError as e:
        print("Error di split_and_join:", e)