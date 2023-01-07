from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from bot_message import *
from bot_token import *

TOKEN = token


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    create_handler = ConversationHandler(
        entry_points=[CommandHandler('add', bot_message_create_data)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, create_data)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    del_handler = ConversationHandler(
        entry_points=[CommandHandler('del', bot_message_del_data)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, bot_message_del_number)],
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    find_handler = ConversationHandler(
        entry_points=[CommandHandler('find', bot_message_find_data)],

        states={
            1: [MessageHandler(Filters.text & ~Filters.command, show_find_data)],
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    noname_handler = MessageHandler(Filters.command, noname)
    start_handler = CommandHandler('start', start)
    show_handler = CommandHandler('show', show_phonebook)

    dp.add_handler(create_handler)
    dp.add_handler(start_handler)
    dp.add_handler(show_handler)
    dp.add_handler(del_handler)
    dp.add_handler(find_handler)
    dp.add_handler(noname_handler)
    updater.start_polling()
    updater.idle()