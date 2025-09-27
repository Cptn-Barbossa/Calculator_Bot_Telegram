
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import MessageHandler, filters
from handle_numbers import handle_numbers, math
from config import TOKEN

async def start(update, context):
    await update.message.reply_text("Привет! Я бот помощник который умеет делать разные вещи! \nНапиши /help чтобы узнать мои команды\n")

async def help(update, context):
    await update.message.reply_text("Мои команды:\n/start - начать работу с ботом\n/help - получить помощь\n/math - математические\n")

async def unknown(update, context):
    await update.message.reply_text(
        "Я не понимаю что ты хочешь от меня ;(\n"
        "Вот что я могу:\n"
        "/start — начать работу\n"
        "/help — помощь\n"
        "/math — математические операции\n"
    )


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("math", math))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.COMMAND, unknown))
app.add_handler(MessageHandler(filters.TEXT, handle_numbers))
app.run_polling()