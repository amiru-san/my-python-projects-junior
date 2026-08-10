import time

user = int(input("Введите число: "))

while True:
    print(user)
    user -= 1
    time.sleep(1)
    if user < 1:
        print("Время вышло!")
        break