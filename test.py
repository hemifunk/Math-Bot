import unittest
from program import show_topic_options
from consts import TOPIC_OPTIONS_KEYBOARD
from unittest.mock import AsyncMock, MagicMock
from utils import create_keyboard, group_buttons
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class TestKeyboardUtils(unittest.TestCase):

    def test_create_keyboard(self):
        buttons = ['button1', 'button2', 'button3']
        result = create_keyboard(buttons)
        expected = [[InlineKeyboardButton('button1', callback_data='button1'), InlineKeyboardButton('button2', callback_data='button2')],
                    [InlineKeyboardButton('button3', callback_data='button3')]]
        self.assertEqual(result, expected)

    def test_group_buttons(self):
        buttons = [[InlineKeyboardButton('button1', callback_data='button1')],
                   [InlineKeyboardButton('button2', callback_data='button2')],
                   [InlineKeyboardButton('button3', callback_data='button3')]]
        result = group_buttons(buttons)
        expected = [[InlineKeyboardButton('button1', callback_data='button1'), InlineKeyboardButton('button2', callback_data='button2')],
                    [InlineKeyboardButton('button3', callback_data='button3')]]
        self.assertEqual(result, expected)


class TestShowTopicOptions(unittest.TestCase):
    def setUp(self):
        self.update = AsyncMock()
        self.context = MagicMock()
        self.context.user_data = {}

    async def test_show_topic_options(self):
        self.update.message.text = 'Test Topic'
        self.update.message.reply_text = AsyncMock()

        await show_topic_options(self.update, self.context)

        self.assertEqual(self.context.user_data['topic'], 'Test Topic')
        self.update.message.reply_text.assert_called_once_with(
            f"*יאללה Test Topic, איך אפשר לעזור?*",
            reply_markup=InlineKeyboardMarkup(TOPIC_OPTIONS_KEYBOARD),
            parse_mode='Markdown'
        )


if __name__ == '__main__':
    unittest.main()
