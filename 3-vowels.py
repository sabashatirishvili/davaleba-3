def count_vowels(str):
    """ფუნქცია, რომელიც ითვლის სტრიქონში ხმოვნებს"""
    str = str.lower()
    vowels = ["ა", "ე", "ი", "ო", "უ"]
    counter = 0
    for letter in str:
        if letter in vowels:
            counter += 1
    return counter

