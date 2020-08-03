#Function to retrieve article titles and links from a given page:

#Imports:
import requests
from bs4 import BeautifulSoup
import json

#Links I will use stored as variables for later
hx = "http://www.upte.org/local/new/contracts-hx/"
rx = "http://www.upte.org/local/new/contracts-rx/"
tx = "http://www.upte.org/local/new/contracts-tx/"

def LinkRetriever(link, fileName):
    #open a session to the link and retrieve page
    with requests.Session() as s:
        req = s.get(link)

        #parse link page and obtain desired data
        soup = BeautifulSoup(req.text, 'html.parser')

        #retrieves table body with links, article # and article name
        table = soup.find('div', class_ = "entry-content").table.tbody

        

        #create a python dictionary with article number as key and article name and link as values:
        

        articleNos = [i.text for i in table.select('tr td:nth-of-type(1)')]
        articleTitles = [i.text for i in table.select('tr td:nth-of-type(2)')]
        articleLinks = [i['href'] for i in table.select('tr td:nth-of-type(2) a')]
        

        data = [{'Article Number' : a, 'Article Name' : b, 'Article Link' : c} for (a,b,c) in zip(articleNos, articleTitles, articleLinks)]

    #using passed fileName, we pull data from link and assign it to a JSON file
    with open(f'{fileName}.json', 'w') as file:
        file.write(json.dumps(data)) 
    

#Calling function to pull data and create JSON files
#LinkRetriever(rx, 'RXContract')
#LinkRetriever(hx, 'HXContract')
#LinkRetriever(tx, 'TXContract')

#Example of results in JSON file (first 5 records):

with open('HXContract.json') as f:
    HX = json.load(f)

for i in HX[0:5]:
    print(i, end="\n\n")