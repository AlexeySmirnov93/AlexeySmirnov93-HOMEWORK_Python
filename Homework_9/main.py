from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commads import *




app = ApplicationBuilder().token("5867962444:AAGAqncsuRSA6vX2FC5bUV_-XXB6YEJ08Ao").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("help", help))

print ('server start')
app.run_polling()