from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from auxiliary_functions.bot_functions import BotFunctions

class BotCommands:
    def __init__(self, bot_updater, bot_dispatcher):
        bot_functions = BotFunctions()

        start_handler = CommandHandler('start', bot_functions.start_response)
        bot_dispatcher.add_handler(start_handler)

        help_handler = CommandHandler('help', bot_functions.help_response)
        bot_dispatcher.add_handler(help_handler)

        all_lines_handler = CommandHandler('todas_as_linhas', bot_functions.all_lines)
        bot_dispatcher.add_handler(all_lines_handler)

        one_line_handler = CommandHandler(['azul', 'verde', 'vermelha', 'amarela', 'lilas', 'prata', 'rubi','diamante', 
                                            'esmeralda', 'turquesa', 'coral', 'safira', 'jade'], bot_functions.one_line)
        bot_dispatcher.add_handler(one_line_handler)

        unknown_handler = MessageHandler(Filters.command, bot_functions.unknown)
        bot_dispatcher.add_handler(unknown_handler)

        unknown_message_handler = MessageHandler(Filters.text, bot_functions.unknown)
        bot_dispatcher.add_handler(unknown_message_handler)