from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('សួរស្តីខ្ញុំឈ្មោះLONGគឺជាមនុស្សយន្ត(Bot) បច្ចុប្បន្នកំពុងអភិវឌ្ឍន៍!')

app = ApplicationBuilder().token("7660065153:AAE6136d6Y0H-hyTt_taMSrIvz9_TdhihJw").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
