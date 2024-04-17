from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests
from preprocess import preprocessing
###uvicorn main3:apppp --reload

apppp = FastAPI()

@apppp.post("/json")
async def get_body(request: Request):
    return await request.body()
@apppp.get("/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}
@apppp.get("/")
###def read_user(url: str ):
def read_user(url: str ,HTMLelement):
    filtered_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    testing=str(HTMLelement)
    titles = soup.findAll(testing)
    for data in titles:
        filtered_titles.append(data.text)
        global titlese
        titlese=(' '.join(filtered_titles))
    #return{"txt":filtered_titles}
    return{"txt":titlese}
#@apppp.get("///")
#def otv(user_name: str):
 #return {"user_name":user_name,"result": rabot(titlese)}