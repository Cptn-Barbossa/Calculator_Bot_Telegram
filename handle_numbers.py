from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def math(update, context):
    keyboard = [
        ["Сложение", "Вычитание"],
        ["Умножение", "Деление"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "Выбери операцию: ",
        reply_markup=reply_markup
    )

async def handle_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Обработка выбора операции через кнопки
    if text == "Сложение":
        context.user_data["operation"] = "summ"
        await update.message.reply_text("Давай начнём складывать!\nВведи первое число:\n")
        return
    elif text == "Вычитание":
        context.user_data["operation"] = "subtract"
        await update.message.reply_text("Давай начнём вычитать!\nВведи первое число:\n")
        return
    elif text == "Умножение":
        context.user_data["operation"] = "multiply"
        await update.message.reply_text("Давай начнём умножать!\nВведи первое число:\n")
        return
    elif text == "Деление":
        context.user_data["operation"] = "division"
        await update.message.reply_text("Давай начнём делить!\nВведи первое число:\n")
        return

    # Дальше — обработка чисел
    operation = context.user_data.get("operation")
    is_number = text.replace("-", "").isdigit()
    if not operation:
        if is_number:
            await update.message.reply_text(
                "Сначала выбери операцию: /math"
            )
        return
    if "number1" not in context.user_data:
        try:
            context.user_data["number1"] = float(text)
            await update.message.reply_text("Введите второе число:")
        except ValueError:
            await update.message.reply_text("Пожалуйста, введите число, а не текст.")
    else:
        try:
            context.user_data["number2"] = float(text)
            number1 = context.user_data["number1"]
            number2 = context.user_data["number2"]
            if operation == "summ":
                result = number1 + number2
                op_sign = "+"
            elif operation == "subtract":
                result = number1 - number2
                op_sign = "-"
            elif operation == "multiply":
                result = number1 * number2
                op_sign = "*"
            elif operation == "division":
                if number2 == 0:
                    await update.message.reply_text("Ошибка: Деление на ноль невозможно. Лапух, он не знает вышмат, не издевайся.")
                    return
                result = number1 / number2
                op_sign = "/"
            else:
                await update.message.reply_text("Неизвестная операция.")
                return
            await update.message.reply_text(f"Результат: {number1} {op_sign} {number2} = {result}")
            context.user_data.clear()
            await update.message.reply_text("Если хотите ещё, выберите операцию и введите первое число:")
            await update.message.reply_text("Или введите /help чтобы узнать мои команды :)")
        except ValueError:
            await update.message.reply_text("Пожалуйста, введите число, а не текст.")