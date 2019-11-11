from datetime import datetime

from get_data.get_lines_status import AllLinesStatus

class TreatLinesResponse:
    def __init__(self):
        self.all_lines_status = AllLinesStatus()
        self.lines_status_response = self.all_lines_status.get_all_lines()[1]
        self.response_all_line = self.create_lines_status_list(self.lines_status_response)
    
    
    def create_lines_status_list(self, status_response):
        response_list = []
        for line in status_response:
            line_name = line['Nome'].capitalize()
            line_number = line['LinhaId']
            line_status = line['Status']
            line_description = line['Descricao']
            response_list.append([line_number, line_name, line_status, line_description])
        date = self.format_update_date(status_response[-1:][0]['DataGeracao'])
        response_list.append(date)

        return response_list

    
    def create_response_all_lines(self, response_list):
        text_response = ""
        for line in response_list[:-1]:
            if not line[3]:
                text_response = text_response + f"*Linha {line[0]} - {line[1]}*\n*Status:*\n✅ {line[2]}\n\n"
                if line[2] in ["Operações Encerradas", "Operação Encerrada"]: 
                    text_response = text_response.replace("✅", "❌")
            else:
                text_response = text_response + f"*Linha {line[0]} - {line[1]}*\n*Status:*\n❌ {line[2]}\n*Motivo:* {line[3]}\n\n"
        text_response = text_response + f"\n_Data de atualização: \n{response_list[-1:][0]}_"
        
        return text_response


    def create_response_one_line(self, response_list, line):
        text_response = ""
        for line_response in response_list[:-1]:
            if line.capitalize() in line_response:
                if not line_response[3]:
                    text_response = text_response + f"*Linha {line_response[0]} - {line_response[1]}*\n*Status:*\n✅ {line_response[2]}\n"
                    if line_response[2] in ["Operações Encerradas", "Operação Encerrada"]:
                        text_response = text_response.replace("✅", "❌")
                else:
                    text_response = text_response + f"*Linha {line_response[0]} - {line_response[1]}*\n*Status:*\n❌ {line_response[2]}\n*Motivo:* {line_response[3]}\n"
        text_response = text_response + f"\n_Data de atualização: \n{response_list[-1:][0]}_"

        return text_response
    

    def format_update_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        formatted_date = date.strftime("%d/%m/%Y - %H:%M")

        return formatted_date





