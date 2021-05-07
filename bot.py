import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

name = ''

def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Help!')


def reg_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Введите свое имя и фамилию для регистрации')
    name = update.message.text
    pass

def main() -> None:
    updater = Updater("1794679515:AAG_8EIxUGAQA_5E2Jcvyyf_CpYQVnaqndw")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("reg", reg_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reg_command))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()