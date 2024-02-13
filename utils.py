from telegram import InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import (ConversationHandler, CallbackQueryHandler, 
                          MessageHandler, CommandHandler, filters)

from consts import TOPIC_MENU_KEYBOARD

async def motion_problem(update, context): 
    
    topic = update.message.text

    reply_markup = InlineKeyboardMarkup(TOPIC_MENU_KEYBOARD)

    await update.message.reply_text(f"*יאללה {topic}, איך לעזור?*", 
                                    reply_markup=reply_markup, parse_mode='Markdown')
    return ConversationHandler.END

motion_problems_handler = MessageHandler(filters.Regex("בעיות תנועה"), motion_problem)

utils_features_handlers = [motion_problems_handler]