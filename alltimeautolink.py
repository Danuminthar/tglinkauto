import os
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Render Port အတွက် Web Server သတ်မှတ်ခြင်း
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# ၁။ မိမိ BotFather မှရသော API Token ကို ဒီနေရာတွင် ထည့်ပါ
BOT_TOKEN = "8490087597:AAFsqPXsqPI1fOFjl7HmRjNk4YGoXID5QR8"

# ၂။ ပို့စ်တိုင်း၏ အောက်ခြေတွင် ထည့်လိုသော လင့်ခ်နှင့် စာသားကို သတ်မှတ်ပါ
FOOTER_TEXT = """

🔗 ဇာတ်ကားကောင်းများကြည့်ရန် Join ပါ:
https://t.me/+NnNgYUEklMAzMTY1
https://t.me/moviesourcess 

🔗 အမှောင်ကားကြည့်ရန် Join ပါ:
https://t.me/+ptrKsmvyO3VkMDBl 

ဈေးနှုန်းသက်သာစွာဖြင့် 
ကြော်ညာထည့်သွင်းလိုပါက 
https://t.me/DeDee1123 
သို့ဆက်သွယ်လိုက်ပါ"""

async def auto_append_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    if not post:
        return

    if post.text:
        new_text = post.text + FOOTER_TEXT
        try:
            await context.bot.edit_message_text(
                chat_id=post.chat_id,
                message_id=post.message_id,
                text=new_text,
                disable_web_page_preview=False
            )
        except Exception as e:
            print(f"Error text: {e}")

    elif post.caption:
        new_caption = post.caption + FOOTER_TEXT
        try:
            await context.bot.edit_message_caption(
                chat_id=post.chat_id,
                message_id=post.message_id,
                caption=new_caption
            )
        except Exception as e:
            print(f"Error caption: {e}")

if __name__ == "__main__":
    # Flask Server ကို နောက်ကွယ်တွင် Run ခြင်း
    Thread(target=run_flask).start()

    # Telegram Bot စတင်ခြင်း
    bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
    bot_app.add_handler(MessageHandler(filters.ChatType.CHANNEL, auto_append_link))
    bot_app.run_polling()
