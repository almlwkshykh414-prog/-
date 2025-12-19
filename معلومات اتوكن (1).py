import telebot
from telebot import types
import requests

token = '8154980535:AAFb8FL0rXXmYSmK0oRowNXEP0Y7j-zJvc4'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    btn1 = types.InlineKeyboardButton('• معلومات التوكن •', callback_data='btn1')
    btn2 = types.InlineKeyboardButton('• المطور •', url='t.me/WW_GGW')
    k = types.InlineKeyboardMarkup(row_width=1)
    k.add(btn1, btn2)
    bot.send_message(message.chat.id, """<strong>
👋🏻
—————————————————
اهلاً بك عزيزي 
في بوت معلومات التوكن ❤
</strong>""", reply_markup=k, parse_mode='html')
@bot.callback_query_handler(func=lambda call: True)
def Karar(call):
    if call.data == 'btn1':
        msg = bot.send_message(call.message.chat.id, "ارسل التوكن الان:")
        bot.register_next_step_handler(msg, nm)

def nm(message):
    token = message.text
    try:
        getme = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()
        webhook = requests.get(f"https://api.telegram.org/bot{token}/getWebhookInfo").json()

        if not getme.get("ok"):
            bot.send_message(message.chat.id, "❌ التوكن غير صالح.")
            return

        user = getme["result"]["username"]
        name = getme["result"]["first_name"]
        user_id = getme["result"]["id"]
        webhook_url = webhook["result"].get("url", "❌ لا يوجد ويبهوك")

        btn = types.InlineKeyboardButton('• المطور •', url='t.me/WW_GGW')
        c = types.InlineKeyboardMarkup(row_width=1)
        c.add(btn)

        bot.send_message(message.chat.id, f"""
<strong>✅ معلومات التوكن</strong>
——————————————
👤 الاسم: {name}
📎 اليوزر: @{user}
🆔 الايدي: {user_id}
🌐 الويبهوك: {webhook_url}
""", reply_markup=c, parse_mode='html')

    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ أثناء جلب المعلومات.\n{e}")

bot.polling()