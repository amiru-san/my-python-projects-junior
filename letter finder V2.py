langs = ("rus", "eng", "uzb", "esp", "ger", "jpn", "kor", "chn")
print(langs, f"\n")

def rus():
    while True:
        print(f"=== Счётчик Букв ===\n")
        print("Чтобы выйти, впиши 'exit'")
        a = str(input("Слово или предложение для счёта: "))
        if a == "exit":
            print(f"Успешный выход.\n")
            break
        b = str(input("Цель (буква): "))
        if b == "exit":
            print(f"Успешный выход.\n")
            break
        c = a.count(b)
        print("Счётчик:", c, f"\n")
    
def eng():
    while True:
        print(f"=== Letter Counter ===\n")
        print("To exit, type 'exit'")
        a = str(input("Word of sentence to count with: "))
        if a == "exit":
            print(f"The system was successfully exited.\n")
            break

        b = str(input("Target (letter): "))
        if b == "exit":
            print(f"The system was successfully exited.\n")
            break
        c = a.count(b)
        print("Counter:", c, f"\n")

def uzb():
    while True:
        print(f"=== Belgilar soni ===\n")
        print("Chiqish uchun 'exit' yozing.")
        a = str(input("Ballarga oid so'z yoki ibora: "))
        if a == "exit":
            print(f"Tizimdan muvaffaqiyatli chiqildi.\n")
            break
        b = str(input("Belgilar soni: "))
        if b == "exit":
            print(f"Tizimdan muvaffaqiyatli chiqildi.\n")
            break
        c = a.count(b)
        print("Kashr:", c, f"\n")

def esp():
    while True:
        print(f"=== Contador de letras ===\n")
        print("Para salir, escribe «exit»")
        a = str(input("Una palabra o una frase para la cuenta: "))
        if a == "exit":
            print(f"Salida correcta del sistema.\n")
            break
        b = str(input("Objetivo (letra): "))
        if b == "exit":
            print(f"Salida correcta del sistema.\n")
            break
        c = a.count(b)
        print("Contador:", c, f"\n")

def ger():
    while True:
        print(f"=== Buchstaben-Zähler ===\n")
        print("Um das Programm zu beenden, gib „exit“ ein.")
        a = str(input("Ein Wort oder ein Satz für die Rechnung: "))
        if a == "exit":
            print(f"Erfolgreiches Beenden des Systems.\n")
            break
        b = str(input("Ziel (Buchstabe): "))
        if b == "exit":
            print(f"Erfolgreiches Beenden des Systems.\n")
            break
        c = a.count(b)
        print("Zähler:", c, f"\n")

def jpn():
    while True:
        print(f"=== 文字数カウンター ===\n")
        print("終了するには、「exit」と入力してください")
        a = str(input("スコアを記録するための単語または文: "))
        if a == "exit":
            print(f"システムからのログアウトに成功しました。\n")
            break
        b = str(input("目的（文字）: "))
        if b == "exit":
            print(f"システムからのログアウトに成功しました。\n")
            break
        c = a.count(b)
        print("カウンター:", c, f"\n")

def kor():
    while True:
        print(f"=== 문자 카운터 ===\n")
        print("나오려면 'exit'를 입력하세요")
        a = str(input("계산할 단어 또는 문장: "))
        if a == "exit":
            print(f"시스템에서 정상적으로 로그아웃되었습니다.\n")
            break
        b = str(input("목표 (문자): "))
        if b == "exit":
            print(f"시스템에서 정상적으로 로그아웃되었습니다.\n")
            break
        c = a.count(b)
        print("계량기:", c, f"\n")
    
def chn():
    while True:
        print(f"=== 字母计数器 ===\n")
        print("要退出，请输入“exit”")
        a = str(input("用于计数的单词或短语: "))
        if a == "exit":
            print(f"已成功退出系统。\n")
            break
        b = str(input("目标（字母）: "))
        if b == "exit":
            print(f"已成功退出系统。\n")
            break
        c = a.count(b)
        print("计数器:", c, f"\n")

user_lang=str(input(f"Which language do you want to use?\n> ").lower().strip())

if user_lang == langs[0]:
    rus()
elif user_lang == langs[1]:
    eng()
elif user_lang == langs[2]:
    uzb()
elif user_lang == langs[3]:
    esp()
elif user_lang == langs[4]:
    ger()
elif user_lang == langs[5]:
    jpn()
elif user_lang == langs[6]:
    kor()
elif user_lang == langs[7]:
    chn()
else:
    print("Unknown language, try again.")