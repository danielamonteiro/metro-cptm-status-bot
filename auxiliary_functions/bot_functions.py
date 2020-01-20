
import logging
import telegram
from telegram.ext.dispatcher import run_async
import os

from auxiliary_functions.treat_lines_response import TreatLinesResponse

class BotFunctions:

    @run_async
    def start_response(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        welcome_message = "🤖 Oi, tudo bem? Eu sou um bot que vai te ajudar a saber o status das linhas de Metro/Cptm de SP. 🚈🚇\nPara saber o status de todas as linhas, mande o comando /todas_as_linhas \nPara saber o status de alguma linha específica mande o comando /linha, por exemplo: para saber o status da linha lilás mande /lilas (sempre sem acentos) e assim por diante. 🤙 \n💥NOVIDADE:💥 Para receber o mapa oficial das linhas de Metro/CPTM de SP em pdf mande /mapa\n\n⛔ATENÇÃO:⛔ Sou um projeto independente, portanto não tenho ligação nenhuma com os canais oficiais do Metro e/ou CPTM!"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {welcome_message}")

    @run_async
    def help_response(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        help_message = "A qualquer momento você pode mandar /todas_as_linhas para saber o status de todas as linhas do Metro/CPTM ou mandar /linha para saber o status de alguma linha específica, por exemplo, /azul (sempre sem acentos) para saber o status da linha azul e assim por diante. 🚇\n\n💥NOVIDADE💥: Agora você pode enviar o comando /mapa e receber um arquivo (em formato de pdf) do mapa oficial das linhas de Metro/CPTM de São Paulo, tenta aí. 😁"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {help_message}")

    @run_async
    def all_lines(self, update, context):
        self.lines_response = TreatLinesResponse()
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        all_lines_message = self.lines_response.create_response_all_lines(self.lines_response.response_all_line)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=all_lines_message, parse_mode=telegram.ParseMode.MARKDOWN)
        all_line = all_lines_message.replace("\n", "")
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {str(all_line)}")

    @run_async
    def one_line(self, update, context):
        self.lines_response = TreatLinesResponse()
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        line = update.message.text.replace("lilas", "lilás")
        line = line.strip("/")
        one_line_message = self.lines_response.create_response_one_line(self.lines_response.response_all_line, line)
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=one_line_message, parse_mode=telegram.ParseMode.MARKDOWN)
        one_line = one_line_message.replace("\n", "")
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {str(one_line)}")

    @run_async
    def send_map_file(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.UPLOAD_DOCUMENT)
        try:
            context.bot.send_document(chat_id=update.effective_chat.id, document="http://www.metro.sp.gov.br/pdf/mapa-da-rede-metro.pdf", filename="Mapa linhas Metro e CPTM - SP")
            logging.info(f"ChatID [{update.effective_chat.id}] Arquivo PDF do mapa do Metro/CPTM enviado com sucesso!")
        except:
            download_fail_message = "Desculpe, a página do Metro onde eu faço o download do mapa oficial das linhas não está disponível. 😔 Tente novamente mais tarde."
            context.bot.send_message(chat_id=update.effective_chat.id, text=download_fail_message, parse_mode=telegram.ParseMode.MARKDOWN)
            logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {download_fail_message}")

    @run_async
    def unknown(self, update, context):
        logging.info(f"ChatID [{update.effective_chat.id}] User Name: {update.effective_chat.first_name} {update.effective_chat.last_name}")
        logging.info(f"ChatID [{update.effective_chat.id}] User input: {update.message.text}")
        unknown_message = "Poxa, desculpa, mas ainda não sou capaz de responder essa mensagem. 😔\nMande /help para saber quais comandos eu consigo responder! 😉"
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
        context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_message)
        logging.info(f"ChatID [{update.effective_chat.id}] BOT's response: {unknown_message}")