def is_palindrome(str):
  """ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი პალინდრომი"""
  str = str.replace(" ", "").lower()
  reversed = str.replace(" ", "")[::-1].lower()
  return str == reversed
  

