import requests
import json
#TODO: transformar os prints em log

class AllLinesStatus:
    
    def __init__(self):
        #TODO: alterar para pegar do json
        self.line_status_url = "http://apps.cptm.sp.gov.br:8080/AppMobileService/api/LinhasMetropolitanasAppV3?versao=4"

    
    def get_all_lines(self):

        try:
            all_lines_response = requests.get(self.line_status_url)
            all_lines_status_code = all_lines_response.status_code
            all_lines_status = json.loads(all_lines_response.text)
            information_unavailable = self.check_all_lines_info(all_lines_status)
            print(information_unavailable)
            
            if all_lines_status_code == 200 and information_unavailable == False:
                #print(all_lines_status)
                #print(all_lines_status_code)
                for line in all_lines_status:
                    print(line['LinhaId'], line['Nome'], line['Tipo'])
            else:
                #TODO: implementar consulta nos outros endpoints
                print("Status diferente de 200 ou informação indisponível")
        except Exception as e:
            print("Deu merda")
            print(e)
        if all_lines_response:
            return all_lines_status_code, all_lines_status


    def check_all_lines_info(self, all_lines_response):
        information_unavailable = False
        #TODO: validar o texto exato
        for line in all_lines_response:
            print(line['Status'])
            if "xx" in line['Status']:
                information_unavailable = True
                break
        
        return information_unavailable

status_lines = AllLinesStatus()
a, b = status_lines.get_all_lines()
print(a, b)
print(type(a), print(type(b)))


