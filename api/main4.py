from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests
import collections
#from preprocess import preprocessing

ap = FastAPI()
#from main3 import titlese
@ap.post("/json")

async def get_body(request: Request):
    return await request.body()
#uvicorn main4:ap --reload --port 8001
#@appp.get("/{user_id}")
@ap.get("/")
#def read_user(user_id: str):
#    return {"user_idNEWAPI2": user_id}
def read_user(url: str):
    filtered_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    titleses = soup.findAll('span')
    for data in titleses:
        filtered_titles.append(data.text)
        stroka=' '.join(filtered_titles)
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
    return [titleses,s,chastovst[0][0]]