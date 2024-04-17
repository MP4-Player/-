from fastapi import Request, FastAPI 
import collections
import uvicorn
import requests
from collections import Counter

apppp = FastAPI()


@apppp.get("/")

async def get_text( UrlAPI:str,url: str,HTMLelement: str):

    payload = {"url": url, "HTMLelement": HTMLelement}
    res = requests.get(UrlAPI, params=payload)
    words = res.text
    vvod=words
    vvod.replace("\ ",' ').replace('/',' ').replace('.',' ').replace('[',' ').replace(']',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace('[',' ').replace(']',' ').replace('"',' ').replace("'",' ').replace('%',' ').replace('<',' ').replace('>',' ').replace('1',' ').replace('2',' ').replace('3',' ').replace('4',' ').replace('5',' ').replace('6',' ').replace('7',' ').replace('8',' ').replace('9',' ').replace('0',' ')
    dlin= str(vvod).split()
    s=max(dlin, key=len)
    chasto = vvod.split() 
    Countered = Counter(chasto )   
    chastovst = Countered.most_common(1)
    return [s,chastovst[0][0]]