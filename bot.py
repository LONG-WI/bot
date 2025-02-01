from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN' with your bot's token
TOKEN = '7660065153:AAE6136d6Y0H-hyTt_taMSrIvz9_TdhihJw'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. Send me a message and I will echo it back.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
