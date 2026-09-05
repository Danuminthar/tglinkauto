import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

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

    # စာသားသီးသန့် ပို့စ်ဖြစ်ပါက
    if post.text:
        new_text = post.text + FOOTER_TEXT
        try:
            await context.bot.edit_message_text(
                chat_id=post.chat_id,
                message_id=post.message_id,
                text=new_text,
                disable_web_page_preview=False
            )
            print(f"Message {post.message_id} updated.")
        except Exception as e:
            print(f"Error: {e}")

    # ဓာတ်ပုံ/ဗီဒီယို ပါသော ပို့စ်ဖြစ်ပါက (Caption)
    elif post.caption:
        new_caption = post.caption + FOOTER_TEXT
        try:
            await context.bot.edit_message_caption(
                chat_id=post.chat_id,
                message_id=post.message_id,
                caption=new_caption
            )
            print(f"Caption {post.message_id} updated.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.CHANNEL, auto_append_link))
    
    print("Python Telegram Bot စတင်ပွင့်နေပါပြီ...")
    app.run_polling()
