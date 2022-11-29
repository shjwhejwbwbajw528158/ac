from telegram.ext import *



def st(u,c):
    u.message.reply_text("Hello Bro")
    print("Someone Called Start")





u = Updater("5938418108:AAHymtX7mJfhDZQI97FkASRpxdnz2c2Q-4Y",use_context=True)



u.dispatcher.add_handler(CommandHandler("start",st))

u.start_polling()
u.idle()
