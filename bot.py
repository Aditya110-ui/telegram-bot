import telebot
from telebot import types

BOT_TOKEN = "8125827798:AAEVEfutpzDMwuAWBhrIMlxJuApOOp8ZPW4"
CHANNEL_LINK = "https://t.me/rarestudy"
INSTRUCTION_IMAGE = "https://drive.google.com/uc?export=download&id=1ixy-RxeCpjk0m0YZVC4QRJe3BDnz1MAb"
VIDEO_LINK = "https://drive.google.com/uc?export=download&id=1iua8T8yXra_1Ck7xcm9Pta9ElHt1Kd94"
WEBSITE_LINK = "http://rarestudy.site"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("✅ Joined", callback_data="joined")
    markup.add(btn)
    bot.send_message(
        message.chat.id,
        f"👋 Welcome!\n\n📢 Pehle is channel ko join karo:\n👉 {CHANNEL_LINK}\n\nPhir neeche '✅ Joined' dabao.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "joined")
def ask_disable_browser(call):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("✅ Done", callback_data="browser_disabled")
    markup.add(btn)

    bot.send_photo(call.message.chat.id, INSTRUCTION_IMAGE,
                   caption="🛑 Ab Telegram ke inbuilt browser ko band karo:\n\n⚙️ Settings → Chat Settings → Turn OFF \"Open links in Telegram\"\n\nUske baad 'Done' dabao.",
                   reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "browser_disabled")
def send_final_resources(call):
    bot.send_message(call.message.chat.id, f"🔗 Your course access link:\n{WEBSITE_LINK}")
    bot.send_video(call.message.chat.id, video=VIDEO_LINK, caption="📽️ How to access the website successfully.")

bot.polling()
