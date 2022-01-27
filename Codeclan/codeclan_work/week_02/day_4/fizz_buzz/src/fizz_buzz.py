def fizz_buzz(num):

    if num % 3 == 0 and num % 5 == 0: 
        return "fizzbuzz"
    if num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)