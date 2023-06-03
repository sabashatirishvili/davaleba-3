def is_anagram(str1, str2):
    """ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი ანაგრამა"""
    str1_sorted = sorted(str1.replace(" ", "").lower())
    str2_sorted = sorted(str2.replace(" ", "").lower())
    return str1_sorted == str2_sorted
