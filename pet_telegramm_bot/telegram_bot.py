from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from datetime import datetime

import os
import random

jokes = (None,) # Список анекдотов Удалён

thanks_replies = [
    "Спасибо! Это точно его растрогает 🎈",
    "Записал, запечатал, передам Андрюхе",
    "Хах, отличное поздравление! 🎉",
    "Супер, я это сохранил в секретной базе поздравлений 🤫",
    "Передам имениннику лично под фанфары!",
    "Он обязательно это прочитает и расплывётся в улыбке 😊",
    "Да ты поэт, просто праздник какой-то!",
    "Добавлено в книгу великих поздравлений 📘"
]

extra_replies = [
    "Дополнение к поздравлению получено",
    "Ещё одно тёплое слово в копилку 🎁",
    "Передам это тоже — Андрюха не забудет!",
    "Записал и это. Андрюха будет в восторге 🤩",
    "Хорошее дополнение, пусть будет!",
    "Добавлено к праздничной телеге 🚂",
    "Уже представил, как Андрюха это читает 😎",
    "Ты умеешь удивлять, записал и это!",
]


def has_congratulated(user_id: int) -> bool:
    if not os.path.exists("congratulators.txt"):
        return False
    with open("congratulators.txt", "r") as file:
        return str(user_id) in file.read()

def mark_as_congratulated(user_id: int):
    with open("congratulators.txt", "a") as file:
        file.write(f"{user_id}\n")

# Кнопки меню
keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🎉 Поздравить!")],
        [KeyboardButton("🎂 Сколько ему исполнилось?")],
        [KeyboardButton("📚 Расскажи анекдот")]
    ],
    resize_keyboard=True
)

# Приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name
    last_name = user.last_name or ""
    full_name = f"{name} {last_name}".strip()
    await update.message.reply_text(
        f"Привет, {full_name}!\nДобро пожаловать в\nПриёмную Поздравлений 🎉\nТыкай рядом со скрепкой ;)",
        reply_markup=keyboard
    )

# Обработка текстовых сообщений
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user
    username = user.username or user.first_name

    if "Поздравить" in text:
        await update.message.reply_text(
            "Андрюху можно поздравить в этом чате:\nТекстом, картинкой, аудио, видео или анекдотом\n"
            "\nПриёмная сохраняет все поздравления,\nа после передаёт имениннику 🎁"
        )
    elif "Сколько" in text:
        await update.message.reply_text(
            "Мальчику исполнилось 31 годик 🎂\n"
            "Смело закидываем ему 31 рубль 🤑\nна карту"
        )
    elif "анекдот" in text.lower():
        joke = random.choice(jokes)
        await update.message.reply_text(f"Вжух анекдот:\n\n{joke}")
    else:
        save_message(username, text)
        reply = random.choice(thanks_replies)
        await update.message.reply_text(reply)

# Обработка медиа
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.effective_user
    user_id = user.id
    username = user.username or user.first_name

    if "Поздравить" in text:
        if has_congratulated(user_id):
            await update.message.reply_text("Ты уже начал поздравлять 🎉 Можешь добавить что-то ещё — я всё сохраню! 😉")
        else:
            await update.message.reply_text(
                "Андрюху можно поздравить в этом чате:\nТекстом, картинкой, аудио, видео или анекдотом\n"
                "\nПриёмная сохраняет все поздравления,\nа после передаёт имениннику 🎁"
            )
            mark_as_congratulated(user_id)

    elif "Сколько" in text:
        await update.message.reply_text(
            "Мальчику исполнилось 31 годик 🎂\n"
            "Идея! Закидываем ему 31 рубль 🤑\n"
            "на карту Сбера по номеру number 😄\n"
        )

    elif "анекдот" in text.lower():
        joke = random.choice(jokes)
        await update.message.reply_text(f"Вжух анекдот:\n\n{joke}")

    else:
        if not has_congratulated(user_id):
            await update.message.reply_text("Сначала нажми кнопку 'Поздравить'\nОна снизу справа около скрепки 😉")
        else:
            save_message(username, text)
            reply = random.choice(extra_replies)
            await update.message.reply_text(reply)

# Сохраняем сообщение в текстовый файл
def save_message(username, message):
    with open("congratulations.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {username}: {message}\n")

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token("ToKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(
        filters.PHOTO | filters.Sticker.ALL | filters.VIDEO | filters.Document.ALL, handle_text
    ))

    app.run_polling()
