from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


menu_start=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Math"),
            KeyboardButton(text="Trivia"),
        ],
        [
            KeyboardButton(text="Date"),

        ],
    ],
    resize_keyboard=True
)