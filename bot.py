from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai

# إعداد المفاتيح
BOT_TOKEN = "8446070901:AAHXqAKG7IWanYLR-C9XgnxiqWruJHKbXyk"
OPENAI_KEY =  "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"  # مفتاح OpenAI يبدأ بـ sk-
openai.api_key = OPENAI_KEY

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً بك في بوت الذكاء الاصطناعي الخاص بـ 𝑨𝑩! ابدأ رحلتك الآن.")

# أمر /ask
async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = ' '.join(context.args)
    if not user_input:
        await update.message.reply_text("🧠 اكتب سؤالك بعد الأمر /ask")
        return
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

# أمر /subscribe
async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("اشترك الآن", url="https://yourdomain.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📩 اشترك لتصلك التحديثات!", reply_markup=reply_markup)

# تشغيل البوت
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("subscribe", subscribe))
app.run_polling()