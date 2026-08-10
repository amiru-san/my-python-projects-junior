while True:
    try:
        user = int(input("Enter your number: "))
        
        if user % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("There must be a number.")