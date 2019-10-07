import telebot

from treat_lines_response import TreatLinesResponse

token_bot = "922691719:AAHcOSM49xGbFD_aCoMHOEVG2yP_CtRRgfQ"

bot = telebot.TeleBot(token_bot)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_message = "Oi, tudo bem? Eu sou um bot que vai te ajudar a saber o status das linhas de Metro/Cptm de SP. \nPara saber o status de todas as linhas, mande o comando /todas_as_linhas \nPara saber o status de alguma linha específica mande o comando /linha \nPor exemplo, para saber o status da linha azul, mande /azul e assim por diante ;)"
    bot.reply_to(message, welcome_message)

@bot.message_handler(commands=['todas_as_linhas'])
def send_all_lines(message):
    all_lines = TreatLinesResponse()
    all_lines_message = all_lines.construct_all_lines_response()
    bot.reply_to(message, all_lines_message)


bot.polling()