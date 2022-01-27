num = list(range(1, 30))

def fizz_buzz(num):


    game_played = []

    for number in num:
        if number % 3 == 0 and num % 5 == 0: 
            number = "fizzbuzz"
            game_played.append(number)
        if number % 3 == 0:
            number = "buzz"
            game_played.append(number)
        elif number % 5 == 0:
            number = "fizz"
            game_played.append(number)
        else:
            number = str(number)
            game_played.append(number)

    print(game_played)

fizz_buzz(num)