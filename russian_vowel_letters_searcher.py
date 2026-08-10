letters = ("аеёиоуыэюя")

while True:
    user = str(input("Введите слово: ")).lower()
        
    found = [char for char in user if char in letters]
        
    if len(found) > 0:
        print(f"Найдено гласных букв: {len(found)}")
    else:
        print(f"Гласных букв не найдено.\n")
        continue