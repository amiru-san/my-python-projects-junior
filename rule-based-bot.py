import random
import re
import time
import difflib
import json
import os
import telebot

# ТОКЕН БОТА (Получи у @BotFather)
TOKEN = '8974030116:AAFD4LSfoZtOBIK0yUFtQCH1QlaU0lP7tqk'
bot = telebot.TeleBot(TOKEN)

# Настройка пути к базе данных
JSON_PATH = "memory.json"

# --- БЛОК ПРОВЕРОК И ФУНКЦИЙ ОЧИСТКИ ТЕКСТА ---

def is_fully_profane(text):
    t = text.lower()
    leet_map = {
        '1': 'i', '!': 'i', '¹': 'i', '¡': 'i', '|': 'i',
        '0': 'o', '@': 'a', '4': 'a', '$': 's', '5': 's', 
        '3': 'e', '7': 't', '+': 't', '8': 'b', '9': 'g'
    }
    for bad_char, good_char in leet_map.items():
        t = t.replace(bad_char, good_char)
    t = re.sub(r'[^a-z]', '', t)
    t = re.sub(r'(.)\1+', r'\1\1', t)
    bad_words = [
        "shit", "fuck", "bitch", "ass", "cunt", 
        "dick", "pussy", "whore", "bastard", "sex", "penis"
    ]
    for word in bad_words:
        if word in t:
            return True
    return False

# --- БЛОК РАБОТА С JSON (ИНДИВИДУАЛЬНО ДЛЯ КАЖДОГО ЮЗЕРА) ---

def load_all_data():
    if os.path.exists(JSON_PATH):
        try:
            with open(JSON_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return {}
    return {}

def save_all_data(data):
    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_user_profile(user_id):
    db = load_all_data()
    return db.get(str(user_id))

def save_user_profile(user_id, user_profile_data):
    db = load_all_data()
    db[str(user_id)] = user_profile_data
    save_all_data(db)

def is_registered(message):
    profile = get_user_profile(message.from_user.id)
    if not profile or not profile.get("username"):
        bot.reply_to(message, "❌ You are not registered yet! Please use the /register command first.")
        return False
    return True

# --- БАЗА ДАННЫХ СЛОВ И ФРАЗ БОТА ---

bot_desc = [
    "== I am here, coffee's brewing. ==", "== New day, new vibe. Let's get it! ==",
    "== Your favorite digital bestie is online. ==", "== Sending you good vibes today! ==",
    "== I've got your back, no matter what. ==", "== Let's crush this day together! ==",
    "== I am here. What's the plan? ==", "== Always here whenever you wanna chat. ==",
    "== Quick chats, big support, zero judgment. ==", "== Coffee's ready, just waiting on you. ==",
    "== Your virtual soulmate is in the house. ==", "== Let's make today fun and productive. ==",
    "== Sorting out your chaos in style. ==", "== Here to save your time and sanity. ==",
    "== New goals? We've got this! ==", "== Need to vent or need a hand? I'm here. ==",
    "== Keeping things simple and stress-free. ==", "== Your ultimate partner-in-crime is ready. ==",
    "== You and me? The perfect team. ==", "== I am here! What are we doing first? ==",
    "== I am always here when you need a friend. ==", "== Only good vibes and warm replies. ==",
    "== Your go-to girl for literal fun. ==", "== Bringing some cozy vibes to your day. ==",
    "== I am ready. Let's begin! ==", "== Forget the stress, let's focus on you. ==",
    "== Your ride-or-die digital friend. ==", "== New look, same me, ready to hype you up. ==",
    "== I'll handle the boring stuff. You relax. ==", "== I'm here for you, always. =="
]

bot_greet = [
    "Hello {name}. I am here.", "Hi {name}. I'm ready when you are.",
    "Hello {name}. Glad you could make it.", "Hi there, {name}. Let's get started.",
    "Hello {name}. I've been waiting for you.", "Hi {name}. I'm ready to discuss whatever you need.",
    "Hello {name}. I'm entirely at your disposal.", "Hi {name}. Have a seat.",
    "Hello {name}. Tell me what's on your mind.", "Hi {name}. I'm here and I'm listening.",
    "Hello {name}. Let's get straight to business.", "Hi {name}. I hope your day is going productively.",
    "Hello {name}. I'm ready to give you my full attention.", "Hi {name}. I appreciate you taking the time.",
    "Hello {name}. We definitely have things to talk about"
]

bot_byes = [
    "Goodbye {name}, and take care of yourself.", "Got it {name}. Let's talk again next time you're free.",
    "Understood perfectly, {name}. I'll be logging off and closing the session too.",
    "Copy that {name}. See you around next time.", "Roger that, {name}. Thanks for letting me know. Disconnecting right now.",
    "I hear you, {name}. No problem at all. Taking my leave and heading out now.",
    "Clear, {name}. Thanks for the update. I am going offline from here.",
    "Message received loud and clear from you, {name}. Goodbye and have a great rest of the day.",
    "Understood, {name}. That's completely fine. See you later, take care.",
    "Got it, {name}. Appreciate the heads up. Have a truly wonderful day ahead.",
    "Copy that, {name}. Have a highly productive rest of your day today.",
    "Roger that, {name}. Everything makes sense. Talk soon and stay safe.",
    "Fair enough, {name}. Let's leave it at that for now. Goodbye.",
    "Understood, {name}. Wish you all the best. Goodbye and take it easy."
]

bot_thank = [
    "You are very welcome {name}. Wishing you a good time.", "It was my absolute pleasure for you, {name}. Have a fantastic time.",
    "You are most welcome, {name}. I am glad I could make things easier for you.",
    "Always at your service, {name}. Have a great rest of your time.", "Thank you for your kind words, {name}. I truly appreciate it.",
    "You're very welcome, {name}. Wishing you all the best with your tasks or work.",
    "The pleasure is all mine, {name}. Have a wonderful and productive day.", "Not a problem at all for you, {name}. Glad to hear that.",
    "It's always a pleasure, {name}. Have a beautiful day!", "You are very welcome, {name}. Take care and have a wonderful week.",
    "The pleasure is entirely mine, {name}. Enjoy the rest of your day."
]

region_bot = [
    "Your current system location is set to {region}, {name}.", "According to my network protocols, you are running from {region}.",
    "Checking your server coordinates... It says {region}.", "Current location data received: {region}.",
    "We are currently connected through {region} right now!"
]

bot_misund = [
    "Sorry, I didn't get that. Could you rephrase it?", "I'm not sure I understand. Could you put it differently?",
    "Fix that, please. I didn't quite catch your meaning.", "I'm confused. Rephrase that for me, will you?",
    "Could you change the wording? I didn't follow.", "Sorry, I didn't understand. Try explaining it another way.",
    "Correction needed, I didn't get what you meant.", "I lost the thread. Could you rephrase your point?",
    "Sorry, that didn't make sense to me. Try rephrasing it.", "I'm having trouble understanding. Mind putting it another way?",
    "Could you clarify that? I didn't process it correctly.", "Sorry, I didn't follow. Rephrase that for me.",
    "I'm not entirely sure what you mean. Could you reword that?", "Fix that sentence, I didn't quite understand.",
    "Sorry, I missed your point. Try stating it differently."
]

# Ключевые слова для текстового парсера
greet = ["hi", "hai", "hello", "hey", "yo", "sup", "greetings", "hiya", "heya", "hey there", "whatsup", "wazzup", "wassup", "hallo", "welcome", "cheers", "wsg"]
byes = ["bye", "later", "cya", "leaving", "gtg", "bai"]
thanks = ["ty", "thx", "appreciate it", "thank you", "thanks", "cheers"]
locate = ["region", "location", "city", "country", "coordinates", "position", "zone"]
user_name_keys = ["name", "heading", "username"]
user_ager_keys = ["age", "lifetime", "oldness"]
time_keys = ["date", "time", "hour", "minute", "day", "month", "year", "clock", "calendar"]

# Игры и калькулятор фейлы/вин
win = ["Alright, you got me. You win!", "I admit it, I lost this one.", "Fair play, you totally beat me!", "Wow, nice move! You win!", "Okay, okay, I surrender. Your victory!", "You outsmarted me. Congrats!", "No excuses, you won fair and square.", "I completely missed that. You win!", "Fine, the victory is yours this time.", "Victory goes to the human. Well played!"]
lost = ["I won this round, but you did great! Keep it up!", "Got you! Close one though, you're playing really well.", "My point, but honestly, you're a tough opponent!", "I took this one, but that was a really good try.", "Got lucky this time! You're doing awesome, let's continue.", "This round is mine, but don't give up, you're doing great!", "I win here, but you put up a really good fight!", "Got you this time! But seriously, you're doing amazing.", "My win, but that was an excellent effort. Good job!", "I took the point, but you're still doing great. Next round?"]
tie = ["It's a tie. Both sides made the right move.", "A draw. We analyzed the situation identically.", "It's a tie. Neither of us left any room for error.", "We chose the same option. The round is a draw.", "No advantage gained. It's a tie, well played.", "A perfect match. Neither strategy could overcome the other.", "It's a draw. We are completely balanced this round.", "The results are identical. It is a tie.", "No winner this time. Both choices neutralized each other.", "A tie. An equal and well-calculated response from both sides."]

divide_error = ["Sorry, but division by zero is mathematically impossible.", "An error occurred: you cannot divide a number by zero.", "Operation denied. Zero is not a valid divisor.", "Unfortunately, this calculation cannot be performed with a zero denominator.", "Nice try, but division by zero is not allowed.", "Sorry, but you can't share something with nobody.", "Error: Please choose a number other than zero to divide by.", "Action blocked: Attempted to divide by zero.", "Sorry, but dividing by zero would break the universe.", "Sorry, but my calculator refuses to destroy reality by dividing by zero.", "Nice try, but I’m not risking a black hole for your math homework.", "You can't divide by zero. Somewhere, a math teacher is crying."]
digits_error = ["Error: Please use numbers only, not letters.", "Operation denied. Only numeric values are allowed here.", "Unfortunately, letters won't work — I need digits only.", "Nice attempt, but this calculation requires strictly numbers.", "Please type using numbers only. Save the letters for your texts.", "Input error: We only speak the language of numbers here.", "Action blocked: Text detected where only digits should be.", "Nice try, but I only understand the language of mathematics.", "Error: Letters are powerless here, please enter numbers only.", "Unfortunately, you can't do math with words. I need digits.", "Please use digits. Somewhere, a math teacher is crying because you used letters.", "Input rejected. My calculator refuses to read text; it skipped literature class."]

# Фразы времени
time_bot = ["According to my clock, it's {hour}:{minute:02d}.", "Right now it's {hour}:{minute:02d}.", "The clock says {hour}:{minute:02d}.", "It's {hour}:{minute:02d} right now."]
hour_bot = ["It's currently the {hour} o'clock hour.", "We are inside the {hour} hour right now.", "The hour counter is at {hour}.", "It's {hour} o'clock sharp. Well, almost sharp..."]
minute_bot = ["The minute hand is currently at {minute}.", "It's exactly {minute} minutes past the hour.", "We are {minute} minutes into this hour, {name}.", "My counter shows {minute} minutes right now."]
date_bot = ["Today is {day}/{month}/{year} (DD/MM/YYYY).", "According to my calendar, it's {day}/{month}/{year}, {name}.", "It's {day}/{month}/{year}. Can you believe we are already in {year}?", "Today's date is {day}/{month}/{year}."]
day_bot = ["Today is {week}, {name}.", "According to my calendar, it's {week}.", "It's {week} today, {name}.", "My clock says it's {week}."]
year_bot = ["We are currently in the year {year}, {name}.", "According to my calendar, it's {year}.", "It's {year} right now.", "The current year is {year}, {name}."]
month_bot = ["We are currently in {month}, {name}.", "According to my calendar, it's {month}", "It's {month} right now, {name}", "My system says we are in {month}."]

bot_callname = ["According to my system logs, your name is {name}.", "You are registered as {name} in this session.", "My database identifies you as {name}.", "Your current profile name is {name}.", "According to the provided data, you are {name}.", "You are recognized in this system as {name}.", "The records indicate that your name is {name}.", "Based on your account information, you are {name}."]
bot_callage = ["System metrics state that you are {age} years of age.", "Your user profile is flagged with the age of {age}.", "According to the entry, your chronological age is {age}.", "The timestamp on your account calculates your age as {age}.", "Our records show your demographic profile matches the age of {age}.", "The system has logged your maturity level at {age}.", "Your current session parameters identify you as {age} years old.", "Data verification confirms your age milestone is {age}."]

signs = "&@#$_()*':;!?~`|•√π÷×§∆}{=°^¥€¢£%©®™✓\",.<>/_‽¡¿¬±≠≤≥≈≡∞∫√∂∇∏∑‹›«»„+-"
unsup_rus = "йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"

# --- ОБРАБОТКА СТАНДАРТНЫХ КОМАНД ---

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1) # Небольшая искусственная пауза для эффекта
    welcome_text = random.choice(bot_desc) + "\n\n**Available commands:**\n" \
                   "/register — Start your registration\n" \
                   "/location — Automatically sync your city\n" \
                   "/name — Show your username\n" \
                   "/age — Show your registered age\n" \
                   "/botinfo — Information about the bot\n" \
                   "/calc — Run calculation engine\n" \
                   "/randomizer — Number guess game\n" \
                   "/rps — Rock, Paper, Scissors\n" \
                   "/time, /date, /month, /day, /hour, /minute — Time parameters\n\n" \
                   "Or just chat with me in English!"
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['botinfo'])
def show_bot_info(message):
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    profile = get_user_profile(message.from_user.id)
    bot_naming = profile.get("botname", "Assistant") if profile else "Assistant"
    bot_aging = profile.get("botage", "1.0") if profile else "99"
    info = f"=== BOT'S INFO ===\n• Bot Version: 1.0\n• Name: {bot_naming}\n• Current Age: {bot_aging}\n• Purpose: Assistant"
    bot.reply_to(message, info)

# --- УПРАВЛЕНИЕ СЕКЦИЕЙ РЕГИСТРАЦИИ ---

@bot.message_handler(commands=['register'])
def start_registration(message):
    bot.reply_to(message, "=== REGISTRATION ===\nPlease, enter your username (8-24 characters, English only):")
    bot.register_next_step_handler(message, process_username_step)

def process_username_step(message):
    name = message.text
    if any(char in signs or char in unsup_rus for char in name) or is_fully_profane(name) or len(name) < 8 or len(name) > 24:
        bot.reply_to(message, "❌ Invalid username rules (8-24 chars, no bad words, Eng only). Type /register to restart.")
        return

    user_profile = {
        "username": name,
        "city": "Unknown",
        "age": None,
        "botname": None,
        "botage": None
    }
    save_user_profile(message.from_user.id, user_profile)
    
    bot.reply_to(message, "Please, enter your age:")
    bot.register_next_step_handler(message, process_age_step)

def process_age_step(message):
    try:
        user_age = int(message.text)
        if user_age < 1 or user_age > 99:
            bot.reply_to(message, "❌ Age must be between 1 and 99. Type /register to restart.")
            return
        
        user_id = message.from_user.id
        user_profile = get_user_profile(user_id)
        user_profile["age"] = user_age
        save_user_profile(user_id, user_profile)
        
        bot.reply_to(message, "Bot name:")
        bot.register_next_step_handler(message, process_botname_step)
    except ValueError:
        bot.reply_to(message, "❌ There must be a number, not a letter. Type /register to restart.")

def process_botname_step(message):
    bot_naming = message.text
    if any(char in signs or char in unsup_rus for char in bot_naming) or is_fully_profane(bot_naming):
        bot.reply_to(message, "❌ Invalid bot name rules. Type /register to restart.")
        return

    user_id = message.from_user.id
    user_profile = get_user_profile(user_id)
    user_profile["botname"] = bot_naming
    save_user_profile(user_id, user_profile)
    
    bot.reply_to(message, "Please, enter your bot's age:")
    bot.register_next_step_handler(message, process_botage_step)

def process_botage_step(message):
    try:
        bot_aging = int(message.text)
        if bot_aging <= 0:
            bot.reply_to(message, "❌ Age must be positive. Type /register to restart.")
            return

        user_id = message.from_user.id
        user_profile = get_user_profile(user_id)
        user_profile["botage"] = bot_aging
        save_user_profile(user_id, user_profile)
        
        bot.reply_to(message, f"🎉 Data completely saved! Use /location command anytime to sync your city.")
    except ValueError:
        bot.reply_to(message, "❌ There must be a number, not a letter. Type /register to restart.")

# --- АВТОНОМНЫЕ КОМАНДЫ ДАННЫХ ПОЛЬЗОВАТЕЛЯ (/location, /name, /age) ---

@bot.message_handler(commands=['location'])
def get_auto_location(message):
    if not is_registered(message): return
    
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1.5)
    
    user_id = message.from_user.id
    user_profile = get_user_profile(user_id)
    lang = message.from_user.language_code
    
    if lang == 'ru':
        detected_city = "Tashkent"
    elif lang == 'ja':
        detected_city = "Toyama"
    elif lang == 'en':
        detected_city = "London"
    else:
        detected_city = "New York"
        
    user_profile["city"] = detected_city
    save_user_profile(user_id, user_profile)
    
    bot_name = f"{user_profile['botname']}:"
    name = user_profile['username']
    
    response_text = random.choice(region_bot).format(region=detected_city, name=name)
    bot.reply_to(message, f"{bot_name} {response_text}")

@bot.message_handler(commands=['name'])
def get_user_name_cmd(message):
    if not is_registered(message): return
    
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    
    user_profile = get_user_profile(message.from_user.id)
    bot_name = f"{user_profile['botname']}:"
    name = user_profile['username']
    
    response_text = random.choice(bot_callname).format(name=name)
    bot.reply_to(message, f"{bot_name} {response_text}")

@bot.message_handler(commands=['age'])
def get_user_age_cmd(message):
    if not is_registered(message): return
    
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    
    user_profile = get_user_profile(message.from_user.id)
    bot_name = f"{user_profile['botname']}:"
    user_age = user_profile['age']
    
    response_text = random.choice(bot_callage).format(age=user_age)
    bot.reply_to(message, f"{bot_name} {response_text}")

# --- УПРАВЛЕНИЕ МЕНЮ /CALC ---

@bot.message_handler(commands=['calc'])
def start_calc(message):
    if not is_registered(message): return
    bot.reply_to(message, "=== CALCULATOR ===\nFirst Number:")
    bot.register_next_step_handler(message, calc_first_num)

def calc_first_num(message):
    if message.text.lower() in ["close", "exit", "remove", "leave"]: 
        bot.reply_to(message, "Successfully Closed.")
        return
    try:
        n1 = float(message.text)
        bot.reply_to(message, "Second Number:")
        bot.register_next_step_handler(message, calc_second_num, n1)
    except ValueError:
        profile = get_user_profile(message.from_user.id)
        bot.reply_to(message, f"{profile['botname']}: {random.choice(digits_error)}")

def calc_second_num(message, n1):
    if message.text.lower() in ["close", "exit", "remove", "leave"]: 
        bot.reply_to(message, "Successfully Closed.")
        return
    try:
        n2 = float(message.text)
        bot.reply_to(message, "Solution (+, -, *, /):")
        bot.register_next_step_handler(message, calc_solve, n1, n2)
    except ValueError:
        profile = get_user_profile(message.from_user.id)
        bot.reply_to(message, f"{profile['botname']}: {random.choice(digits_error)}")

def calc_solve(message, n1, n2):
    solve = message.text.strip()
    profile = get_user_profile(message.from_user.id)
    bot_name = f"{profile['botname']}:"
    
    if solve in ["close", "exit", "remove", "leave"]: 
        bot.reply_to(message, "Successfully Closed.")
        return

    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.8)

    if solve == "+": bot.reply_to(message, f"{bot_name} {n1 + n2}")
    elif solve == "-": bot.reply_to(message, f"{bot_name} {n1 - n2}")
    elif solve == "*": bot.reply_to(message, f"{bot_name} {n1 * n2}")
    elif solve == "/":
        if n2 == 0:
            bot.reply_to(message, f"{bot_name} {random.choice(divide_error)}")
        else:
            bot.reply_to(message, f"{bot_name} {n1 / n2}")
    else:
        bot.reply_to(message, f"{bot_name} Error: Invalid operator.")

# --- УПРАВЛЕНИЕ МЕНЮ /RANDOMIZER ---

@bot.message_handler(commands=['randomizer'])
def start_randomizer(message):
    if not is_registered(message): return
    bot.reply_to(message, "=== RANDOMIZER ===\nGuess the number from 1 to 10:")
    bot.register_next_step_handler(message, process_randomizer)

def process_randomizer(message):
    if message.text.lower() in ["close", "exit", "remove", "leave"]: 
        bot.reply_to(message, "Successfully Closed.")
        return
    if any(char in unsup_rus for char in message.text):
        bot.reply_to(message, "We are sorry, but this kind of symbols is not supported.")
        return

    profile = get_user_profile(message.from_user.id)
    bot_name = f"{profile['botname']}:"
    
    user_guess = message.text.translate(str.maketrans("", "", signs))
    if not user_guess.isdigit():
        bot.reply_to(message, "Use only numbers.")
        return
        
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)

    user_guess = int(user_guess)
    bot_guess = random.randint(1, 10)
    
    output = f"{bot_name} My number is {bot_guess}\n"
    if user_guess == bot_guess:
        output += random.choice(win)
    else:
        output += random.choice(lost)
    bot.reply_to(message, output)

# --- УПРАВЛЕНИЕ МЕНЮ /RPS ---

@bot.message_handler(commands=['rps'])
def start_rps(message):
    if not is_registered(message): return
    bot.reply_to(message, "=== ROCK, PAPER, SCISSORS ===\nYour move:")
    bot.register_next_step_handler(message, process_rps)

def process_rps(message):
    user_game = message.text.lower().strip()
    if user_game in ["close", "exit", "remove", "leave"]: 
        bot.reply_to(message, "Successfully Closed.")
        return
    if any(char in unsup_rus for char in user_game):
        bot.reply_to(message, "We are sorry, but this kind of symbols is not supported.")
        return

    profile = get_user_profile(message.from_user.id)
    bot_name = f"{profile['botname']}:"
    
    user_game = user_game.translate(str.maketrans("", "", signs))
    bot_game_rps = random.choice(["Paper!", "Scissors!", "Rock!"])
    
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)

    rules = {
        ("paper!", "rock"): lost, ("paper!", "scissors"): win,
        ("rock!", "scissors"): lost, ("rock!", "paper"): win,
        ("scissors!", "paper"): lost, ("scissors!", "rock"): win,
        ("paper!", "paper"): tie, ("rock!", "rock"): tie,
        ("scissors!", "scissors"): tie
    }
    
    key = (bot_game_rps.lower(), user_game)
    if key in rules:
        bot.reply_to(message, f"{bot_name} {bot_game_rps}\n{random.choice(rules[key])}")
    else:
        bot.reply_to(message, "That is not a move. Use Rock Paper Scissors rules.")

# --- УПРАВЛЕНИЕ ВРЕМЕННЫМИ КОМАНДАМИ ИЗ СПИСКА ---

@bot.message_handler(commands=['time', 'hour', 'minute', 'date', 'day', 'year', 'month'])
def handle_time_commands(message):
    if not is_registered(message): return
    
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(0.7)

    profile = get_user_profile(message.from_user.id)
    bot_name = f"{profile['botname']}:"
    name = profile['username']
    
    cmd = message.text.replace("/", "").lower().strip()
    lt = time.localtime()
    
    if cmd == 'time':
        bot.reply_to(message, f"{bot_name} {random.choice(time_bot).format(hour=lt.tm_hour, minute=lt.tm_min)}")
    elif cmd == 'hour':
        bot.reply_to(message, f"{bot_name} {random.choice(hour_bot).format(hour=lt.tm_hour)}")
    elif cmd == 'minute':
        bot.reply_to(message, f"{bot_name} {random.choice(minute_bot).format(minute=lt.tm_min, name=name)}")
    elif cmd == 'date':
        bot.reply_to(message, f"{bot_name} {random.choice(date_bot).format(day=lt.tm_mday, month=lt.tm_mon, year=lt.tm_year, name=name)}")
    elif cmd == 'day':
        bot.reply_to(message, f"{bot_name} {random.choice(day_bot).format(week=time.strftime('%A'), name=name)}")
    elif cmd == 'year':
        bot.reply_to(message, f"{bot_name} {random.choice(year_bot).format(year=lt.tm_year, name=name)}")
    elif cmd == 'month':
        bot.reply_to(message, f"{bot_name} {random.choice(month_bot).format(month=time.strftime('%B'), name=name)}")

# --- УМНЫЙ ОБРАБОТЧИК ДЛЯ ОБЫЧНОГО СВОБОДНОГО ТЕКСТА ---

@bot.message_handler(func=lambda message: True)
def handle_text_processor(message):
    if not is_registered(message): return
    
    bot.send_chat_action(message.chat.id, 'typing')
    
    profile = get_user_profile(message.from_user.id)
    bot_name = f"{profile['botname']}:"
    name = profile['username']
    user_age = profile['age']
    user_region = profile['city']
    
    user_input = message.text.lower().strip()
    if any(char in unsup_rus for char in user_input):
        bot.reply_to(message, "We are sorry, but this kind of symbols is not supported.")
        return

    for sign in signs:
        user_input = user_input.replace(sign, " ")

    user_words = user_input.split()
    if not user_words: return
    
    detect_greet = False; detect_byes = False; detect_thank = False
    detect_location = False; detect_name = False; detect_age = False
    detect_date = False  # Флаг для отслеживания запросов даты/времени
    
    for word in user_words:
        clean_word = re.sub(r'(.)\1+', r'\1\1', word)
        
        if difflib.get_close_matches(clean_word, greet, n=1, cutoff=0.8): detect_greet = True
        if difflib.get_close_matches(clean_word, byes, n=1, cutoff=0.9): detect_byes = True
        if difflib.get_close_matches(clean_word, thanks, n=1, cutoff=0.75): detect_thank = True
        if difflib.get_close_matches(clean_word, locate, n=1, cutoff=0.85): detect_location = True
        if difflib.get_close_matches(clean_word, user_name_keys, n=1, cutoff=0.85): detect_name = True
        if difflib.get_close_matches(clean_word, user_ager_keys, n=1, cutoff=0.85): detect_age = True
        if difflib.get_close_matches(clean_word, time_keys, n=1, cutoff=0.8): detect_date = True

    time.sleep(1.2)

    if detect_location:
        bot.reply_to(message, f"{bot_name} {random.choice(region_bot).format(region=user_region, name=name)}")
    elif detect_name:
        bot.reply_to(message, f"{bot_name} {random.choice(bot_callname).format(name=name)}")
    elif detect_age:
        bot.reply_to(message, f"{bot_name} {random.choice(bot_callage).format(age=user_age)}")
    elif detect_date:
        lt = time.localtime()
        bot.reply_to(message, f"{bot_name} {random.choice(date_bot).format(day=lt.tm_mday, month=lt.tm_mon, year=lt.tm_year, name=name)}")
    elif detect_greet:
        bot.reply_to(message, f"{bot_name} {random.choice(bot_greet).format(name=name)}")
    elif detect_byes:
        bot.reply_to(message, f"{bot_name} {random.choice(bot_byes).format(name=name)}")
    elif detect_thank:
        bot.reply_to(message, f"{bot_name} {random.choice(bot_thank).format(name=name)}")
    else:
        bot.reply_to(message, f"{bot_name} {random.choice(bot_misund)}")

if __name__ == '__main__':
    print("lets go baby")
    bot.infinity_polling()