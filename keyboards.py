from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard():
    keyboard = ReplyKeyboardMarkup(keyboard=
    [
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/help")
        ],
        [
            KeyboardButton(text="/about")
        ]
    ], resize_keyboard=True)
    return keyboard



