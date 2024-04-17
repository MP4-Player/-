from fastapi import Request, FastAPI
import requests
from bs4 import BeautifulSoup




apppp = FastAPI()

@apppp.get("/")
@apppp.get("/")
def read_user(url: str ,HTMLelement:str):
    filtered_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    titles = soup.findAll(HTMLelement)
    for data in titles:
        filtered_titles.append(data.text)
        global titlese
        titlese=(' '.join(filtered_titles))
        titlese=titlese.replace("\ ",' ').replace('/',' ').replace('.',' ').replace('[',' ').replace(']',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace('[',' ').replace(']',' ').replace('"',' ').replace("'",' ').replace('%',' ').replace('<',' ').replace('>',' ').replace('1',' ').replace('2',' ').replace('3',' ').replace('4',' ').replace('5',' ').replace('6',' ').replace('7',' ').replace('8',' ').replace('9',' ').replace('0',' ')
    return(titlese)
