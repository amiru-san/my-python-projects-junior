from random import *

bot = randint(1, 10)
while True:
    try:
        user = int(input("Ваше число: "))
        
        if user == bot:
            print("Поздравляем, вы угадали!")
            break
        else:
            print("Неверно, попробуй еще раз.")
    except ValueError:
        print("Только числа.")