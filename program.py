from telegram import InlineKeyboardMarkup
from telegram.ext import (ConversationHandler, CallbackQueryHandler, 
                          MessageHandler, CommandHandler, filters)

from consts import (GEOMETRY_COMMUNITY, GEOMETRY_LESSONS, GEOMETRY_PROGRAM,
                    INTEGRALS_COMMUNITY,
                    INTEGRALS_LESSONS, PROPABILITY_COMMUNITY,
                    PROPABILITY_LESSONS,
                    RATIONALS_FUNCTIONS_COMMUNITY,
                    RATIONALS_FUNCTIONS_LESSONS,
                    ROOT_FUNCTIONS_COMMUNITY,
                    ROOT_FUNCTIONS_LESSONS, ROOT_FUNCTIONS_PROGRAM,
                    SERIES_COMMUNITY, SERIES_LESSONS, SERIES_PROGRAM,
                    TOPIC_OPTIONS_KEYBOARD,
                    TOPICS_REGEX_PATTERN,
                    CHOOSE_OPTION,
                    TRIGONOMETRY_COMMUNITY,
                    TRIGONOMETRY_FUNCTIONS_COMMUNITY,
                    TRIGONOMETRY_FUNCTIONS_LESSONS,
                    TRIGONOMETRY_LESSONS,
                    WORD_PROBLEMS_COMMUNITY,
                    WORD_PROBLEMS_LESSONS,
                    WORD_PROBLEMS_PROGRAM,
                    TRIGONOMETRY_PROGRAM,
                    INTEGRALS_PROGRAM,
                    RATIONALS_FUNCTIONS_PROGRAM,
                    PROPABILITY_PROGRAM,
                    TRIGONOMETRY_FUNCTIONS_PROGRAM)

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
    
        
    await update.callback_query.message.reply_text(text = text)
    return ConversationHandler.END


async def communities(update, context): 
        
    topic = context.user_data['topic']
    
    if (topic == "בעיות מילוליות"):
        text = WORD_PROBLEMS_COMMUNITY
    
    if (topic == "סדרות"):
        text = SERIES_COMMUNITY
        
    if (topic == "פונקציית שורש"):
        text = ROOT_FUNCTIONS_COMMUNITY
        

    if (topic == "גיאומטריה"):
        text = GEOMETRY_COMMUNITY

    if (topic == "פונקציית טריגו"):
        text = TRIGONOMETRY_FUNCTIONS_COMMUNITY

    if (topic == "הסתברות"):
        text = PROPABILITY_COMMUNITY

    if (topic == "טריגונומטריה"):
        text = TRIGONOMETRY_COMMUNITY

    if (topic == "אינטגרלים"):
        text = INTEGRALS_COMMUNITY
    
    if (topic == "פונקציית מנה"):
        text = RATIONALS_FUNCTIONS_COMMUNITY
        
    await update.callback_query.message.reply_text(text = text)
    return ConversationHandler.END


async def study_program(update, context): 
        
    topic = context.user_data['topic']
    
    if (topic == "בעיות מילוליות"):
        text = WORD_PROBLEMS_PROGRAM
    
    if (topic == "סדרות"):
        text = SERIES_PROGRAM
        
    if (topic == "פונקציית שורש"):
        text = ROOT_FUNCTIONS_PROGRAM

    if (topic == "גיאומטריה"):
        text = GEOMETRY_PROGRAM

    if (topic == "פונקציית טריגו"):
        text = TRIGONOMETRY_FUNCTIONS_PROGRAM

    if (topic == "הסתברות"):
        text = PROPABILITY_PROGRAM

    if (topic == "טריגונומטריה"):
        text = TRIGONOMETRY_PROGRAM

    if (topic == "אינטגרלים"):
        text = INTEGRALS_PROGRAM
    
    if (topic == "פונקציית מנה"):
        text = RATIONALS_FUNCTIONS_PROGRAM
        
    await update.callback_query.message.reply_text(text = text)
    return ConversationHandler.END


topic_conversation_handler = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex(TOPICS_REGEX_PATTERN), show_topic_options)
    ],
    states={CHOOSE_OPTION: [CallbackQueryHandler(lessons_videos, pattern='^שיעורים מוקלטים$'), 
                            CallbackQueryHandler(communities, pattern='^הצטרפות לקהילה$'),
                            CallbackQueryHandler(study_program, pattern='^תוכנית למידה$')]},
    fallbacks=[],
    name="math",
    persistent=True,
    allow_reentry=True
)

utils_features_handlers = [topic_conversation_handler,
                           CallbackQueryHandler(lessons_videos, pattern='^שיעורים מוקלטים$'),
                           CallbackQueryHandler(communities, pattern='^הצטרפות לקהילה$'),
                           CallbackQueryHandler(study_program, pattern='^תוכנית למידה$')]


