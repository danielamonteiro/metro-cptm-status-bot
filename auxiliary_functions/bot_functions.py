
import logging
import telegram

from auxiliary_functions.treat_lines_response import TreatLinesResponse

class BotFunctions:
    def __init__(self):
        self.lines_response = TreatLinesResponse()

    def start_response(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        welcome_message = "🤖 Oi, tudo bem? Eu sou um bot que vai te ajudar a saber o status das linhas de Metro/Cptm de SP. 🚈🚇\nPara saber o status de todas as linhas, mande o comando /todas_as_linhas \nPara saber o status de alguma linha específica mande o comando /linha \nPor exemplo, para saber o status da linha azul, mande /azul (sem acentos) e assim por diante.🤙\n⛔ATENÇÃO:⛔ Sou um projeto independente, portanto não tenho ligação nenhuma com os canais oficiais do Metro e/ou CPTM!"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

    def help_response(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        help_message = "A qualquer momento você pode mandar /todas_as_linhas para saber o status de todas as linhas do Metro/CPTM ou mandar /linha para saber o status de alguma linha específica, por exemplo, /azul (sempre sem acentos) para saber o status da linha azul e assim por diante. 🚇"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)

    def all_lines(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        all_lines_message = self.lines_response.create_response_all_lines(self.lines_response.response_all_line)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=all_lines_message, parse_mode=telegram.ParseMode.MARKDOWN)

    def one_line(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        line = update.message.text.replace("lilas", "lilás")
        line = line.strip("/")
        one_line_message = self.lines_response.create_response_one_line(self.lines_response.response_all_line, line)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=one_line_message, parse_mode=telegram.ParseMode.MARKDOWN)

    def unknown(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        unknown_message = "Poxa, desculpa, mas ainda não sou capaz de responder essa mensagem. 😔\nMande /help para saber quais comandos eu consigo responder! 😉"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_message)