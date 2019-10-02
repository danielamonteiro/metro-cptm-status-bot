from get_lines_status import AllLinesStatus

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
        date = status_response[-1:][0]['DataGeracao']
        response_list.append(date)
        response_text = self.create_response_all_lines(response_list)

        return response_text
    
    def create_response_all_lines(self, response_list):
        text_response = ""
        for line in response_list[:-1]:
            if not line[3]:
                text_response = text_response + f"Linha {line[0]} -> {line[1]} - Status: {line[2]}\n"
            else:
                text_response = text_response + f"Linha {line[0]} -> {line[1]} - Status: {line[2]} Motivo: {line[3]}\n"
        text_response = text_response + f"Data de atualização: {response_list[-1:][0]}"
        print(text_response)
        return text_response

lines = TreatLinesResponse()


