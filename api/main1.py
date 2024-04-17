from fastapi import Request, FastAPI
from bs4 import BeautifulSoup
import requests
from preprocess import preprocessing


app = FastAPI()

@app.post("/json")

async def get_body(request: Request):
    return await request.body()
###uvicorn main:app --reload
@app.get("/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}
@app.get("/")
###def read_user(url: str ):
def read_user(url: str ,HTMLelement):
    filtered_titles = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    testing=str(HTMLelement)
    titles = soup.findAll(testing)
    for data in titles:
        filtered_titles.append(data.text)
        texst=(' '.join(str(el) for el in filtered_titles))
    #return{"txt":filtered_titles}
    return{"txt":texst}