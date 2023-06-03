def is_perfect(num):
    divSum = 0
    for i in range(1, num):
        if num % i == 0:
            divSum += i
    return num == divSum
