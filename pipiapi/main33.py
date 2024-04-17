from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests
import collections
from preprocess import preprocessing
###uvicorn main3:apppp --reload

ap = FastAPI()

@ap.get("/")
def read_user(url: str):
    filtered_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    titles = soup.findAll('title')
    for data in titles:
        filtered_titles.append(data.text)
        stroka = ' '
        for j in filtered_titles:
            stroka += str(j)+ ' ' 
    #stroka=titleses
 #def rabot(words):
    vvod=str(stroka)
    vvod.replace('.',' ').replace('[',' ').replace(']',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace('[',' ').replace(']',' ').replace('"',' ').replace("'",' ').replace('%',' ').replace('<',' ').replace('>',' ')
    print('ППППППППППППППППППППППООООООООООООООООООООССССССССССССССССССЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬЬМММММММММММООООООООООТРИ СЮДА',vvod)
    dlin= str(vvod).split()
    s=max(dlin, key=len)
    chasto = vvod.split() 
    Countered = collections.Counter(chasto )   
    chastovst = Countered.most_common(1)
    return [titles,s,chastovst[0][0]]