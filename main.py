from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ConversationHandler, PicklePersistence
from consts import START_MENU_KEYBOARD, TOKEN
from logger import setup_logger
from program import utils_features_handlers


main_logger = setup_logger("main_logger")


async def start(update, context):

    user_details = update.message.from_user
    private_name = user_details.first_name

    reply_markup = ReplyKeyboardMarkup(START_MENU_KEYBOARD)

    await update.message.reply_text(text=f"היי {private_name}🙂 מה אפשר ללמד אותך היום?", reply_markup=reply_markup)
    return ConversationHandler.END


def main():

    main_logger.info("Bot started!")
    
    persistence = PicklePersistence(filepath=r"C:\Users\User\OneDrive\MathBotProject\Math-Bot\data_math_bot.txt")
    app = Application.builder().token(TOKEN).persistence(persistence).build()


    app.add_handlers(utils_features_handlers)
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

    main_logger.info("Bot finished!")


if __name__ == '__main__':
    main()
