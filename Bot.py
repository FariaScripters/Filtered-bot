from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Hello! I am your bot. How can I help you?")

def main():
    # Bot Token
    updater = Updater("7694723736:AAETA9JnlN53sLGCrrO3fAnxqt6m0P-NYw4", use_context=True)

    # Command Handler
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
