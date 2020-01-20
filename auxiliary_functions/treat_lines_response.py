from datetime import datetime

from get_data.get_lines_status import AllLinesStatus

class TreatLinesResponse:
    def __init__(self):
        self.all_lines_status = AllLinesStatus()
        self.response_all_line = self.all_lines_status.get_all_lines()[1]

    
    def create_response_all_lines(self, response_list):
        try:
            text_response = ""
            for line in response_list:
                if not line.get('Descricao'):
                    text_response = text_response + f"*Linha {line.get('LinhaId')} - {line.get('Nome').capitalize()}*\n*Status:*\n✅ {line.get('Status')}\n\n"
                    if line.get('Status') in ["Operações Encerradas", "Operação Encerrada", "Operação Parcial"]: 
                        text_response = text_response.replace("✅", "❌")
                else:
                    text_response = text_response + f"*Linha {line.get('LinhaId')} - {line.get('Nome')}*\n*Status:*\n❌ {line.get('Status')}\n*Motivo:* {line.get('Descricao')}\n\n"
            text_response = text_response + f"\n_Data de atualização: \n{self.format_update_date(response_list[0].get('DataGeracao'))}_"
        except:
            text_response = "Hey, desculpe, eu tive um probleminha para acessar o serviço que me traz o status da linhas. 😥\nPor favor, envie o comando novamente para que eu possa tentar mais uma vez. Juro que não foi minha culpa."
        
        return text_response


    def create_response_one_line(self, response_list, line):
        text_response = ""
        for line_response in response_list:
            if line.upper() == line_response.get("Nome").upper():
                if not line_response.get('Descricao'):
                    text_response = text_response + f"*Linha {line_response.get('LinhaId')} - {line_response.get('Nome').capitalize()}*\n*Status:*\n✅ {line_response.get('Status')}\n"
                    if line_response.get('Status') in ["Operações Encerradas", "Operação Encerrada"]:
                        text_response = text_response.replace("✅", "❌")
                else:
                    text_response = text_response + f"*Linha {line_response.get('LinhaId')} - {line_response.get('Nome').capitalize()}*\n*Status:*\n❌ {line_response.get('Status')}\n*Motivo:* {line_response.get('Descricao')}\n"
        if text_response:
            text_response = text_response + f"\n_Data de atualização: \n{self.format_update_date(line_response.get('DataGeracao'))}_"    
        else:
            text_response = "Hey, desculpe, eu tive um probleminha para acessar o serviço que me traz o status da linha solicitada. 😥\nPor favor, envie o comando novamente para que eu possa tentar mais uma vez. Juro que não foi minha culpa."
              

        return text_response
    

    def format_update_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        formatted_date = date.strftime("%d/%m/%Y - %H:%M")

        return formatted_date





