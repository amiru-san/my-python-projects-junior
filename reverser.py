while True:
    user = str(input("Введите слово: "))
    
    result = "".join(reversed(user))
    print(result)