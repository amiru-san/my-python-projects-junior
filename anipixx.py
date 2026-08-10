import telebot
from telebot import types
import os

token = '8974412743:AAHI3KZRfBHiHvZP6IwD2UTWGA0YU4psO1o'

# токен
bot = telebot.TeleBot(token)

# папки
beautyfolder = "/storage/emulated/0/AniPixx/images/beauty"
romancefolder = "/storage/emulated/0/AniPixx/images/romance"
couplefolder = "/storage/emulated/0/AniPixx/images/couple"
memesfolder = "/storage/emulated/0/AniPixx/images/memes"
cutefolder = "/storage/emulated/0/AniPixx/images/cute"
blkwhtfolder = "/storage/emulated/0/AniPixx/images/black and white"
darkfolder = "/storage/emulated/0/AniPixx/images/dark"

# считалки
beautyphoto_index = 0
romancephoto_index = 0
couplephoto_index = 0
memephoto_index = 0
cutephoto_index = 0
blkwhtphoto_index = 0
darkphoto_index = 0

# красота
def beautiful(msg):
    global beautyphoto_index
    
    beautifully = sorted(os.listdir(beautyfolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if beautyphoto_index >= len(beautifully):
        beautyphoto_index = 0

    beautyphoto_path = os.path.join(beautyfolder, beautifully[beautyphoto_index])
    with open(beautyphoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Beauty Theme</i>", parse_mode='HTML')
    beautyphoto_index += 1

# роматиш
def romantic(msg):
    global romancephoto_index
    
    romantically = sorted(os.listdir(romancefolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if romancephoto_index >= len(romantically):
        romancephoto_index = 0

    romancephoto_path = os.path.join(romancefolder, romantically[romancephoto_index])
    with open(romancephoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Romance Theme</i>", parse_mode='HTML')
    romancephoto_index += 1
    
# парочка
def couple(msg):
    global couplephoto_index
    
    couples = sorted(os.listdir(couplefolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if couplephoto_index >= len(couples):
        couplephoto_index = 0

    couplephoto_path = os.path.join(couplefolder, couples[couplephoto_index])
    with open(couplephoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Matching Theme</i>", parse_mode='HTML')
    couplephoto_index += 1

# ржунимагу
def meme(msg):
    global memephoto_index
    
    memes = sorted(os.listdir(memesfolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if memephoto_index >= len(memes):
        memephoto_index = 0

    memephoto_path = os.path.join(memesfolder, memes[memephoto_index])
    with open(memephoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Meme Theme</i>", parse_mode='HTML')
    memephoto_index += 1
    
# милые
def cute(msg):
    global cutephoto_index
    
    cutty = sorted(os.listdir(cutefolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if cutephoto_index >= len(cutty):
        cutephoto_index = 0

    cutephoto_path = os.path.join(cutefolder, cutty[cutephoto_index])
    with open(cutephoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Cute Theme</i>", parse_mode='HTML')
    cutephoto_index += 1
    
# черно белые
def blkwht(msg):
    global blkwhtphoto_index
    
    blacknwhite = sorted(os.listdir(blkwhtfolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if blkwhtphoto_index >= len(blacknwhite):
        blkwhtphoto_index = 0

    blkwhtphoto_path = os.path.join(blkwhtfolder, blacknwhite[blkwhtphoto_index])
    with open(blkwhtphoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Black and White Theme</i>", parse_mode='HTML')
    blkwhtphoto_index += 1
    
# мрачные
def dark(msg):
    global darkphoto_index
    
    darker = sorted(os.listdir(darkfolder), key=lambda x: int(os.path.splitext(x)[0]))
    
    if darkphoto_index >= len(darker):
        darkphoto_index = 0

    darkphoto_path = os.path.join(darkfolder, darker[darkphoto_index])
    with open(darkphoto_path, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption="•⟡ᛝ @AniPixx_bot ᛝ⟡• // <i>Dark Theme</i>", parse_mode='HTML')
    darkphoto_index += 1

# о боте
def about(msg):
    username = msg.from_user.username
    about = "/storage/emulated/0/AniPixx/about.jpg"
    with open(about, 'rb') as photo:
        bot.send_photo(msg.chat.id, photo, caption=f"Привет снова, {username}.\n\nБот был создан ради развлечения и не несёт ответственность за поведение пользователя или применение контента из бота.\n\nВсе фото были взяты из платформы 'Pinterest'.\nВсе кредиты авторам изображений, я не владею никаким контентом из этого бота.\n\nКонничива, {username}-сан!\n\nЗдесь ты можешь найти эстетичную картинку своего любимого аниме персонажа, или же просто поискать эстетичные изображения в аниме стиле.\n\nБот был сделан @zypax.")

# кнопки
def theme_receive(msg):
    themes = types.ReplyKeyboardMarkup(resize_keyboard=True)
    beautybutton = types.KeyboardButton("| Beautiful |")
    romancebutton = types.KeyboardButton("| Romantic |")
    couplebutton = types.KeyboardButton("| Matching |")
    memebutton = types.KeyboardButton("| Memes |")
    cutebutton = types.KeyboardButton("| Cute |")
    blkwhtbutton = types.KeyboardButton("| Black and white |")
    darkbutton = types.KeyboardButton("| Dark |")
    aboutbutton = types.KeyboardButton("About")
    themes.row(beautybutton, romancebutton)
    themes.row(couplebutton, memebutton)
    themes.row(cutebutton, blkwhtbutton)
    themes.row(darkbutton, aboutbutton)
    return themes

# поехали
@bot.message_handler(commands=['start'])
def greet(msg):
    buttonreceiver = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Меню / Menu")
    buttonreceiver.add(btn)
    username = msg.from_user.username
    bot.send_message(msg.chat.id, f"Привет {username}.\n\nЯ — бот который отправляет рандомные эстетичные  аниме картинки тебе в чат.\n\nНажми на кнопку под твоей клавиатурой, чтобы открыть меню тем.", reply_markup=buttonreceiver)
    bot.register_next_step_handler(msg, on_click)

def on_click(msg):
    if msg.text == "Меню / Menu":
        bot.send_message(msg.chat.id, f"<b>Доступные темы:</b>\n\n<i>• Красивые / Beautiful •</i>\n\n<i>• Романтические / Romantic • </i>\n\n<i>• Парные / Matching •</i>\n\n<i>• Мемы / Memes •</i>\n\n<i>• Милые / Cute •</i>\n\n<i>• Чёрно-белые / Black and white •</i>\n\n<i>• Мрачные / Dark •</i>\n\n<b>Скоро будет новый завоз картинок и аватарок.</b>", parse_mode='HTML', reply_markup=theme_receive(msg))
        bot.register_next_step_handler(msg, buttonanswer)
    else:
        bot.register_next_step_handler(msg, on_click)
# действия кнопок
def buttonanswer(msg):
   if msg.text == "| Beautiful |":
      beautiful(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "| Romantic |":
      romantic(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "| Matching |":
      couple(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "| Memes |":
      meme(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "| Cute |":
      cute(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "| Black and white |":
      blkwht(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "| Dark |":
      dark(msg)
      bot.register_next_step_handler(msg, on_click)
   elif msg.text == "About":
      about(msg)
      bot.register_next_step_handler(msg, on_click)
   else:
       bot.send_message(msg.chat.id, "Команда не распознана, используй кнопки. / Unknown command, use buttons.")
   bot.register_next_step_handler(msg, buttonanswer)

# менюшка

@bot.message_handler(commands=['menu'])
def menumode(menu):
    bot.send_message(menu.chat.id, f"<b>Доступные темы:</b>\n\n<i>• Красивые</i> — /beauty\n\n<i>• Романтические</i> — /romance\n\n<i>• Парные</i> — /couple\n\n<i>• Мемы</i> — /memes\n\n<i>• Милые</i> — /cute\n\n<i>• Чёрно-белые</i> — /blkwht\n\n<i>• Мрачные картинки</i> — /dark\n\n<b>Скоро будет новый завоз картинок, <b>stay tuned!</b>", parse_mode='HTML')

bot.infinity_polling()