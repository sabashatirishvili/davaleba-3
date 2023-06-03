def count_vowels(str):
    str = str.lower()
    vowels = ["ა", "ე", "ი", "ო", "უ"]
    counter = 0
    for letter in str:
        if letter in vowels:
            counter += 1
    return counter

