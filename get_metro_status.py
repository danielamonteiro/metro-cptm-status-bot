import json
import xmltodict
from zeep import Client

client = Client('http://apps.metrosp.com.br/api/diretodometro/v1/SituacaoLinhasMetro.asmx?WSDL')

result = client.service.GetSituacaoTodasLinhas('B7758201-15AF-4246-8892-EAAFFC170515')
diretodometro = json.loads(json.dumps(xmltodict.parse(result)))['diretodometro']
print(diretodometro)
#for linha in diretodometro['linhas']['linha']:
#    print(linha['nome'],linha['situacao'])