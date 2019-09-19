import requests
import json

class LinesStatus:
    
    def get_all_lines(self):
        #TODO: alterar para pegar do json
        self.all_lines_url = "http://apps.cptm.sp.gov.br:8080/AppMobileService/api/LinhasMetropolitanasAppV3?versao=4"

        try:
            #all_lines_response = requests.get(self.all_lines_url)
            #all_lines_status = all_lines_response.status_code
            

            all_lines_status = 200
            all_lines_response = open("mock_status.json", encoding="utf8")
            all_lines_response = json.load(all_lines_response)
            information_unavailable = self.check_all_lines_info(all_lines_response)
            if all_lines_status == 200 and information_unavailable == False:
                #print(all_lines_response.text)
                print(all_lines_response)
            else:
                #TODO: implementar consulta nos outros endpoints
                print("Status diferente de 200 ou informação indisponível")
        except Exception as e:
            print("Deu merda")
            print(e)
        if all_lines_response and all_lines_response:
            return all_lines_status, all_lines_response


    def check_all_lines_info(self, all_lines_response):
        all_lines_response = json.loads(all_lines_response)

        #TODO: validar o texto exato
        if "Informação Indisponível" in all_lines_response:
            information_unavailable = True
        else:
            information_unavailable = False
        
        return information_unavailable

status_lines = LinesStatus()
a, b = status_lines.get_all_lines()
print(a, b)

