def is_anagram(str1, str2):
    str1_sorted = sorted(str1.replace(" ", "").lower())
    str2_sorted = sorted(str2.replace(" ", "").lower())
    return str1_sorted == str2_sorted
