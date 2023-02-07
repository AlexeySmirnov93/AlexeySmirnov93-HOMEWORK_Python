from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/time\n/help\n')

