print("=== Calculator V1 ===")

exit = ("exit", "leave", "quit", "left", "remove")

while True:
    try:
        user = float(input("First Num: ").strip().lower())
        user2 = float(input("Second Num: ").strip().lower())
        sym = input("Symbol: ").strip().lower()
        
        if sym == "+":
            print(user, sym, user2, "=", user+user2)
        elif sym == "-":
            print(user, sym, user2, "=", user-user2)
        elif sym in ["/", "÷", ":"]:
            print(user, sym, user2, "=", user/user2)
        elif sym in ["*", "•", "×"]:
            print(user, sym, user2, "=", user*user2)
        else:
            print("Please, enter a symbol.")
            continue
    except ValueError:
        print("There must be a number.")
        continue