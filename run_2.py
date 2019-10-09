import logging

from telegram.ext import Updater, CommandHandler
from auxiliary_functions.bot_functions import all_lines, one_line

token_bot = "922691719:AAHcOSM49xGbFD_aCoMHOEVG2yP_CtRRgfQ"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

bot_updater = Updater(token=token_bot, use_context=True)
bot_dispatcher = bot_updater.dispatcher

#start_handler = CommandHandler('start', start)
#bot_dispatcher.add_handler(start_handler)

all_lines_handler = CommandHandler('todas_as_linhas', all_lines)
bot_dispatcher.add_handler(all_lines_handler)

one_line_handler = CommandHandler(['azul', 'linha_azul', 'vermelha'], one_line)
bot_dispatcher.add_handler(one_line_handler)

if __name__ == "__main__":
    bot_updater.start_polling()
    bot_updater.idle()





#pegar dados da pessoa update.effective_chat: {'id': 365484793, 'type': 'private', 'first_name': 'Daniela', 'last_name': 'Monteiro'}
#pegar texto enviado update.message.text