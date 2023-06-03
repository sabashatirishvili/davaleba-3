def is_palindrome(str):
  str = str.replace(" ", "").lower()
  reversed = str.replace(" ", "")[::-1].lower()
  return str == reversed
  

