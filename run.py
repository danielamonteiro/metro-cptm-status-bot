import telebot

from treat_lines_response import TreatLinesResponse

token_bot = "922691719:AAHcOSM49xGbFD_aCoMHOEVG2yP_CtRRgfQ"

bot = telebot.TeleBot(token_bot)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_message = "Oi, tudo bem? Eu sou um <b>bot</b> que vai te ajudar a saber o status das linhas de Metro/Cptm de SP. \nPara saber o status de todas as linhas, mande o comando /todas_as_linhas \nPara saber o status de alguma linha específica mande o comando /linha \nPor exemplo, para saber o status da linha azul, mande /azul e assim por diante ;)"
    bot.reply_to(message, welcome_message)

@bot.message_handler(commands=['todas_as_linhas'])
def send_all_lines(message):
    all_lines = TreatLinesResponse()
    all_lines_message = all_lines.create_response_all_lines(all_lines.response_all_line)
    bot.reply_to(message, all_lines_message)

@bot.message_handler(commands=['azul', 'linha_azul'])
def send_blue_line(message):
    all_lines = TreatLinesResponse()
    blue_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'azul')
    bot.reply_to(message, blue_line_message)

@bot.message_handler(commands=['verde', 'linha_verde'])
def send_green_line(message):
    all_lines = TreatLinesResponse()
    green_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'verde')
    bot.reply_to(message, green_line_message)

@bot.message_handler(commands=['vermelha', 'linha_vermelha'])
def send_red_line(message):
    all_lines = TreatLinesResponse()
    red_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'vermelha')
    bot.reply_to(message, red_line_message)

@bot.message_handler(commands=['amarela', 'linha_amarela'])
def send_yellow_line(message):
    all_lines = TreatLinesResponse()
    yellow_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'amarela')
    bot.reply_to(message, yellow_line_message)

@bot.message_handler(commands=['lilás', 'lilas', 'linha_lilas'])
def send_lilac_line(message):
    all_lines = TreatLinesResponse()
    lilac_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'lilás')
    bot.reply_to(message, lilac_line_message)

@bot.message_handler(commands=['prata', 'linha_prata'])
def send_silver_line(message):
    all_lines = TreatLinesResponse()
    silver_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'prata')
    bot.reply_to(message, silver_line_message)

@bot.message_handler(commands=['rubi', 'linha_rubi'])
def send_ruby_line(message):
    all_lines = TreatLinesResponse()
    ruby_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'rubi')
    bot.reply_to(message, ruby_line_message)

@bot.message_handler(commands=['diamante', 'linha_diamante'])
def send_diamond_line(message):
    all_lines = TreatLinesResponse()
    diamond_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'diamante')
    bot.reply_to(message, diamond_line_message)

@bot.message_handler(commands=['esmeralda', 'linha_esmeralda'])
def send_emerald_line(message):
    all_lines = TreatLinesResponse()
    emerald_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'esmeralda')
    bot.reply_to(message, emerald_line_message)

@bot.message_handler(commands=['turquesa', 'linha_turquesa'])
def send_turquoise_line(message):
    all_lines = TreatLinesResponse()
    turquoise_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'turquesa')
    bot.reply_to(message, turquoise_line_message)

@bot.message_handler(commands=['coral', 'linha_coral'])
def send_coral_line(message):
    all_lines = TreatLinesResponse()
    coral_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'turquesa')
    bot.reply_to(message, coral_line_message)

@bot.message_handler(commands=['safira', 'linha_safira'])
def send_sapphire_line(message):
    all_lines = TreatLinesResponse()    
    sapphire_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'safira')
    bot.reply_to(message, sapphire_line_message)

@bot.message_handler(commands=['jade', 'linha_jade'])
def send_jade_line(message):
    all_lines = TreatLinesResponse()    
    jade_line_message = all_lines.create_response_one_line(all_lines.response_all_line, 'jade')
    bot.reply_to(message, jade_line_message)


if __name__ == "__main__":
    bot.polling()


