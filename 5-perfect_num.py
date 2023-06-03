def is_perfect(num):
    """ფუნქცია, რომელიც ამოწმებს არის თუ არა რიცხვი სრულყოფილი"""
    divSum = 0
    for i in range(1, num):
        if num % i == 0:
            divSum += i
    return num == divSum
