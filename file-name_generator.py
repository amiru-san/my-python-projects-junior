import time as t
print("=== File Name Generator ===")
proh = ("1234567890@#₽_&-+()/*"':;!?,~`|•√π÷×§∆£€$¢^°={}%©®™✓[].')

while True:
    user = str(input(f"\nWhat is your file type?\n"))
    if any(prohib in proh for prohib in user):
        print(f"No numbers or other symbols, only letters.\n")
        continue
    elif len(user) > 5:
        print(f"File type must be less than 5 characters.\n")
        continue
    elif len(user) < 2:
        print(f"File type must be more than 2 characters.\n")
        continue
    user2 = input(f"\nWhat is your file's name?\n").split()
    print(f"\nGenerating...\n")
    t.sleep(2)
    print("Your file's name:", "_".join(user2) + "." + user)