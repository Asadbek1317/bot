from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters)
BTN_PICTURE, BTN_CHAT, BTN_VIDEO = ('🌄Rasmlar', 'Tanishuv Chatlar', 'Xxx Videolar')


main_buttons = ReplyKeyboardMarkup([
    [BTN_PICTURE], [BTN_CHAT, BTN_VIDEO]
], resize_keyboard=True)

STATE_REGION = 1
STATE_PICTURE = 2

def start(update, context):
    user = update.message.from_user
    buttons = [
        [
            InlineKeyboardButton('Namangan', callback_data='chat_1'),
            InlineKeyboardButton('Andijon', callback_data='chat_2'),
            InlineKeyboardButton("Farg'ona", callback_data='chat_3')
        ],
        [
            InlineKeyboardButton("POp tunani", callback_data='chat_4')
        ]
    ]
    update.message.reply_html("Salom <b>{}!</b> Qalaysiz: Siz bu yerda 👉 3 ta Viloyat haqida Ajoyib narsalarni ko'rishingiz mumkin ".
     format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))

    return STATE_REGION


def inline_callback(update, context):
        query = update.callback_query
        query.message.delete()
        query.message.reply_html(text="<b>Bizni kuzatishni unutmang</b>2️⃣0️⃣2️⃣3️⃣\n ====================================================== \nChatimiz 👉<a href='https://t.me/DOSTLA_DAVRASI_N1'>do'stlar</a> \nQuyidagilardan birini tanlang 👇", reply_markup=main_buttons)
        return STATE_PICTURE

def picture(update, context):
    update.message.reply_text('Sizlar uchun\n \nhttps://t.me/ramantik_rasmlar')

def chat(update, context):
    update.message.reply_text("https://t.me/millatdosh_uz")  

def video(update, context):
    update.message.reply_text('Kechirasiz Sizning yoshingiz hali 18 yoshga tolmagan. Sizga 🔞 korish mumkin emas!!!')      


def main():
    updater = Updater('', use_context=True)

    dispatcher = updater.dispatcher

    #dispatcher.add_handler(CommandHandler('start', start))

    #dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={
            STATE_REGION: [CallbackQueryHandler(inline_callback)],
            STATE_PICTURE:[
                MessageHandler(Filters.regex('^('+BTN_PICTURE+')$'), picture),
                MessageHandler(Filters.regex('^('+ BTN_CHAT +')$'), chat),
                MessageHandler(Filters.regex('^('+ BTN_VIDEO +')$'), video)
            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

main()    