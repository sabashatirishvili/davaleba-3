def largest_common_str(str1, str2):
    """ფუნქცია, რომელიც ორ სტრიქონს შორის პოულობს უდიდეს საერთო ქვესტრიქონს"""
    largest_str = ""
    str1 = str1.lower().split()
    str2 = str2.lower().split()
    for word in str1:
        if word in str2 and len(word) > len(largest_str):
            largest_str = word
    return largest_str
