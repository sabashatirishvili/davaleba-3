def intToRoman(num):
    """ფუნქცია, რომელსაც გადაჰყავს რიცხვი რომაულ სისტემაში"""
    numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        100:"C",
        90: "XC",
        50: "L",
        40: "XL",
        10:"X",
        9: "IX",
        5: "V",
        4: "IV",
        1:"I",
    }
    output = ""
    for key in numerals.keys():
      while key <= num:
         output += numerals[key]
         num -= key
    return output

print(intToRoman(3999))