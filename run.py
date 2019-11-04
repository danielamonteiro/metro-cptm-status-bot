import logging
import os 

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from auxiliary_functions.bot_functions import BotFunctions
from auxiliary_functions.bot_commands import BotCommands
from config.set_log_config import check_config_file
from dotenv import load_dotenv


def main():
    check_config_file()
    load_dotenv()
    logging.info("######## Starting Application #######")    
    
    token_bot = os.getenv("BOT_TOKEN")    
    bot_updater = Updater(token=token_bot, use_context=True)
    bot_dispatcher = bot_updater.dispatcher

    BotCommands(bot_updater, bot_dispatcher)
    
    bot_updater.start_polling()
    bot_updater.idle()

if __name__ == "__main__":
    main()