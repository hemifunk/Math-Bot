from telegram import InlineKeyboardMarkup
from telegram.ext import (ConversationHandler, CallbackQueryHandler, 
                          MessageHandler, CommandHandler, filters)

from consts import (GEOMETRY_LESSONS, INTEGRALS_LESSONS, PROPABILITY_LESSONS, RATIONALS_FUNCTIONS_LESSONS, ROOT_FUNCTIONS_LESSONS, SERIES_LESSONS, TOPIC_OPTIONS_KEYBOARD,
                    TOPICS_REGEX_PATTERN,
                    CHOOSE_OPTION, TRIGONOMETRY_FUNCTIONS_LESSONS, TRIGONOMETRY_LESSONS,
                    WORD_PROBLEMS_LESSONS)

async def show_topic_options(update, context): 
    
    context.user_data['topic'] = update.message.text
    
    topic = context.user_data['topic']

    reply_markup = InlineKeyboardMarkup(TOPIC_OPTIONS_KEYBOARD)

    await update.message.reply_text(f"*יאללה {topic}, איך אפשר לעזור?*", 
                                    reply_markup=reply_markup, parse_mode='Markdown')
    
    return CHOOSE_OPTION


async def lessons_videos(update, context): 
        
    topic = context.user_data['topic']
    
    if (topic == "בעיות מילוליות"):
        text = WORD_PROBLEMS_LESSONS
    
    if (topic == "סדרות"):
        text = SERIES_LESSONS
        
    if (topic == "פונקציית שורש"):
        text = ROOT_FUNCTIONS_LESSONS
        
    if (topic == "גיאומטריה"):
        text = GEOMETRY_LESSONS
    
    if (topic == "פונקציית טריגו"):
        text = TRIGONOMETRY_FUNCTIONS_LESSONS
    
    if (topic == "הסתברות"):
        text = PROPABILITY_LESSONS
        
    if (topic == "טריגונומטריה"):
        text = TRIGONOMETRY_LESSONS
    
    if (topic == "אינטגרלים"):
        text = INTEGRALS_LESSONS
    
    if (topic == "פונקציית מנה"):
        text = RATIONALS_FUNCTIONS_LESSONS
    
        
    await update.callback_query.message.reply_text(text = text, parse_mode='Markdown')
    return ConversationHandler.END


topic_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex(TOPICS_REGEX_PATTERN), show_topic_options)
    ],
    states={CHOOSE_OPTION: [CallbackQueryHandler(lessons_videos, pattern='^שיעורים מוקלטים$')]},
    fallbacks=[],
    name="math",
    persistent=True,
    allow_reentry=True
)

utils_features_handlers = [topic_conversation_handler]


