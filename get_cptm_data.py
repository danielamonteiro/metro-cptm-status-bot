from requests_html import HTMLSession

url = 'http://cptm.sp.gov.br/'
session = HTMLSession()

def get_all_lines_data():
    refs = ['rubi', 'diamante', 'esmeralda', 'turquesa', 'coral', 'safira', 'jade']
    res = session.get(url)

    for ref in refs:
        data = res.html.find('.{0}'.format(ref), first=True)
        yield {
                'line': ref.capitalize(),
                'status': data.text.replace(ref.upper(), '')
            }

    return data

data = get_all_lines_data()
for x in data:
    print(x)

