from telegram import InlineKeyboardMarkup
from telegram.ext import (ConversationHandler, CallbackQueryHandler, 
                          MessageHandler, CommandHandler, filters)

from consts import (TOPIC_OPTIONS_KEYBOARD, TOPICS_REGEX_PATTERN)

async def show_topic_options(update, context): 
    
    context.user_data['topic'] = update.message.text
    
    topic = context.user_data['topic']

    reply_markup = InlineKeyboardMarkup(TOPIC_OPTIONS_KEYBOARD)

    await update.message.reply_text(f"*יאללה {topic}, איך אפשר לעזור?*", 
                                    reply_markup=reply_markup, parse_mode='Markdown')
    return ConversationHandler.END


topic_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex(TOPICS_REGEX_PATTERN), show_topic_options)
    ],
    states={},
    fallbacks=[],
    name="math",
    persistent=True,
    allow_reentry=True
)

utils_features_handlers = [topic_conversation_handler]


