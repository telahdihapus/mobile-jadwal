from bs4 import BeautifulSoup
import requests

req = requests.get('http://gilabola.com/berita-bola/jadwal-bola-malam-ini/')
req = req.text
soup = BeautifulSoup(req, "html.parser")
#print(soup)
table = soup.find('table', attrs={'class':'tablepress tablepress-id-5'})
table_body = table.find('tbody')
#print(table_body)
data = []
rows = table_body.find_all('tr')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele.replace('\n', ': ') for ele in cols if ele])
i = 1

datax = []
js = {}
for data_ in data:
	js['tanggal'] = data_[0]
	js['jadwal'] = data_[1]
	js['tv'] = data_[2]
	datax.append(js)

nama = 'data.json'
save = open(nama, 'w+')
save.write(str(datax))
save.close()