from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7660065153:AAE6136d6Y0H-hyTt_taMSrIvz9_TdhihJw"  # Replace with your bot token

# Command to start the bot
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Send '/sendfile' to receive a file.")

# Command to send a file
def send_file(update: Update, context: CallbackContext) -> None:
    file_path = "FolderFile
/7_វិញ្ញាសារ 2017.pdf"  # Replace with the file you want to send
    with open(file_path, "rb") as file:
        update.message.reply_document(document=file, filename="yourfile.pdf")

# Reply to any text message
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"You said: {update.message.text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sendfile", send_file))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
