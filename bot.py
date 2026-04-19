from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8202205111:AAFli20yPR4NypqUaFcadyInbDzORR61Fdg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """🎉 Welcome to Robot!

Please send your phone number starting with country code.
Example: +880xxxxxxxxxxx

/ca check capacity"""
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
