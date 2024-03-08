import unittest
from unittest.mock import Mock, patch
from telegram.ext import ConversationHandler

from unittest.mock import AsyncMock, MagicMock
from utils import create_keyboard, group_buttons
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


from consts import TOPIC_OPTIONS_KEYBOARD
from program import lessons_videos, communities, study_program, show_topic_options

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

class TestBotFunctions(unittest.TestCase):
    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_lessons_videos(self, mock_update, mock_context):
        mock_context.user_data = {'topic': 'בעיות מילוליות'}
        mock_update.callback_query.message.reply_text = Mock()
        result = await lessons_videos(mock_update, mock_context)
        self.assertEqual(result, ConversationHandler.END)
        mock_update.callback_query.message.reply_text.assert_called_once()

    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_communities(self, mock_update, mock_context):
        mock_context.user_data = {'topic': 'סדרות'}
        mock_update.callback_query.message.reply_text = Mock()
        result = await communities(mock_update, mock_context)
        self.assertEqual(result, ConversationHandler.END)
        mock_update.callback_query.message.reply_text.assert_called_once()

    @patch('telegram.Update')
    @patch('telegram.ext.CallbackContext')
    async def test_study_program(self, mock_update, mock_context):
        mock_context.user_data = {'topic': 'פונקציית שורש'}
        mock_update.callback_query.message.reply_text = Mock()
        result = await study_program(mock_update, mock_context)
        self.assertEqual(result, ConversationHandler.END)
        mock_update.callback_query.message.reply_text.assert_called_once()


if __name__ == '__main__':
    unittest.main()