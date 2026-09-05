import os
from threading import Thread
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Render Port အတွက် Web Server သတ်မှတ်ခြင်း
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ၁။ BotFather ထံမှ ရရှိသော API Token ကို ဒီနေရာတွင် ထည့်ပါ
BOT_TOKEN = "8490087597:AAFsqPXsqPI1fOFjl7HmRjNk4YGoXID5QR8"

# ၂။ Inline Buttons (နှိပ်လို့ရသော ခလုတ်များ) ဒီဇိုင်း သတ်မှတ်ခြင်း
keyboard = [
    [
        InlineKeyboardButton("🎬 VIP Channel", url="https://t.me/+NnNgYUEklMAzMTY1"),
        InlineKeyboardButton("🎬 Main Channel", url="https://t.me/moviesourcess")
    ],
    [
        InlineKeyboardButton("🔞 အမှောင်ကား Channel", url="https://t.me/+ptrKsmvyO3VkMDBl")
    ],
    [
        InlineKeyboardButton("📩 ကြော်ညာထည့်သွင်းရန်", url="https://t.me/DeDee1123")
    ]
]

reply_markup = InlineKeyboardMarkup(keyboard)

async def auto_add_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if not post:
        return

    try:
        # ပို့စ်အမျိုးအစား အားလုံးအောက်တွင် Inline Buttons များ တိုက်ရိုက် ထည့်သွင်းခြင်း
        await context.bot.edit_message_reply_markup(
            chat_id=post.chat_id,
            message_id=post.message_id,
            reply_markup=reply_markup
        )
        print(f"Message {post.message_id} - Buttons added successfully.")
    except Exception as e:
        print(f"Error adding buttons: {e}")

if __name__ == "__main__":

    Thread(target=run_flask).start()

    bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
    bot_app.add_handler(MessageHandler(filters.ChatType.CHANNEL, auto_add_buttons))
    
    print("Python Telegram Bot စတင်ပွင့်နေပါပြီ...")
    bot_app.run_polling()
