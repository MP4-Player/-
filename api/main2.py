 #uvicorn main:app --reload --port 5000
from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests
from preprocess import preprocessing


app2 = FastAPI()

@app2.post("/json")

async def get_body(request: Request):
    return await request.body()
#uvicorn main:app --reload
#@appp.get("/{user_id}")
@app2.get("/")
#def read_user(user_id: str):
#    return {"user_idNEWAPI2": user_id}
def get_text(text: str):
   res = requests.get("http://127.0.0.1:5100/", params={"url": text})
   filtereded_titles = res.text
   vvod=str(filtereded_titles)
   vvod=vvod.replace('.',' ').replace(',',' ').replace('-',' ').replace(':',' ').replace(';',' ').replace('_',' ').replace('[',' ').replace(']',' ').replace('"',' ').replace("'",' ')
   print(vvod)
   dlin= str(vvod).split()
   s=max(dlin, key=len)
   chasto = vvod.split() 
   Countered = Counter(chasto )   
   chastovst = Countered.most_common(1)
   return [s,chastovst[0][0]]

   
    #return{"txt":titles}
#uvicorn 2main:appp --reload --port 5000