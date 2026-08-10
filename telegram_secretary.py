import telebot
import time
import os

BOT_TOKEN = "token here"
bot = telebot.TeleBot(BOT_TOKEN)

MY_USER_ID = 1234567890
TIMEOUT_SECONDS = 0

user_timeouts = {}

@bot.business_message_handler(func=lambda message: message.text is not None)
def main(message):
    if message.from_user.id == MY_USER_ID:
        return

    chat_id = message.chat.id
    current_time = time.time()

    if chat_id in user_timeouts:
        last_time = user_timeouts[chat_id]
        if current_time - last_time < TIMEOUT_SECONDS:
            return

    user_timeouts[chat_id] = current_time

    username = message.from_user.username or message.from_user.first_name
    for i in range(50):
        bot.send_message(
            chat_id=chat_id, 
            text=f"👋 Здравствуйте, {username}!\n\nС вами говорит автоответчик.\nПожалуйста, оставьте сообщение.\n\n<b>Ваше сообщение будет отправлено @AmiruJapan.</b>", 
            business_connection_id=message.business_connection_id, 
            parse_mode='HTML'
        )
   
if __name__ == '__main__':
    bot.infinity_polling(allowed_updates=["message", "edited_message", "business_message", "edited_business_message", "business_connection"])