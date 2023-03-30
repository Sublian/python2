from bs4 import BeautifulSoup
import requests, csv

URL = "https://apewisdom.io/all-crypto/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
criptos = soup.find_all("div", class_="company-name")
criptos =str(criptos)
criptos= criptos.replace('<div class="company-name">', '')
criptos= criptos.replace('</div>,', '/')
criptos= criptos.replace('[', '')
criptos= criptos.replace('</div>]', '')
criptoclean= criptos.split("/")
#criptoclean.pop(0)

#print(criptoclean)

lista =[]
for i in range(5):
    lista.append(criptoclean[i])
    
print(lista)

with open('reddit.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(criptoclean)