
from auxiliary_functions.treat_lines_response import TreatLinesResponse
import telegram

lines_response = TreatLinesResponse()

def start(update, context):
    welcome_message = "Oi, tudo bem? Eu sou um bot que vai te ajudar a saber o status das linhas de Metro/Cptm de SP. \nPara saber o status de todas as linhas, mande o comando /todas_as_linhas \nPara saber o status de alguma linha específica mande o comando /linha \nPor exemplo, para saber o status da linha azul, mande /azul e assim por diante ;)\n *ATENÇÃO:* Sou um projeto independente, portanto não tenho ligação nenhuma com os canais oficiais do Metro e/ou CPTM!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, parse_mode=telegram.ParseMode.MARKDOWN)

def help(update, context):
    help_message = "A qualquer momento você pode mandar /todas_as_linhas para saber o status de todas as linhas do Metro/CPTM ou mandar /linha para saber o status de alguma linha específica (por exemplo, /azul para saber o status da linha azul e assim por diante)."
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message, parse_mode=telegram.ParseMode.MARKDOWN)

def all_lines(update, context):
    all_lines_message = lines_response.create_response_all_lines(lines_response.response_all_line)
    context.bot.send_message(chat_id=update.effective_chat.id, text=all_lines_message, parse_mode=telegram.ParseMode.MARKDOWN)

def one_line(update, context):
    line = update.message.text
    line = line.strip("/")
    one_line_message = lines_response.create_response_one_line(lines_response.response_all_line, line)
    context.bot.send_message(chat_id=update.effective_chat.id, text=one_line_message, parse_mode=telegram.ParseMode.MARKDOWN)