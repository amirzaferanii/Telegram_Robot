import telebot

TOKEN = "your_key "

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام، حالت چطوره؟ برای رمزنگاری از دستور /encrypt و برای رمزگشایی از دستور /decrypt استفاده کنید.")


@bot.message_handler(commands=['encrypt'])
def encrypt_message(message):
    msg = bot.reply_to(message, "لطفاً متنی که می‌خواهید رمزنگاری کنید را وارد کنید:")
    bot.register_next_step_handler(msg, perform_encryption)

def perform_encryption(message):
    plain_text = message.text
    encrypt_text = ""
    for c in plain_text:
        x = ord(c) * 2 + 2
        encrypt_text += chr(x)
    bot.reply_to(message, f"متن رمزنگاری شده:\n```\n{encrypt_text}\n```", parse_mode='Markdown')


@bot.message_handler(commands=['decrypt'])
def decrypt_message(message):
    msg = bot.reply_to(message, "لطفاً متن رمزنگاری شده را وارد کنید:")
    bot.register_next_step_handler(msg, perform_decryption)

def perform_decryption(message):
    encrypt_text = message.text
    plain_text = ""
    for c in encrypt_text:
        x = (ord(c) - 2) // 2
        plain_text += chr(x)
    bot.reply_to(message, f"متن رمزگشایی شده:\n```\n{plain_text}\n```", parse_mode='Markdown')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "چی میگی ؟ ")

bot.infinity_polling()
