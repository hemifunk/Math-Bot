from telegram import InlineKeyboardButton, KeyboardButton

TOKEN = "6835045984:AAFs2I3CG7xxHEeTkVNsfjYFRy1PnYgsVGg"

START_MENU_KEYBOARD = [
        [
        KeyboardButton("פונקציית מנה"),
        KeyboardButton("פונקציית שורש"),
        KeyboardButton("פונקציית טריגו")
        ],
        [
        KeyboardButton("בעיות תנועה"),
        KeyboardButton("בעיות קיצון"),
        KeyboardButton("סדרות")
        ],
        [
        KeyboardButton("הסתברות"),
        KeyboardButton("גיאומטריה"),
        KeyboardButton("טריגונומטריה")
        ]
]

TOPIC_MENU_KEYBOARD =    [[InlineKeyboardButton("שיעורים מוקלטים", callback_data="videos"),
                          InlineKeyboardButton("הצטרפות לקהילה", callback_data="community")],
                          [InlineKeyboardButton("תוכנית למידה", callback_data="planning"),
                          InlineKeyboardButton("בחינות עבר", callback_data="exams")]
                          ]